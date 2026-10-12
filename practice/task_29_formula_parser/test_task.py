import unittest

from practice.task_29_formula_parser.starter import parse_formula


class Tests(unittest.TestCase):
    def test_symbols_and_group(self):
        self.assertEqual(parse_formula("A2(B3C)2"), {"A": 2, "B": 6, "C": 2})
        self.assertEqual(parse_formula("(AB)3C"), {"A": 3, "B": 3, "C": 1})

    def test_nested_groups_and_multi_digit_multiplier(self):
        self.assertEqual(parse_formula("((AB)2C)10"), {"A": 20, "B": 20, "C": 10})

    def test_repeated_symbol(self):
        self.assertEqual(parse_formula("ABA2"), {"A": 3, "B": 1})

    def test_validation(self):
        for formula in ["", "()", "A0", "2A", "A(B", "A)B", "Ab", "A-2"]:
            with self.subTest(formula=formula), self.assertRaises(ValueError): parse_formula(formula)


if __name__ == "__main__":
    unittest.main()
