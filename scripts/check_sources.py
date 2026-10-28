import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from queue import Empty, Queue
from urllib.error import HTTPError
from urllib.parse import quote, urldefrag, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "source-check.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def collect_urls(value, urls):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ("url", "officialUrl") and isinstance(item, str):
                url = urldefrag(item.strip())[0]
                if urlsplit(url).scheme in ("http", "https"):
                    urls.add(url)
            if key == "supportingUrls" and isinstance(item, list):
                for link in item:
                    if isinstance(link, str) and urlsplit(link.strip()).scheme in ("http", "https"):
                        urls.add(urldefrag(link.strip())[0])
            collect_urls(item, urls)
    elif isinstance(value, list):
        for item in value:
            collect_urls(item, urls)


def request_url(url):
    parts = urlsplit(url)
    host = parts.hostname
    if not host or parts.username is not None:
        raise ValueError("URLのホスト名または認証情報を確認してください")
    host = host.encode("idna").decode("ascii")
    if ":" in host:
        host = "[" + host + "]"
    if parts.port is not None:
        host += ":" + str(parts.port)
    path = quote(parts.path, safe="/%:@!$&'()*+,;=-._~")
    query = quote(parts.query, safe="/%?:@!$&'()*+,;=-._~")
    return urlunsplit((parts.scheme, host, path, query, ""))


def check_once(url):
    result = {"url": url, "checked_at": now(), "content_verified": False}
    try:
        encoded = request_url(url)
        result["requested_url"] = encoded
        request = Request(encoded, headers={
            "User-Agent": "GOLFGUTS-SourceCheck/1.1",
            "Accept": "*/*",
        })
        with urlopen(request, timeout=20) as response:
            sample = response.read(1024)
            result.update({
                "http_status": response.status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type", ""),
                "status": "reachable" if response.status == 200 and sample
                          else "needs_review",
            })
    except HTTPError as error:
        result.update({"status": "fetch_failed",
                       "http_status": error.code, "error": str(error)})
        error.close()
    except Exception as error:
        result.update({"status": "fetch_failed",
                       "error": f"{type(error).__name__}: {error}"})
    return result


def check_url(url):
    # Retry transient failures once; keep TLS/auth errors and content dates intact.
    first = check_once(url)
    error = first.get("error", "").lower()
    retryable = (first.get("http_status") in (500, 502, 503, 504)
                 or "timed out" in error or "timeout" in error
                 or "connection reset" in error)
    if first.get("status") == "reachable" or not retryable:
        first["attempts"] = 1
        return first
    time.sleep(3)
    second = check_once(url)
    second["attempts"] = 2
    second["previous_attempt"] = first
    return second


def check_host(urls, queue):
    for index, url in enumerate(urls):
        if index:
            time.sleep(1)
        queue.put(check_url(url))


def save_report(results, total, started, complete=False):
    reachable = sum(r["status"] == "reachable" for r in results)
    report = {
        "started_at": started,
        "updated_at": now(),
        "completed_at": now() if complete else None,
        "complete": complete,
        "scope": "URL接続確認のみ。掲載内容の正確性は未検証。",
        "total": total,
        "checked": len(results),
        "pending": total - len(results),
        "reachable": reachable,
        "needs_review": len(results) - reachable,
        "results": sorted(results, key=lambda item: item["url"]),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    temporary = REPORT.with_suffix(".tmp")
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2)
                         + "\n", encoding="utf-8")
    temporary.replace(REPORT)


def main():
    source = (ROOT / "data.js").read_text(encoding="utf-8-sig")
    match = re.search(r"\b(?:const|let|var)\s+DATA\s*=\s*", source)
    if not match:
        raise RuntimeError("data.js 内に DATA が見つかりません。")
    data, _ = json.JSONDecoder().raw_decode(source[match.end():].lstrip())
    urls = set()
    collect_urls(data, urls)
    if not urls:
        raise RuntimeError("確認対象のURLがありません。")
    groups = {}
    for url in sorted(urls):
        groups.setdefault(urlsplit(url).hostname, []).append(url)

    started = now()
    results = []
    queue = Queue()
    save_report(results, len(urls), started)
    print(f"確認開始: {len(urls)}件 / {len(groups)}サイト", flush=True)
    clock = time.monotonic()
    last_log = clock
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(check_host, batch, queue)
                   for batch in groups.values()]
        while len(results) < len(urls):
            try:
                results.append(queue.get(timeout=5))
                save_report(results, len(urls), started)
            except Empty:
                for future in futures:
                    if future.done():
                        future.result()
                if all(f.done() for f in futures) and queue.empty():
                    raise RuntimeError("確認結果が不足しています。途中結果を確認してください。")
            current = time.monotonic()
            if current - last_log >= 15 or len(results) == len(urls):
                good = sum(r["status"] == "reachable" for r in results)
                print(f"進捗: {len(results)}/{len(urls)}件 | 接続成功: {good}件"
                      f" | 要確認: {len(results) - good}件"
                      f" | 経過: {int(current - clock)}秒", flush=True)
                last_log = current
        for future in futures:
            future.result()
    save_report(results, len(urls), started, complete=True)
    print("確認完了。掲載データと内容確認日は変更していません。", flush=True)


if __name__ == "__main__":
    main()
