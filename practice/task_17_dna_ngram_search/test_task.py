import importlib
import unittest

DNAIndex = importlib.import_module("practice.task_17_dna_ngram_search.starter").DNAIndex


class Tests(unittest.TestCase):
    def setUp(self):
        self.index = DNAIndex({"s2": "AACCGGTT", "s1": "TTCCAACC", "s3": "AAAATTTT"}, 3)

    def test_concrete_query_and_order(self):
        self.assertEqual(self.index.search("AACCG"), ["s2"])
        self.assertEqual(self.index.search("AACC"), ["s1", "s2"])

    def test_ambiguous_character(self):
        self.assertEqual(self.index.search("AAN"), ["s1", "s2", "s3"])
        self.assertEqual(self.index.search("CCN"), ["s1", "s2"])

    def test_short_query_and_repeated_kmers(self):
        self.assertEqual(self.index.search("AA"), [])
        self.assertEqual(self.index.search("AAAA"), ["s3"])

    def test_validation(self):
        with self.assertRaises(ValueError): DNAIndex({}, 0)
        with self.assertRaises(ValueError): DNAIndex({"x": "ACNX"}, 2)
        with self.assertRaises(ValueError): self.index.search("AXC")


if __name__ == "__main__":
    unittest.main()

