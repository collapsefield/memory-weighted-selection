# Memory-Weighted Selection

**Middleware for Continuity and Governed Behaviour in LLM Systems**

Author: Marcos Verrell (Independent Researcher)
Part of the Collapse Aware AI (CAAI) research programme — Verrell's Law framework.

**Read the paper:** [Memory-Weighted Selection (PDF)](Memory-Weighted-Selection.pdf)

---

## What this is

This repository contains the working paper source for *Memory-Weighted
Selection*, a formal reference model for how persistent memory state can bias
candidate selection in LLM-based systems.

The core idea: instead of relying only on direct base-model emission,
retrieval-conditioned generation, or post-hoc moderation, a middleware layer
scores fully formed candidate outputs against a structured persistent memory
state and explicit governor constraints, and selects among them. Selection
itself becomes the primary site of continuity and governance enforcement — no
modification of the base model required.

The reference formulation decomposes persistent memory into three components:

- **Recency** — alignment with recent selections
- **Salience** — alignment with high-importance memory items
- **Anchor** — compatibility with persistent commitments and stability constraints

In the wider CAAI architecture, this layered memory-influence structure is
described as **Weighted Emergence Layering (WEL)**, and the influence of
retained prior information on future selection probability as **Active
Information Weight (AIW)**. The paper presents the general, model-agnostic
reference mechanism; production kernel logic, scoring functions, thresholds,
and implementation details are deliberately out of scope and remain
proprietary.

## Repository contents

```
Memory-Weighted-Selection.pdf
                        — compiled paper for convenient reading

paper_source/
  paper.tex             — full LaTeX source of the working paper
  references.bib        — bibliography
  paper.bbl             — compiled bibliography (for reproducible builds)
  fig_architecture.pdf  — reference architecture figure
  fig_scenario.pdf      — worked scenario figure

research_notes/
  QUANTUM_MEMORY_AND_CARBON_ADJACENT_EVIDENCE.md
                        — bounded adjacent-evidence note on the 2026
                          bilayer-graphene non-Abelian anyon result and its
                          relevance to history-dependent, distributed
                          information. Kept deliberately separate from the
                          paper; see the note's claim-boundary section.
```

## Building the paper

From the repository root:

```
cd paper_source
pdflatex paper.tex
pdflatex paper.tex
pdflatex paper.tex
```

The included `paper.bbl` means no separate BibTeX run is required. Three runs
ensure that citations, references, and PDF bookmarks are fully resolved.

## Scope and claims

The paper makes a narrow, engineering-level claim about middleware candidate
selection. It does not claim consciousness, sentience, agency, quantum
mechanisms, or physical-theoretic validation, and the adjacent-evidence note
in `research_notes/` states its own claim boundaries explicitly.

## Evidence and validation boundary

Collapse Aware AI now has a demonstrated Phase-1 engineering foundation for governed retained-state selection. That implementation evidence is relevant to whether the middleware architecture can be built, inspected, replayed and evaluated.

It is **not automatically independent empirical confirmation of Verrell's Law** merely because the software was deliberately built to apply retained-state weighting.

The canonical Verrell's Law archive now distinguishes three evidence classes:

```text
Independent empirical test
Engineering conformance test
Proxy-based empirical test
```

A runtime test that reuses the selector's own internal retained-state score is an engineering conformance / implementation validation unless the analysis uses an independently frozen score or another non-circular empirical route.

See:

- [Verrell's Law — Empirical Identification Clarification v1.0](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Verrell's Law — Mathematical Foundations and Falsification Protocol v1.0](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

## Relationship to the exploratory software-frequency programme

The separate Verrell's Law archive also contains an exploratory programme asking whether controlled software timing / drive-rate conditions add reproducible information about retained-state coupling or persistence.

That work is:

- non-canonical;
- unvalidated;
- not required for this paper or for CAAI's engineering value;
- not evidence for electromagnetic or physical resonance;
- currently at the runtime-characterization / preregistration stage rather than the evidence stage.

The experimental-control methods developed there — frozen-state comparisons, per-trial restore, read-only or fixed probes, aliasing/phase controls, nested held-out validation, power analysis and preregistered stopping rules — are nevertheless useful for strengthening future CAAI validation.

Current exploratory control note:

- [Frequency-Coupled Retained-State Extension v0.5](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/research_notes/FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.5_PREREGISTRATION_AND_MECHANISM_BOUNDARY.md)

## Status

Working research paper. Empirical benchmark evaluation and stronger independent validation remain future work. The engineering implementation track and the broader Verrell's Law empirical programme should be evaluated under their separate evidence labels rather than collapsed into one claim.

## Citation

Until a preprint identifier is assigned, cite the working paper as:

> Verrell, Marcos. “Memory-Weighted Selection: Middleware for Continuity and
> Governed Behaviour in LLM Systems.” Working paper, 2026.

Machine-readable citation metadata is provided in
[`CITATION.cff`](CITATION.cff). The record will be updated when an arXiv or DOI
identifier becomes available.

## Related

- Verrell's Law — theoretical framework: https://www.verrellslaw.org
- Collapse Aware AI (CAAI) — the applied middleware programme built on this
  mechanism.

## Licence and authorship

Copyright © 2026 Inappropriate Media Limited.
Licensed under CC BY-NC-ND 4.0 — see [LICENSE.md](LICENSE.md).

You may share this work with attribution. You may not use it commercially or
distribute modified versions. For commercial licensing enquiries relating to
Collapse Aware AI, contact via https://www.verrellslaw.org.
