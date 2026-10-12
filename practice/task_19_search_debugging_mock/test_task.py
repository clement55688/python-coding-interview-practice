import copy
import importlib
import unittest

SearchIndex = importlib.import_module("practice.task_19_search_debugging_mock.starter").SearchIndex

DOCS = [
    {"id": "a", "text": "Alpha protein results", "owner": "bea", "type": "note"},
    {"id": "b", "text": "Protein: alpha assay", "owner": "ada", "type": "experiment"},
    {"id": "c", "text": "ALPHA protein protocol", "owner": "ada", "type": "experiment"},
    {"id": "d", "text": "alpha only", "owner": "ada", "type": "note"},
]


class Tests(unittest.TestCase):
    def test_normalization_and_and_semantics(self):
        index = SearchIndex(DOCS)
        self.assertEqual([d["id"] for d in index.search("alpha protein")], ["a", "b", "c"])

    def test_filters_and_filter_only_query(self):
        index = SearchIndex(DOCS)
        self.assertEqual([d["id"] for d in index.search("protein owner:ada type:experiment")], ["b", "c"])
        self.assertEqual([d["id"] for d in index.search("owner:ada type:note")], ["d"])

    def test_defensive_copy_and_input_order(self):
        original = copy.deepcopy(DOCS)
        result = SearchIndex(DOCS).search("alpha")
        self.assertEqual([d["id"] for d in result], ["a", "b", "c", "d"])
        result[0]["text"] = "changed"
        self.assertEqual(DOCS, original)

    def test_validation(self):
        with self.assertRaises(ValueError): SearchIndex(DOCS + [dict(DOCS[0])])
        with self.assertRaises(ValueError): SearchIndex([{"text": "missing id"}])
        with self.assertRaises(ValueError): SearchIndex([{"id": "x", "text": "ok"}]).search("bad:filter")


if __name__ == "__main__":
    unittest.main()

