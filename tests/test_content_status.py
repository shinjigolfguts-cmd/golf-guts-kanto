import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_content_status import inventory, unresolved_inventory, LABELS


class ContentStatusTests(unittest.TestCase):
    def course(self):
        return {'id': 1, 'name': '検証施設', 'url': 'https://example.test/',
                'comparison': {key: {'text': '公式案内で設備なしを確認。'} for key in LABELS}}

    def test_partial_unknown_is_not_hidden_by_nonempty_field(self):
        course = self.course()
        course['comparison']['stay'] = {'text': '浴室あり。宿泊は未確認。詳細を確認できていません。'}
        self.assertEqual(inventory({'courses': [course]}), [])
        rows = unresolved_inventory({'courses': [course]})
        self.assertEqual([(r['id'], r['field']) for r in rows], [(1, 'stay')])

    def test_absent_service_is_not_unresolved(self):
        self.assertEqual(unresolved_inventory({'courses': [self.course()]}), [])

    def test_empty_text_and_null_are_missing(self):
        course = self.course()
        course['comparison']['play'] = None
        course['comparison']['car'] = {'text': '  '}
        self.assertEqual(inventory({'courses': [course]})[0]['fields'], ['play', 'car'])

    def test_historical_basis_does_not_mark_current_text(self):
        course = self.course()
        course['comparison']['rail']['basis'] = '以前は未確認'
        self.assertEqual(unresolved_inventory({'courses': [course]}), [])

    def test_wording_variants_and_multiple_fields(self):
        course = self.course()
        course['comparison']['rail']['text'] = '所要時間を確認できていません。'
        course['comparison']['budget']['text'] = '料金本文を取得できず。'
        self.assertEqual(len(unresolved_inventory({'courses': [course]})), 2)
