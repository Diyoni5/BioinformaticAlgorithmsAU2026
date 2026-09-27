def hamming_distance(first: str, second: str) -> int:
    return sum(1 for a, b in zip(first, second) if a != b)


def neighbors(pattern: str, d: int) -> set[str]:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nuc in 'ACGT':
                neighborhood.add(nuc + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood