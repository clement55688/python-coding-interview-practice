import unittest
from practice.task_13_experiment_scheduler.starter import schedule

class Tests(unittest.TestCase):
    def test_priority_among_ready(self):
        tasks=[{"id":"analyze","depends_on":["prep"],"priority":9},{"id":"prep","depends_on":[],"priority":1},{"id":"backup","depends_on":[],"priority":5},{"id":"report","depends_on":["analyze"],"priority":2}]
        self.assertEqual(schedule(tasks),["backup","prep","analyze","report"])
    def test_tie_and_empty(self):
        self.assertEqual(schedule([]),[])
        self.assertEqual(schedule([{"id":"b","depends_on":[],"priority":1},{"id":"a","depends_on":[],"priority":1}]),["a","b"])
    def test_errors(self):
        cases=[[{"id":"a","depends_on":["x"],"priority":1}],[{"id":"a","depends_on":["b"],"priority":1},{"id":"b","depends_on":["a"],"priority":1}]]
        for case in cases:
            with self.assertRaises(ValueError): schedule(case)
if __name__ == "__main__": unittest.main()

