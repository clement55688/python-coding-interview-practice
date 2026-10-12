import importlib
import unittest

apply_tags = importlib.import_module("practice.task_18_html_range_tags.starter").apply_tags


class Tests(unittest.TestCase):
    def test_nested_and_disjoint(self):
        self.assertEqual(apply_tags("ACGT", [(0, 4, "b"), (1, 3, "i")]), "<b>A<i>CG</i>T</b>")
        self.assertEqual(apply_tags("abcd", [(0, 1, "b"), (2, 4, "i")]), "<b>a</b>b<i>cd</i>")

    def test_same_boundaries(self):
        self.assertEqual(apply_tags("abc", [(0, 3, "b"), (0, 2, "i")]), "<b><i>ab</i>c</b>")
        self.assertEqual(apply_tags("abc", [(0, 3, "b"), (1, 3, "i")]), "<b>a<i>bc</i></b>")

    def test_escaping(self):
        self.assertEqual(apply_tags("a<&", [(0, 3, "code")]), "<code>a&lt;&amp;</code>")

    def test_validation(self):
        invalid = [
            [(0, 3, "b"), (2, 4, "i")],
            [(0, 0, "b")],
            [(-1, 1, "b")],
            [(0, 5, "b")],
            [(0, 1, "1bad")],
            [(0, 1, "b"), (0, 1, "b")],
        ]
        for annotations in invalid:
            with self.subTest(annotations=annotations), self.assertRaises(ValueError):
                apply_tags("abcd", annotations)


if __name__ == "__main__":
    unittest.main()

