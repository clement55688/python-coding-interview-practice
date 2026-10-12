def longest_gene_chains(segments):
    segments_by_gene = {}

    for segment in segments:
        if not isinstance(segment, (tuple, list)) or len(segment) != 3:
            raise ValueError("Each segment must contain a gene, strat, and end.")
        
        gene, start, end = segment
        if (
            not isinstance(gene, str)
            or not gene
            or not isinstance(start, int)
            or isinstance(start, bool)
            or not isinstance(end, int)
            or isinstance(end, bool)
            or start > end
        ):
            raise ValueError("Segment values are invalid.")
        
        segments_by_gene.setdefault(gene, []).append((start, end))
    
    res = []
    
    for gene, intervals in segments_by_gene.items():
        intervals.sort()
        best_chain = None
        chain_start, chain_end = intervals[0]
        piece_count = 1

        for start, end in intervals[1:]:
            if start <= chain_end + 1:
                chain_end = max(end, chain_end)
                piece_count += 1
            else:
                candidate = (gene, chain_start, chain_end, piece_count)
                if best_chain is None or _chain_key(candidate) < _chain_key(best_chain):
                    best_chain = candidate
                chain_start, chain_end = start, end
                piece_count = 1

        candidate = (gene, chain_start, chain_end, piece_count)
        if best_chain is None or _chain_key(candidate) < _chain_key(best_chain):
            best_chain = candidate
        res.append(best_chain)

    return sorted(res)

def _chain_key(chain):
    _, start, end, _ = chain
    return (-(end - start + 1), start, end)
