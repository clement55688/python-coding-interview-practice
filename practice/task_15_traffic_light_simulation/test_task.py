import unittest

from practice.task_15_traffic_light_simulation.starter import simulate_traffic


class Tests(unittest.TestCase):
    def test_partial_cycle_and_tick_boundaries(self):
        timings = {
            "EW": {"green": 2, "yellow": 1, "red": 1},
            "NS": {"green": 1, "yellow": 1, "red": 1},
        }
        original = {
            direction: durations.copy()
            for direction, durations in timings.items()
        }
        self.assertEqual(
            simulate_traffic(timings, 5),
            [
                ("GREEN", "RED"),
                ("GREEN", "RED"),
                ("YELLOW", "RED"),
                ("RED", "RED"),
                ("RED", "GREEN"),
            ],
        )
        self.assertEqual(timings, original)

    def test_full_cycle_repeats_and_zero_ticks(self):
        timings = {
            "EW": {"green": 1, "yellow": 1, "red": 1},
            "NS": {"green": 1, "yellow": 1, "red": 1},
        }
        one_cycle = [
            ("GREEN", "RED"),
            ("YELLOW", "RED"),
            ("RED", "RED"),
            ("RED", "GREEN"),
            ("RED", "YELLOW"),
            ("RED", "RED"),
        ]
        self.assertEqual(simulate_traffic(timings, 0), [])
        self.assertEqual(simulate_traffic(timings, 6), one_cycle)
        self.assertEqual(simulate_traffic(timings, 7), one_cycle + [("GREEN", "RED")])

    def test_invalid_tick_count(self):
        timings = {
            "EW": {"green": 1, "yellow": 1, "red": 1},
            "NS": {"green": 1, "yellow": 1, "red": 1},
        }
        for ticks in (-1, 1.5, True):
            with self.subTest(ticks=ticks), self.assertRaises(ValueError):
                simulate_traffic(timings, ticks)

    def test_invalid_timings(self):
        valid = {
            "EW": {"green": 1, "yellow": 1, "red": 1},
            "NS": {"green": 1, "yellow": 1, "red": 1},
        }
        invalid = [
            {"EW": valid["EW"], "NS": valid["NS"], "X": valid["EW"]},
            {"EW": valid["EW"]},
            {"EW": {"green": 1, "yellow": 1}, "NS": valid["NS"]},
            {"EW": {"green": 1, "yellow": 1, "red": 1, "blue": 1}, "NS": valid["NS"]},
            {"EW": {"green": 0, "yellow": 1, "red": 1}, "NS": valid["NS"]},
            {"EW": {"green": True, "yellow": 1, "red": 1}, "NS": valid["NS"]},
        ]
        for timings in invalid:
            with self.subTest(timings=timings), self.assertRaises(ValueError):
                simulate_traffic(timings, 1)


if __name__ == "__main__":
    unittest.main()
