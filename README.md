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

## Status

Working research paper. Empirical benchmark evaluation is identified as future
work. A version of this paper is being prepared for preprint submission.

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

Copyright © 2026 Marcos Verrell / Inappropriate Media Limited.
Licensed under CC BY-NC-ND 4.0 — see [LICENSE.md](LICENSE.md).

You may share this work with attribution. You may not use it commercially or
distribute modified versions. For commercial licensing enquiries relating to
Collapse Aware AI, contact via https://www.verrellslaw.org.
