import unittest

from practice.task_02_usage_totals.starter import usage_totals


class UsageTotalsTests(unittest.TestCase):
    def test_example(self):
        records = [
            {"record_id": "r1", "reagent": "buffer", "quantity": 3},
            {"record_id": "r2", "reagent": "buffer", "quantity": 4},
            {"record_id": "r1", "reagent": "enzyme", "quantity": 90},
        ]
        self.assertEqual(usage_totals(records), {"buffer": 7})

    def test_empty_and_conflicting_duplicate(self):
        self.assertEqual(usage_totals([]), {})
        records = [
            {"record_id": "x", "reagent": "salt", "quantity": 2},
            {"record_id": "y", "reagent": "salt", "quantity": 0},
            {"record_id": "x", "reagent": "salt", "quantity": 50},
        ]
        self.assertEqual(usage_totals(records), {"salt": 2})
