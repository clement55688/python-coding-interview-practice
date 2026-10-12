import unittest
from practice.task_09_expiring_lru.starter import ExpiringLRUCache

class Tests(unittest.TestCase):
    def test_lru_and_replacement(self):
        c=ExpiringLRUCache(2); c.put("a",1,10,0); c.put("b",2,10,1)
        self.assertEqual(c.get("a",2),1); c.put("c",3,10,3)
        self.assertIsNone(c.get("b",4)); self.assertEqual(c.keys(4),["a","c"])
        c.put("a",9,10,5); self.assertEqual(c.keys(5),["c","a"])
    def test_expiry_and_capacity(self):
        c=ExpiringLRUCache(1); c.put("a",1,2,0); self.assertIsNone(c.get("a",2))
        c.put("b",2,1,3); c.put("c",3,2,4); self.assertEqual(c.keys(4),["c"])
    def test_validation_and_delete(self):
        with self.assertRaises(ValueError): ExpiringLRUCache(0)
        c=ExpiringLRUCache(1)
        with self.assertRaises(ValueError): c.put("x",1,0,0)
        c.put("x",1,1,1)
        with self.assertRaises(ValueError): c.get("x",0)
        self.assertTrue(c.delete("x")); self.assertFalse(c.delete("x"))
if __name__ == "__main__": unittest.main()

