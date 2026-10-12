import unittest

from practice.task_05_debugging_counts.starter import count_statuses


class DebuggingCountsTests(unittest.TestCase):
    def test_empty_single_and_repeated_statuses(self):
        self.assertEqual(count_statuses([]), {})
        self.assertEqual(count_statuses([{"status": "received"}]), {"received": 1})
        self.assertEqual(
            count_statuses(
                [
                    {"status": "received"},
                    {"status": "processing"},
                    {"status": "received"},
                ]
            ),
            {"received": 2, "processing": 1},
        )
