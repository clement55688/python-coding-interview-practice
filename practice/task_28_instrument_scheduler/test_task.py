import copy
import unittest

from practice.task_28_instrument_scheduler.starter import schedule_instrument


class Tests(unittest.TestCase):
    def test_priority_and_nonpreemption(self):
        jobs = [
            {"id": "a", "arrival": 0, "duration": 4, "priority": 1},
            {"id": "b", "arrival": 1, "duration": 2, "priority": 5},
            {"id": "c", "arrival": 1, "duration": 1, "priority": 3},
        ]
        self.assertEqual(schedule_instrument(jobs), [
            {"id": "a", "start": 0, "end": 4},
            {"id": "b", "start": 4, "end": 6},
            {"id": "c", "start": 6, "end": 7},
        ])

    def test_idle_jump_and_ties(self):
        jobs = [
            {"id": "z", "arrival": 3, "duration": 1, "priority": 2},
            {"id": "a", "arrival": 3, "duration": 2, "priority": 2},
        ]
        self.assertEqual(schedule_instrument(jobs), [
            {"id": "a", "start": 3, "end": 5},
            {"id": "z", "start": 5, "end": 6},
        ])

    def test_empty_and_nonmutation(self):
        self.assertEqual(schedule_instrument([]), [])
        jobs = [{"id": "a", "arrival": 0, "duration": 1, "priority": 1}]
        original = copy.deepcopy(jobs)
        schedule_instrument(jobs)
        self.assertEqual(jobs, original)

    def test_validation(self):
        valid = {"id": "a", "arrival": 0, "duration": 1, "priority": 1}
        cases = [[{}], [{**valid, "duration": 0}], [{**valid, "priority": True}], [valid, dict(valid)]]
        for jobs in cases:
            with self.subTest(jobs=jobs), self.assertRaises(ValueError): schedule_instrument(jobs)


if __name__ == "__main__":
    unittest.main()
