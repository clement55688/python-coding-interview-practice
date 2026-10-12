import unittest
from practice.task_11_search_repair.starter import SearchIndex

DOCS=[{"id":"b","title":"Protein Run","body":"alpha beta","type":"experiment","owner":"Ada"},{"id":"a","title":"Alpha Notes","body":"protein","type":"note","owner":"Ben"},{"id":"c","title":"Control","body":"alpha protein","type":"experiment","owner":"Ada"}]
class Tests(unittest.TestCase):
    def test_and_semantics_and_input_order(self):
        s=SearchIndex(DOCS); self.assertEqual(s.search("alpha protein"),["b","a","c"])
    def test_filters(self):
        s=SearchIndex(DOCS); self.assertEqual(s.search("protein type:experiment owner:ada"),["b","c"])
        self.assertEqual(s.search("   "),["b","a","c"])
        with self.assertRaises(ValueError): s.search("color:red")
    def test_validation_and_copy(self):
        with self.assertRaises(ValueError): SearchIndex(DOCS+[dict(DOCS[0])])
        source=[dict(DOCS[0])]; s=SearchIndex(source); source[0]["title"]="changed"
        self.assertEqual(s.search("protein"),["b"])
if __name__ == "__main__": unittest.main()

