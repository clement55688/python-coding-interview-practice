import unittest

from practice.task_06_shared_instrument_time.starter import earliest_shared_start


class SharedInstrumentTimeTests(unittest.TestCase):
    def test_earliest_fit_and_exact_fit(self):
        first = [(1, 5), (8, 14)]
        second = [(2, 4), (9, 12)]
        self.assertEqual(earliest_shared_start(first, second, 3), 9)
        self.assertEqual(earliest_shared_start([(1, 5)], [(2, 5)], 3), 2)

    def test_touching_boundaries_and_empty_input(self):
        self.assertIsNone(earliest_shared_start([(1, 3)], [(3, 6)], 1))
        self.assertEqual(earliest_shared_start([(1, 3), (3, 5)], [(1, 5)], 4), 1)
        self.assertIsNone(earliest_shared_start([], [(1, 5)], 1))

    def test_inputs_are_not_modified(self):
        first = [(1, 5), (8, 14)]
        second = [(2, 4), (9, 12)]
        first_original = list(first)
        second_original = list(second)
        earliest_shared_start(first, second, 3)
        self.assertEqual(first, first_original)
        self.assertEqual(second, second_original)
