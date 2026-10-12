# 29 — Parse a grouped assay formula

Implement `parse_formula(formula)`.

The grammar contains:

- one-letter uppercase symbols `A`–`Z`;
- parentheses for nested groups;
- optional positive integer multipliers after a symbol or closing parenthesis.

Examples:

```python
parse_formula("A2(B3C)2") == {"A": 2, "B": 6, "C": 2}
parse_formula("(AB)3C") == {"A": 3, "B": 3, "C": 1}
```

- Return keys in lexicographic insertion order.
- Reject empty formulas, unbalanced/empty groups, lowercase characters, zero multipliers, leading numbers, and unexpected characters.
- Target O(n) parsing time aside from sorting the distinct result keys.

Explain what each stack frame represents and when counts are multiplied and merged.

Follow-up: allow multi-letter symbols such as `Na` while keeping tokenization unambiguous.
