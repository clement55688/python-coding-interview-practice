import unittest

from practice.task_22_elevator_controller.starter import ElevatorController


class Tests(unittest.TestCase):
    def test_idle_choice_and_duplicate_requests(self):
        elevator = ElevatorController(8)
        elevator.request(4); elevator.request(2); elevator.request(2)
        self.assertEqual(elevator.step(), {"floor": 1, "direction": "UP", "pending": [2, 4]})
        self.assertEqual(elevator.step(), {"floor": 2, "direction": "UP", "pending": [4]})

    def test_continues_then_reverses(self):
        elevator = ElevatorController(8)
        elevator.request(3)
        elevator.step()
        elevator.request(0)
        self.assertEqual(elevator.step()["floor"], 2)
        self.assertEqual(elevator.step(), {"floor": 3, "direction": "DOWN", "pending": [0]})
        self.assertEqual(elevator.step()["floor"], 2)

    def test_current_floor_and_snapshot_copy(self):
        elevator = ElevatorController(3)
        elevator.request(0)
        snap = elevator.step()
        self.assertEqual(snap, {"floor": 0, "direction": "IDLE", "pending": []})
        snap["pending"].append(2)
        self.assertEqual(elevator.snapshot()["pending"], [])

    def test_validation(self):
        for count in [0, -1, True]:
            with self.subTest(count=count), self.assertRaises(ValueError): ElevatorController(count)
        elevator = ElevatorController(3)
        for floor in [-1, 3, True]:
            with self.subTest(floor=floor), self.assertRaises(ValueError): elevator.request(floor)


if __name__ == "__main__":
    unittest.main()
