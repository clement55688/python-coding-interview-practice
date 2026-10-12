import unittest

from practice.task_01_latest_status.starter import latest_status


class LatestStatusTests(unittest.TestCase):
    def test_latest_status_and_later_tie_wins(self):
        events = [
            {"sample_id": "A", "timestamp": 10, "status": "received"},
            {"sample_id": "B", "timestamp": 8, "status": "processing"},
            {"sample_id": "A", "timestamp": 7, "status": "queued"},
            {"sample_id": "A", "timestamp": 10, "status": "processing"},
        ]
        self.assertEqual(
            latest_status(events),
            {"A": (10, "processing"), "B": (8, "processing")},
        )

    def test_empty_and_older_event(self):
        self.assertEqual(latest_status([]), {})
        events = [
            {"sample_id": "A", "timestamp": 10, "status": "latest"},
            {"sample_id": "A", "timestamp": 9, "status": "older"},
        ]
        self.assertEqual(latest_status(events), {"A": (10, "latest")})
