# 02 — DNA n-gram search

Implement `DNAIndex(sequences, k)` and `search(query)`.

`sequences` maps unique IDs to DNA strings containing only `A`, `C`, `G`, and `T`. Build an inverted index from every length-`k` substring to the IDs containing it.

Search rules:

- A concrete query contains only `A/C/G/T`; return IDs whose sequence contains every query k-mer.
- `N` in a query matches any one nucleotide. Expand ambiguous k-mers logically, without changing stored sequences.
- Return IDs in lexicographic order.
- A query shorter than `k` returns an empty list.
- Raise `ValueError` for `k <= 0`, invalid stored sequences, or invalid query characters.

After the baseline, discuss how expansion grows with multiple `N` characters and propose a safer production approach.
