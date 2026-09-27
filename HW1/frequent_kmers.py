from reverse_complement import reverse_complement
from neighbors import neighbors, hamming_distance


def frequent_words_with_mismatches_and_reverse_complements(
    text: str, k: int, d: int
) -> set[str]:

    counts = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        for neighbor in neighbors(pattern, d):
            counts[neighbor] = counts.get(neighbor, 0) + 1
            rc = reverse_complement(neighbor)
            counts[rc] = counts.get(rc, 0) + 1

    max_count = max(counts.values())
    return {p for p, c in counts.items() if c == max_count}