# 03 — Encode nested text ranges

Implement `apply_tags(text, annotations)`.

Each annotation is `(start, end, tag)` using half-open indexes `[start, end)`. Return text with HTML tags inserted.

```python
apply_tags("ACGT", [(0, 4, "b"), (1, 3, "i")])
# "<b>A<i>CG</i>T</b>"
```

Requirements:

- Ranges may be disjoint or nested.
- Ranges that cross, such as `[0, 3)` and `[2, 4)`, are invalid because they cannot produce well-nested HTML; raise `ValueError`.
- At the same start index, open the longer range first.
- At the same end index, close the shorter/inner range first.
- Escape `&`, `<`, and `>` in the input text.
- Accept only tag names made of ASCII letters and digits, starting with a letter.
- Reject empty/out-of-bounds ranges and duplicate annotations.

Explain event ordering and complexity.
