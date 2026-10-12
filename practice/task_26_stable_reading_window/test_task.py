import copy
import unittest

from practice.task_26_stable_reading_window.starter import longest_stable_window


class Tests(unittest.TestCase):
    def test_longest_window(self):
        self.assertEqual(longest_stable_window([8, 2, 4, 7], 4), (1, 3))
        self.assertEqual(longest_stable_window([10, 1, 2, 4, 7, 2], 5), (2, 6))

    def test_tie_prefers_earliest(self):
        self.assertEqual(longest_stable_window([1, 2, 10, 11], 1), (0, 2))

    def test_empty_single_and_nonmutation(self):
        self.assertEqual(longest_stable_window([], 0), (0, 0))
        readings = [3]
        original = copy.deepcopy(readings)
        self.assertEqual(longest_stable_window(readings, 0), (0, 1))
        self.assertEqual(readings, original)

    def test_validation(self):
        for readings, spread in [([1, True], 1), ([1, "2"], 1), ([1], -1), ([1], True)]:
            with self.subTest(readings=readings, spread=spread), self.assertRaises(ValueError):
                longest_stable_window(readings, spread)


if __name__ == "__main__":
    unittest.main()
