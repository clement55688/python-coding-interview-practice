import unittest
from practice.task_08_gene_chains.starter import longest_gene_chains

class Tests(unittest.TestCase):
    def test_merge_and_choose(self):
        data = [("B", 8, 9), ("A", 5, 7), ("A", 1, 2), ("A", 3, 4), ("B", 1, 2)]
        original = list(data)
        self.assertEqual(longest_gene_chains(data), [("A",1,7,3),("B",1,2,1)])
        self.assertEqual(data, original)
    def test_overlap_and_tie(self):
        self.assertEqual(longest_gene_chains([("G",10,12),("G",11,15),("G",1,6)]), [("G",1,6,1)])
    def test_empty_and_invalid(self):
        self.assertEqual(longest_gene_chains([]), [])
        for bad in [[("",1,2)], [("A",3,2)], [("A",True,2)], [("A",1)]]:
            with self.assertRaises(ValueError): longest_gene_chains(bad)
if __name__ == "__main__": unittest.main()

