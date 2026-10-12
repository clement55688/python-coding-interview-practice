import unittest
from practice.task_07_traffic_controller.starter import TrafficController

class Tests(unittest.TestCase):
    def test_normal_cycle_and_snapshot_copy(self):
        c = TrafficController()
        self.assertEqual(c.handle("timer")["color"], "GREEN")
        self.assertEqual(c.handle("timer")["color"], "YELLOW")
        self.assertEqual(c.handle("timer")["color"], "RED")
        snap = c.snapshot(); snap["color"] = "BROKEN"
        self.assertEqual(c.snapshot()["color"], "RED")

    def test_pedestrian_and_emergency(self):
        c = TrafficController(); c.handle("timer"); c.handle("pedestrian")
        self.assertTrue(c.snapshot()["pedestrian_pending"])
        c.handle("emergency"); c.handle("timer")
        self.assertEqual(c.snapshot()["color"], "RED")
        self.assertTrue(c.snapshot()["pedestrian_pending"])
        c.handle("clear"); c.handle("timer"); c.handle("timer")
        self.assertEqual(c.snapshot()["served_pedestrians"], 1)

    def test_invalid_events(self):
        c = TrafficController()
        with self.assertRaises(ValueError): c.handle("clear")
        with self.assertRaises(ValueError): c.handle("dance")

if __name__ == "__main__": unittest.main()

