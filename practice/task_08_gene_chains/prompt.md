# Module 08: Longest contiguous gene chain

Original practice exercise; not an actual Benchling interview question.

`longest_gene_chains(segments)` receives `(gene, start, end)` tuples with inclusive coordinates. Validate non-empty gene names, integer coordinates (booleans are not valid coordinates), and `start <= end`.

For each gene, merge intervals that overlap or touch (`next_start <= current_end + 1`). Return that gene's longest merged chain as `(gene, start, end, piece_count)`. Length is `end - start + 1`; break equal-length ties by earlier start, then earlier end. Sort results by gene name. Empty input returns `[]`.

Do not mutate the input. State your complexity before coding.
