# Memory-Weighted Selection

**Middleware for continuity and governed retained-state behavioural selection**

Part of the Collapse Aware AI (CAAI) engineering / research programme.

**Read the paper:** [Memory-Weighted Selection (PDF)](Memory-Weighted-Selection.pdf)

---

## What this is

This repository contains the working-paper source for *Memory-Weighted Selection*, a formal public reference model for how persistent retained state can influence candidate selection in model-agnostic middleware.

The core idea is that a host or generator supplies a set of permitted candidate outputs/actions, while a separate middleware layer evaluates those candidates against structured retained state and declared constraints before final selection.

Selection itself becomes the place where behavioural continuity is made operational — without requiring retraining of the underlying model.

> **Retained history is eligible evidence, not automatic authority.**

The paper is a public formalisation. Production CAAI kernel logic, scoring functions, private thresholds, tuning and runtime implementation remain proprietary.

---

## Applied engineering status — 27 August 2026

The CAAI engineering programme has progressed substantially beyond the original reference model used when this paper was first published.

### Core Gold Build

The frozen commercial selector foundation now has a public-safe accepted lineage covering:

- selection among host-supplied permitted candidates;
- reference and governed retained-state conditions;
- persistence / restart recall;
- deterministic replay in tested conditions;
- retained-state revision / revocation;
- durable Decision Records and customer-safe evidence in the integrated evaluation line;
- managed evaluation and evidence export.

### Evolution 2

The richer continuity engineering branch now includes accepted checkpoints for:

- structured ContinuityFrame interpretation;
- bounded hybrid retained-state retrieval;
- Open Loops / Reopen Semantics;
- Interaction Fit;
- suppression and bounded proactive controls;
- Confidence / Clarification;
- Contradiction / Change Surfacing;
- record-only Outcomes;
- Agent Self-History;
- bounded turn-local behavioural signals;
- Session Observation foundation;
- Engineering Tuning;
- a restart-safe local Engineer Model with microphone speech-to-text input.

Evolution 2 remains an **Engineering build rather than a finished Production release**.

Current public-safe CAAI engineering status:

- [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack)
- [CAAI Public Overview 2026](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack/blob/main/CAAI_PUBLIC_OVERVIEW_2026.md)
- [Current Engineering State — 27 August 2026](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack/blob/main/CURRENT_ENGINEERING_STATE_2026-08-27.md)

---

## Why the clean reference matters

A central CAAI principle is that retained history must not win simply because it exists.

A clean current-task/reference behaviour remains available to compete with history-conditioned alternatives.

That makes the selection question more useful than ordinary memory retrieval alone:

> **Did history actually earn the right to change the behaviour?**

This is particularly relevant to long-running agents, simulations and game/NPC systems where stale or over-dominant memory can be as damaging as forgetting.

---

## Reference memory decomposition

The public paper uses a deliberately simplified reference decomposition:

- **Recency** — alignment with recent retained state;
- **Salience** — alignment with higher-importance retained items;
- **Anchor** — compatibility with persistent commitments / stability references.

The wider private CAAI architecture now contains richer retained-state lifecycle, retrieval, confidence, change, suppression and evidence machinery than this paper’s minimal reference model.

The paper should therefore be read as a **formal public abstraction**, not as a complete specification of the current private runtime.

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
- universal hallucination prevention;
- disclosure of proprietary Crown internals.

---

## Evidence and validation boundary

CAAI engineering tests establish that the middleware architecture can be built, executed, inspected, replayed and evaluated in bounded conditions.

That is not automatically independent empirical confirmation of Verrell’s Law merely because CAAI was deliberately built around retained-state selection.

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
**Core Gold status:** frozen commercial selector foundation.  
**Evolution 2 status:** richer engineering programme, not yet a finished Production release.  
**Independent empirical validation:** separate research track.

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
