import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_sources import check_url
from summarize_sources import exit_status

class RetryTests(unittest.TestCase):
    @patch('check_sources.time.sleep')
    @patch('check_sources.check_once')
    def test_transient_failure_recovers(self, check, sleep):
        for failure in [{'error':'TimeoutError'}, {'error':'Connection reset'}, {'http_status':500}, {'http_status':502}, {'http_status':503}, {'http_status':504}]:
            first = dict(failure, status='fetch_failed', content_verified=False)
            check.side_effect = [first, {'status':'reachable','http_status':200,'content_verified':False}]
            result = check_url('https://example.test')
            self.assertEqual(result['status'], 'reachable')
            self.assertEqual(result['attempts'], 2)
            self.assertEqual(result['previous_attempt'], first)
            self.assertFalse(result['content_verified'])

    @patch('check_sources.time.sleep')
    @patch('check_sources.check_once')
    def test_auth_tls_notfound_and_success_are_not_retried(self, check, sleep):
        for value in [{'http_status':401}, {'http_status':403}, {'http_status':404}, {'http_status':410}, {'error':'SSL certificate verification failed'}, {'status':'reachable','http_status':200}]:
            check.reset_mock()
            check.return_value = dict(value)
            result = check_url('https://example.test')
            self.assertEqual(result['attempts'], 1)
            check.assert_called_once()
        sleep.assert_not_called()

    @patch('check_sources.time.sleep')
    @patch('check_sources.check_once')
    def test_existing_warning_and_failure_policy_preserved(self, check, sleep):
        for final_code, expected in [(503,0),(404,1),(410,1)]:
            check.side_effect = [{'status':'fetch_failed','http_status':503}, {'status':'fetch_failed','http_status':final_code}]
            result = check_url('https://example.test')
            self.assertEqual(result['status'], 'fetch_failed')
            self.assertEqual(result['attempts'], 2)
            self.assertEqual(exit_status({'total':1,'pending':0,'complete':True,'results':[result]}), expected)

if __name__ == '__main__': unittest.main()
