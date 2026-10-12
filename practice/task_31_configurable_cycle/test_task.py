import unittest

from practice.task_31_configurable_cycle.starter import PhaseCycle


class Tests(unittest.TestCase):
    def test_ticks_and_boundaries(self):
        cycle = PhaseCycle([("GREEN", 3), ("YELLOW", 1), ("RED", 2)])
        self.assertEqual(cycle.tick(2)["phase"], "GREEN")
        self.assertEqual(cycle.tick()["phase"], "YELLOW")
        self.assertEqual(cycle.tick()["phase"], "RED")

    def test_large_tick_count(self):
        cycle = PhaseCycle([("A", 2), ("B", 3)])
        self.assertEqual(cycle.tick(12), {"phase": "B", "elapsed": 0, "remaining": 3, "phases": [("A", 2), ("B", 3)]})

    def test_duration_update_carries_elapsed(self):
        cycle = PhaseCycle([("A", 5), ("B", 2), ("C", 3)])
        cycle.tick(4)
        self.assertEqual(cycle.update_duration("A", 2)["phase"], "C")
        self.assertEqual(cycle.snapshot()["elapsed"], 0)

    def test_validation_and_copy(self):
        for phases in [[], [("", 1)], [("A", 0)], [("A", 1), ("A", 2)], [("A", True)]]:
            with self.subTest(phases=phases), self.assertRaises(ValueError): PhaseCycle(phases)
        cycle = PhaseCycle([("A", 1)])
        with self.assertRaises(ValueError): cycle.tick(0)
        with self.assertRaises(ValueError): cycle.update_duration("missing", 2)
        snap = cycle.snapshot(); snap["phases"].append(("B", 2))
        self.assertEqual(cycle.snapshot()["phases"], [("A", 1)])


if __name__ == "__main__":
    unittest.main()
