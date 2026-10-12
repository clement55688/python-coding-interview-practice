import unittest
from practice.task_14_plate_allocator.starter import allocate

class Tests(unittest.TestCase):
    def test_deterministic_allocation(self):
        self.assertEqual(allocate([{"id":"s1","replicates":2},{"id":"s2","replicates":1}],{"A1"}),{"s1":["B1","C1"],"s2":["D1"]})
    def test_rows_distinct_and_reserved(self):
        out=allocate([{"id":"x","replicates":8}],{"A1","B1"})["x"]
        self.assertEqual(len({w[0] for w in out}),8); self.assertFalse({"A1","B1"}&set(out))
    def test_validation(self):
        for samples,reserved in [([{"id":"x","replicates":9}],None),([{"id":"x","replicates":1},{"id":"x","replicates":1}],None),([], {"Z9"})]:
            with self.assertRaises(ValueError): allocate(samples,reserved)
if __name__ == "__main__": unittest.main()

