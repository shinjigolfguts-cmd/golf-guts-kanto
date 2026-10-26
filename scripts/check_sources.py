import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "source-check.json"


def collect_urls(value, urls):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ("url", "officialUrl") and isinstance(item, str):
                url = urldefrag(item.strip())[0]
                if urlsplit(url).scheme in ("http", "https"):
                    urls.add(url)
            collect_urls(item, urls)
    elif isinstance(value, list):
        for item in value:
            collect_urls(item, urls)


def check_url(url):
    result = {
        "url": url,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "content_verified": False,
    }
    request = Request(
        url,
        headers={
            "User-Agent": "GOLFGUTS-SourceCheck/1.0",
            "Accept": "*/*",
        },
    )

    try:
        with urlopen(request, timeout=20) as response:
            # 接続確認のみ。本文の正確性は判定しません。
            sample = response.read(1024)
            status = response.status
            result.update({
                "http_status": status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type", ""),
                "status": (
                    "reachable"
                    if status == 200 and sample
                    else "needs_review"
                ),
            })
    except HTTPError as error:
        result.update({
            "status": "fetch_failed",
            "http_status": error.code,
            "error": str(error),
        })
    except Exception as error:
        result.update({
            "status": "fetch_failed",
            "error": f"{type(error).__name__}: {error}",
        })

    return result


def check_host(urls):
    results = []
    for url in urls:
        results.append(check_url(url))
        # 同じサイトへの連続アクセスを抑えます。
        time.sleep(1)
    return results


def main():
    source = (ROOT / "data.js").read_text(encoding="utf-8-sig")
    match = re.search(r"\b(?:const|let|var)\s+DATA\s*=\s*", source)
    if not match:
        raise RuntimeError("data.js 内に DATA が見つかりません。")

    data, _ = json.JSONDecoder().raw_decode(
        source[match.end():].lstrip()
    )
    urls = set()
    collect_urls(data, urls)
    if not urls:
        raise RuntimeError("確認対象のURLがありません。")

    groups = {}
    for url in sorted(urls):
        host = urlsplit(url).hostname
        groups.setdefault(host, []).append(url)

    started = datetime.now(timezone.utc).isoformat()
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        for batch in executor.map(check_host, groups.values()):
            results.extend(batch)

    results.sort(key=lambda item: item["url"])
    reachable = sum(
        item["status"] == "reachable" for item in results
    )
    report = {
        "started_at": started,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "scope": "URL接続確認のみ。掲載内容の正確性は未検証。",
        "total": len(results),
        "reachable": reachable,
        "needs_review": len(results) - reachable,
        "results": results,
    }

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    temporary = REPORT.with_suffix(".tmp")
    temporary.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(REPORT)

    print(f"確認対象: {len(results)}件")
    print(f"接続できたURL: {reachable}件")
    print(f"要確認: {len(results) - reachable}件")
    print("掲載データと内容確認日は変更していません。")


if __name__ == "__main__":
    main()
