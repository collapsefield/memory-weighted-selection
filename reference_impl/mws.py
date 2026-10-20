"""Public reference only. Not Collapse Aware AI/Crown source or runtime."""
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class Candidate:
    name: str
    base: float
    memory: float
    soft_penalty: float
    eligible: bool = True

def choose(candidates: Iterable[Candidate], memory_coefficient: float = 0.8,
           governor_coefficient: float = 1.5):
    """First-eligible order is the declared deterministic tie-break."""
    if memory_coefficient < 0 or governor_coefficient < 0:
        raise ValueError("coefficients must be nonnegative")
    eligible = [c for c in candidates if c.eligible]
    if not eligible:
        return None, {}
    scores = {c.name: c.base + memory_coefficient*c.memory
              - governor_coefficient*c.soft_penalty for c in eligible}
    return max(eligible, key=lambda c: scores[c.name]).name, scores

def threshold(candidates: Iterable[Candidate], governor_coefficient: float = 0):
    """Smallest memory coefficient for a strict score crossover from disabled winner.

    Ties at the threshold depend on declared candidate order. Returns None if
    no challenger with strictly higher memory alignment exists.
    """
    pool = [c for c in candidates if c.eligible]
    winner, _ = choose(pool, 0, governor_coefficient)
    if winner is None:
        return None
    baseline = next(c for c in pool if c.name == winner)
    base_score = baseline.base-governor_coefficient*baseline.soft_penalty
    opportunities = [(base_score-(c.base-governor_coefficient*c.soft_penalty)) /
                      (c.memory-baseline.memory) for c in pool
                      if c.memory > baseline.memory]
    return min(opportunities) if opportunities else None
