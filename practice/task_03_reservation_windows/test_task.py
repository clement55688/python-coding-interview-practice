import unittest

from practice.task_03_reservation_windows.starter import merge_reservations


class ReservationWindowsTests(unittest.TestCase):
    def test_merge_overlaps_and_preserve_adjacency(self):
        windows = [(8, 10), (1, 4), (3, 6), (4, 7)]
        original = list(windows)
        self.assertEqual(merge_reservations(windows), [(1, 7), (8, 10)])
        self.assertEqual(windows, original)
        self.assertEqual(merge_reservations([(4, 7), (1, 4)]), [(1, 4), (4, 7)])

    def test_empty_input(self):
        self.assertEqual(merge_reservations([]), [])
