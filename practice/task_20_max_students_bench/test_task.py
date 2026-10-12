import copy
import unittest

from practice.task_20_max_students_bench.starter import max_students_on_bench


class Tests(unittest.TestCase):
    def test_groups_and_deduplicates(self):
        records = [("s1", "b1"), ("s2", "b1"), ("s1", "b1"), ("s1", "b2"), ("s3", "b2")]
        self.assertEqual(max_students_on_bench(records), 2)

    def test_empty_and_single(self):
        self.assertEqual(max_students_on_bench([]), 0)
        self.assertEqual(max_students_on_bench([("s1", "b1")]), 1)

    def test_input_is_not_mutated(self):
        records = [("s1", "b1"), ("s2", "b1")]
        original = copy.deepcopy(records)
        max_students_on_bench(records)
        self.assertEqual(records, original)

    def test_validation(self):
        for records in [[("", "b1")], [("s1", "")], [("s1",)], [["s1", "b1"]]]:
            with self.subTest(records=records), self.assertRaises(ValueError):
                max_students_on_bench(records)


if __name__ == "__main__":
    unittest.main()
