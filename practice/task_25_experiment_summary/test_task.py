import copy
import unittest

from practice.task_25_experiment_summary.starter import summarize_runs


class Tests(unittest.TestCase):
    def test_latest_event_and_grouping(self):
        events = [
            {"event_id": "e1", "run_id": "r2", "sample_id": "s3", "status": "queued", "timestamp": 1},
            {"event_id": "e2", "run_id": "r1", "sample_id": "s2", "status": "failed", "timestamp": 3},
            {"event_id": "e3", "run_id": "r1", "sample_id": "s1", "status": "running", "timestamp": 1},
            {"event_id": "e4", "run_id": "r1", "sample_id": "s1", "status": "complete", "timestamp": 2},
        ]
        self.assertEqual(summarize_runs(events), [
            {"run_id": "r1", "sample_ids": ["s1", "s2"], "status_counts": {"complete": 1, "failed": 1}},
            {"run_id": "r2", "sample_ids": ["s3"], "status_counts": {"queued": 1}},
        ])

    def test_duplicate_event_and_timestamp_tie(self):
        events = [
            {"event_id": "e1", "run_id": "r", "sample_id": "s", "status": "old", "timestamp": 2},
            {"event_id": "e1", "run_id": "r", "sample_id": "other", "status": "ignored", "timestamp": 9},
            {"event_id": "e2", "run_id": "r", "sample_id": "s", "status": "new", "timestamp": 2},
        ]
        self.assertEqual(summarize_runs(events)[0]["status_counts"], {"new": 1})

    def test_empty_and_nonmutation(self):
        self.assertEqual(summarize_runs([]), [])
        events = [{"event_id": "e", "run_id": "r", "sample_id": "s", "status": "ok", "timestamp": 0}]
        original = copy.deepcopy(events)
        summarize_runs(events)
        self.assertEqual(events, original)

    def test_validation(self):
        valid = {"event_id": "e", "run_id": "r", "sample_id": "s", "status": "ok", "timestamp": 1}
        cases = [
            {},
            {**valid, "event_id": ""},
            {**valid, "timestamp": True},
            {**valid, "status": 1},
        ]
        for events in cases:
            with self.subTest(event=events), self.assertRaises(ValueError): summarize_runs([events])


if __name__ == "__main__":
    unittest.main()
