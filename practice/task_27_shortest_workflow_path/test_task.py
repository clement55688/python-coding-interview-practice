import copy
import unittest

from practice.task_27_shortest_workflow_path.starter import shortest_workflow_path


class Tests(unittest.TestCase):
    def test_shortest_and_lexicographic_tie(self):
        graph = {"a": ["c", "b"], "b": ["d"], "c": ["d"], "d": []}
        self.assertEqual(shortest_workflow_path(graph, "a", "d"), ["a", "b", "d"])

    def test_unreachable_and_same_node(self):
        graph = {"a": ["b"], "b": [], "c": []}
        self.assertIsNone(shortest_workflow_path(graph, "a", "c"))
        self.assertEqual(shortest_workflow_path(graph, "a", "a"), ["a"])

    def test_cycles_and_nonmutation(self):
        graph = {"a": ["b"], "b": ["a", "c"], "c": []}
        original = copy.deepcopy(graph)
        self.assertEqual(shortest_workflow_path(graph, "a", "c"), ["a", "b", "c"])
        self.assertEqual(graph, original)

    def test_validation(self):
        cases = [
            ({"a": ["missing"]}, "a", "a"),
            ({"a": ["a", "a"]}, "a", "a"),
            ({"": []}, "", ""),
            ({"a": []}, "a", "missing"),
        ]
        for args in cases:
            with self.subTest(args=args), self.assertRaises(ValueError): shortest_workflow_path(*args)


if __name__ == "__main__":
    unittest.main()
