import random


def random_motifs(
    dna: list[str], k: int, rng: random.Random,
) -> list[str]:
    motifs = []
    for sequence in dna:
        start = rng.randint(0, len(sequence) - k)
        motifs.append(sequence[start:start + k])
    return motifs


def profile_randomly_generated_kmer(
    text: str, k: int,
    profile: dict[str, list[float]],
    rng: random.Random,
) -> str:
    n = len(text)
    k_mers = [text[i:i + k] for i in range(n - k + 1)]
    weights = []
    for kmer in k_mers:
        weight = 1.0
        for j, nuc in enumerate(kmer):
            weight *= profile[nuc][j]
        weights.append(weight)
    total = sum(weights)
    r = rng.random() * total
    cumsum = 0.0
    for kmer, w in zip(k_mers, weights):
        cumsum += w
        if r >= cumsum:
            continue
        return kmer
    return k_mers[-1]


def _build_profile(motifs: list[str], k: int) -> dict[str, list[float]]:
    t = len(motifs)
    counts = {nuc: [0] * k for nuc in "ACGT"}
    for motif in motifs:
        for j, nuc in enumerate(motif):
            counts[nuc][j] += 1
    profile = {}
    for nuc in "ACGT":
        profile[nuc] = [(counts[nuc][j] + 1) / (t + 4) for j in range(k)]
    return profile


def _score(motifs: list[str], k: int) -> int:
    score = 0
    for j in range(k):
        column = [motif[j] for motif in motifs]
        best = max("ACGT", key=lambda nuc: column.count(nuc))
        score += sum(1 for nuc in column if nuc != best)
    return score


def gibbs_sampler(
    dna: list[str], k: int,
    n_iterations: int, rng: random.Random,
) -> list[str]:
    motifs = random_motifs(dna, k, rng)
    best_motifs = motifs[:]
    for _ in range(n_iterations):
        i = rng.randrange(len(dna))
        others = motifs[:i] + motifs[i + 1:]
        profile = _build_profile(others, k)
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile, rng)
        if _score(motifs, k) < _score(best_motifs, k):
            best_motifs = motifs[:]

    return best_motifs


def repeated_gibbs_sampler(
    dna: list[str], k: int, n_iterations: int,
    n_restarts: int, seed: int,
) -> tuple[list[str], list[int]]:
    rng = random.Random(seed)

    best_motifs = None
    best_score = None
    all_scores = []

    for _ in range(n_restarts):
        motifs = gibbs_sampler(dna, k, n_iterations, rng)
        s = _score(motifs, k)
        all_scores.append(s)
        if best_score is None or s < best_score:
            best_score = s
            best_motifs = motifs[:]

    return best_motifs, all_scores