import copy
import unittest

from practice.task_21_robot_navigator.starter import run_robot


class Tests(unittest.TestCase):
    def test_turns_movement_and_path(self):
        result = run_robot(4, 4, set(), ["F", "R", "F", "F", "L", "F"])
        self.assertEqual(result, {"position": (2, 2), "heading": "N", "visited": [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]})

    def test_obstacles_and_boundaries_are_ignored(self):
        self.assertEqual(run_robot(2, 2, {(0, 1)}, ["F", "L", "F"]), {"position": (0, 0), "heading": "W", "visited": [(0, 0)]})

    def test_inputs_are_not_mutated(self):
        obstacles, commands = {(1, 0)}, ["R", "F"]
        before = (copy.deepcopy(obstacles), copy.deepcopy(commands))
        run_robot(2, 2, obstacles, commands)
        self.assertEqual((obstacles, commands), before)

    def test_validation(self):
        cases = [
            (0, 2, set(), [], (0, 0), "N"),
            (2, 2, {(2, 0)}, [], (0, 0), "N"),
            (2, 2, set(), [], (2, 0), "N"),
            (2, 2, set(), ["X"], (0, 0), "N"),
            (2, 2, set(), [], (0, 0), "Q"),
        ]
        for args in cases:
            with self.subTest(args=args), self.assertRaises(ValueError):
                run_robot(*args)


if __name__ == "__main__":
    unittest.main()
