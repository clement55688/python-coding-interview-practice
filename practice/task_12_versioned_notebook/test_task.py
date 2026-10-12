import unittest
from practice.task_12_versioned_notebook.starter import NotebookStore

class Tests(unittest.TestCase):
    def test_versions_and_revert(self):
        s=NotebookStore(); self.assertEqual(s.create("e",{"status":"draft","tags":["a"]}),1)
        self.assertEqual(s.update("e",{"status":"done"}),2); self.assertEqual(s.get("e",1)["status"],"draft")
        self.assertEqual(s.revert("e",1),3); self.assertEqual(s.get("e")["status"],"draft"); self.assertEqual(s.history("e"),[1,2,3])
    def test_defensive_copy(self):
        s=NotebookStore(); data={"nested":{"x":1}}; s.create("e",data); data["nested"]["x"]=9
        got=s.get("e"); got["nested"]["x"]=7; self.assertEqual(s.get("e")["nested"]["x"],1)
    def test_errors(self):
        s=NotebookStore()
        with self.assertRaises(ValueError): s.create("",{})
        with self.assertRaises(KeyError): s.get("missing")
if __name__ == "__main__": unittest.main()

