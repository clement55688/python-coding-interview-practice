import copy
import unittest

from practice.task_30_vending_machine.starter import VendingMachine


class Tests(unittest.TestCase):
    def test_purchase_and_change(self):
        machine = VendingMachine({"A": {"price": 65, "stock": 2}})
        machine.insert_coin(100)
        self.assertEqual(machine.select("A"), {"code": "A", "change": [25, 10]})
        self.assertEqual(machine.snapshot()["catalog"]["A"]["stock"], 1)
        self.assertEqual(machine.snapshot()["balance"], 0)

    def test_failed_selection_keeps_balance(self):
        machine = VendingMachine({"A": {"price": 25, "stock": 1}})
        machine.insert_coin(10)
        with self.assertRaises(ValueError): machine.select("A")
        self.assertEqual(machine.snapshot()["balance"], 10)

    def test_refund_and_snapshot_copy(self):
        catalog = {"A": {"price": 15, "stock": 1}}
        original = copy.deepcopy(catalog)
        machine = VendingMachine(catalog)
        machine.insert_coin(25); machine.insert_coin(10)
        self.assertEqual(machine.refund(), [25, 10])
        snap = machine.snapshot(); snap["catalog"]["A"]["stock"] = 0
        self.assertEqual(machine.snapshot()["catalog"]["A"]["stock"], 1)
        self.assertEqual(catalog, original)

    def test_validation_and_stock(self):
        for catalog in [{}, {"": {"price": 5, "stock": 1}}, {"A": {"price": 6, "stock": 1}}, {"A": {"price": 5, "stock": -1}}]:
            with self.subTest(catalog=catalog), self.assertRaises(ValueError): VendingMachine(catalog)
        machine = VendingMachine({"A": {"price": 5, "stock": 0}})
        with self.assertRaises(ValueError): machine.insert_coin(7)
        with self.assertRaises(ValueError): machine.select("A")


if __name__ == "__main__":
    unittest.main()
