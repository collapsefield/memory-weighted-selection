# Memory-Weighted Selection

**Middleware for continuity and retained-state behavioural selection**

Author: Marcos Ross  
Part of the Collapse Aware AI (CAAI) engineering / research programme.

**Read the paper:** [Memory-Weighted Selection (PDF)](Memory-Weighted-Selection.pdf)

---

## What this is

This repository contains the working-paper source for *Memory-Weighted Selection*, a formal reference model for how persistent retained state can influence candidate selection in model-agnostic middleware.

The core idea is that a host or generator supplies a set of permitted candidate outputs/actions, while a separate middleware layer evaluates those candidates against structured retained state and declared constraints before final selection.

Selection itself becomes the place where behavioural continuity is made operational — without requiring retraining of the underlying model.

The paper is a public formalisation. Production CAAI kernel logic, scoring functions, thresholds and runtime implementation remain proprietary.

---

## Applied engineering status — August 2026

The CAAI engineering programme has now progressed beyond the original Phase-1 foundation used when this paper was first published.

The current private engineering line includes a live-integrated retained-state selection path and a bounded **local managed-evaluation package**.

Public-safe demonstrated engineering now includes:

- retained-state selection among permitted candidates;
- persistence and deterministic replay;
- explicit retained-state revision / revocation;
- continuity memory and session boot;
- recall routing / correction / revoked-context protection;
- bounded ambiguity handling;
- agency-impact routing;
- durable private Decision Records;
- customer-safe Decision Record projection;
- live Phase-2 → Core selector integration;
- failure/replay/restart and duplicate-protection hardening;
- managed evaluation with customer-safe JSON / HTML / PDF evidence.

A controlled synthetic live comparison held the prompt, candidate set, candidate order, mapped thread and deterministic seed constant while comparing declared reference and governed retained-state conditions. The real selector chose different permitted candidates across the two conditions.

That is an **engineering implementation result**, not independent empirical proof of Verrell’s Law and not isolated causal proof of one configuration variable.

Current public-safe CAAI engineering status:

- [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack)
- [Current Engineering State — 7 August 2026](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack/blob/main/CURRENT_ENGINEERING_STATE_2026-08-07.md)
- [Managed Evaluation Evidence — 7 August 2026](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack/blob/main/MANAGED_EVALUATION_EVIDENCE_2026-08-07.md)

---

## Reference memory decomposition

The public paper uses a deliberately simplified reference decomposition:

- **Recency** — alignment with recent retained state;
- **Salience** — alignment with higher-importance retained items;
- **Anchor** — compatibility with persistent commitments / stability references.

The wider private CAAI architecture now contains richer retained-state lifecycle, recall-quality and evidence machinery than this paper’s minimal reference model.

The paper should therefore be read as a **formal public abstraction**, not as a complete specification of the current production/private runtime.

---

## Repository contents

```text
Memory-Weighted-Selection.pdf
                        — compiled paper for convenient reading

paper_source/
  paper.tex             — full LaTeX source of the working paper
  references.bib        — bibliography
  paper.bbl             — compiled bibliography
  fig_architecture.pdf  — reference architecture figure
  fig_scenario.pdf      — worked scenario figure

research_notes/
  QUANTUM_MEMORY_AND_CARBON_ADJACENT_EVIDENCE.md
                        — bounded adjacent-evidence research note,
                          deliberately separate from the engineering paper
```

---

## Building the paper

From the repository root:

```text
cd paper_source
pdflatex paper.tex
pdflatex paper.tex
pdflatex paper.tex
```

The included `paper.bbl` means no separate BibTeX run is required.

---

## Scope and claims

The paper makes a narrow engineering-level claim about middleware candidate selection.

It does **not** claim:

- consciousness or sentience;
- AGI;
- quantum implementation;
- electromagnetic memory as an established CAAI mechanism;
- new established physics;
- universal emotional / psychological inference;
- disclosure of proprietary Crown internals.

---

## Evidence and validation boundary

CAAI engineering tests establish that the middleware architecture can be built, executed, inspected, replayed and evaluated.

That is not automatically independent empirical confirmation of Verrell’s Law merely because CAAI was deliberately built around retained-state weighting.

A runtime test that reuses the selector’s own internal retained-state score is an **engineering conformance / implementation validation** unless the analysis uses an independently frozen score or another non-circular empirical route.

The research and engineering evidence labels must remain separate.

---

## Relationship to Verrell’s Law

Verrell’s Law is a separate proposed falsifiable retained-state selection framework.

CAAI can be assessed entirely as software without accepting speculative physical interpretation.

The canonical research archive is:

- [collapsefield-verrells-law](https://github.com/collapsefield/collapsefield-verrells-law)

---

## Status

**Paper status:** working public engineering paper.  
**CAAI implementation status:** live-integrated retained-state selection and local managed-evaluation packaging now exist in the private engineering line.  
**Independent empirical validation:** remains separate future research work.

The paper, CAAI engineering implementation and Verrell’s Law empirical programme should be evaluated under their separate evidence labels rather than collapsed into one claim.

---

## Citation

Until a preprint identifier is assigned, cite the working paper as:

> Ross, Marcos. “Memory-Weighted Selection: Middleware for Continuity and Governed Behaviour in LLM Systems.” Working paper, 2026.

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).

---

## Licence and authorship

Copyright © 2026 Inappropriate Media Limited.
Licensed under CC BY-NC-ND 4.0 — see [LICENSE.md](LICENSE.md).

You may share this work with attribution. You may not use it commercially or distribute modified versions except as permitted by the licence.

For CAAI commercial evaluation or licensing enquiries, see the [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack).
