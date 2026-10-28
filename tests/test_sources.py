import sys
import unittest
import tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_sources import collect_urls, request_url
from summarize_sources import classify, csv_cell, write_summary, exit_status

class SourceTests(unittest.TestCase):
    def test_warning_is_not_incomplete_or_missing_page(self):
        report = {"total":1,"pending":0,"complete":True,"results":[{"status":"fetch_failed","http_status":503}]}
        self.assertEqual(exit_status(report),0)
        report["results"][0]["http_status"] = 404
        self.assertEqual(exit_status(report),1)
        report.update(complete=False,pending=1)
        self.assertEqual(exit_status(report),1)

    def test_nested_urls(self):
        urls = set()
        collect_urls({'url':'https://a.test/a#x','supportingUrls':['https://a.test/b#z','javascript:bad'], 'nested':[{'officialUrl':' https://a.test/c '}], 'text':'https://ignore.test'}, urls)
        self.assertEqual(urls, {'https://a.test/a','https://a.test/b','https://a.test/c'})
    def test_encoding(self):
        url = request_url('https://例え.jp/料金?q=食事')
        self.assertTrue(url.startswith('https://xn--'))
        self.assertEqual(request_url(url),url)
        with self.assertRaises(ValueError):request_url('https://user:pass@example.com')
    def test_classification(self):
        self.assertEqual(classify({'http_status':404}),'ページなし（要確認）')
        self.assertEqual(classify({'http_status':403}),'認証・アクセス制限')
        self.assertEqual(classify({'http_status':503}),'接続先サーバーエラー')
        self.assertEqual(classify({'error':'TimeoutError'}),'タイムアウト')
        self.assertEqual(classify({'error':'SSL certificate'}),'証明書・TLS')
    def test_csv_and_incomplete(self):
        self.assertEqual(csv_cell('=1+1'),"'=1+1")
        report={'total':2,'pending':1,'complete':False,'results':[{'url':'https://example.com','status':'reachable'}]}
        with tempfile.TemporaryDirectory() as directory:
            text,complete=write_summary(report,Path(directory))
            self.assertFalse(complete)
            self.assertIn('未完了',text)
            self.assertTrue((Path(directory)/'needs-review.csv').exists())
            report.update(total=1,pending=0,complete=True)
            self.assertTrue(write_summary(report,Path(directory))[1])

if __name__ == '__main__':unittest.main()
