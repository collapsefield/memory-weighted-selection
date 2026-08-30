# Memory-Weighted Selection

**Public engineering working paper for retained-state candidate selection**  
**Part of the Collapse Aware AI™ (CAAI) engineering/research programme**

**Read the paper:** [Memory-Weighted Selection (PDF)](Memory-Weighted-Selection.pdf)

---

## What This Is

This repository contains the working-paper source for *Memory-Weighted Selection*, a public reference formulation for how persistent retained state can influence candidate selection in model-agnostic middleware.

The host or generator supplies a set of permitted candidate outputs/actions. A separate middleware layer can evaluate those candidates against structured retained state and declared constraints before final selection.

> **Retained history is eligible evidence, not automatic authority.**

The paper is a public formalisation. Production CAAI kernel logic, private scoring functions, exact thresholds, tuning and runtime implementation remain proprietary.

---

## Retained-State Selection — Category Relationship

The current technical process/category language is **Retained-State Selection**:

> **Retained-State Selection is the controlled study or process by which information preserved from prior states is permitted to influence selection among presently available candidate outcomes.**

The general concept of retained state is not claimed as original. The narrower emphasis is candidate-relative influence at selection time together with measurement, ablation and — in engineered systems — governance.

Public references:

- [Retained-State Selection Category and Terminology Note v1.0](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_CATEGORY_NOTE_v1.0.md)
- [Retained-State Selection Benchmark v0.1](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md)
- [Current Verrell’s Law / CAAI Boundary — 30 August 2026](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/00_CURRENT_POSITION_2026-08-30.md)

---

## Relationship to Collapse Aware AI™

Canonical commercial position:

> **Collapse Aware AI™ is retained-state middleware for governed selection: the host supplies permitted candidate actions, retained history may influence which candidate wins, and final selection remains bounded, inspectable and replayable in tested conditions.**

CAAI uses **Governed Retained-State Selection** as its engineering approach: retained history may influence selection but does not receive automatic authority.

Current commercial/evaluation source:

- [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack)
- [CAAI Commercial / Evaluation Index](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack/blob/main/00_RETAINED_STATE_SELECTION_COMMERCIAL_INDEX.md)

---

## Applied Engineering Status

### Core Gold

Core Gold is the frozen current commercial selector foundation.

Public-safe accepted capabilities in the integrated lineage include:

- selection among host-supplied permitted candidate actions;
- reference and governed retained-state conditions;
- persistence / restart recall;
- deterministic replay in tested conditions;
- retained-state revision / revocation;
- durable Decision Records and customer-safe evidence;
- managed evaluation and evidence export.

### Evolution 2

Evolution 2 is the richer continuity Engineering branch. Public-safe accepted checkpoints include structured ContinuityFrame interpretation, bounded hybrid retained-state retrieval, Open Loops/Reopen Semantics, Interaction Fit, suppression/proactive controls, Confidence/Clarification, Contradiction/Change Surfacing, record-only Outcomes, Agent Self-History, bounded behavioural signals, Session Observation foundation and Engineering Tuning.

Evolution 2 remains an **Engineering build rather than a finished Production commercial offer**.

---

## Why the Clean Reference Matters

Retained history must not win simply because it exists.

A clean current-task/reference behaviour remains available to compete with history-conditioned alternatives.

The important question is:

> **Did history actually earn the right to change the selection?**

That distinction matters in long-running agents, games/NPCs, simulations, regulated workflows and other systems where stale or over-dominant history can be as damaging as forgetting.

---

## Reference Memory Decomposition

The public paper uses a deliberately simplified reference decomposition:

- **Recency** — alignment with recent retained state;
- **Salience** — alignment with higher-importance retained items;
- **Anchor** — compatibility with persistent commitments/stability references.

The wider private CAAI architecture contains richer retained-state lifecycle, retrieval, confidence, change, suppression and evidence machinery than this paper’s minimal model.

The paper should therefore be read as a **formal public abstraction**, not a complete specification of the private runtime.

---

## Buyer-Facing Evaluation Pattern

A practical bounded demonstration should make retained-state influence measurable:

```text
same present condition
+ different retained history
→ measurable selection difference
→ disable retained-state influence
→ comparison/reference result
→ replay
→ inspectable evidence
```

This is an engineering/evaluation pattern. It is not independent empirical validation of Verrell’s Law.

---

## Independent Convergence Around the Problem

Independent research addresses adjacent pieces of the same engineering territory, including history-aware candidate verification, execution-path-aware runtime governance, trusted final authority outside the model, bounded action vocabularies, selective long-horizon memory and governed agent-memory architectures.

Current comparison:

- [Independent Convergence Map — Retained-State Selection, Agent Memory and Runtime Governance](research_notes/INDEPENDENT_CONVERGENCE_MAP_2026-08-30.md)

Those works strengthen the case that the surrounding problem is active. They do **not** prove CAAI is globally unique and do not independently validate Verrell’s Law.

---

## Repository Contents

```text
Memory-Weighted-Selection.pdf
                        — compiled paper

paper_source/
  paper.tex             — LaTeX source
  references.bib        — bibliography
  paper.bbl             — compiled bibliography
  fig_architecture.pdf  — reference architecture figure
  fig_scenario.pdf      — worked scenario figure

research_notes/
  QUANTUM_MEMORY_AND_CARBON_ADJACENT_EVIDENCE.md
                        — bounded adjacent-evidence research note

  INDEPENDENT_CONVERGENCE_MAP_2026-08-30.md
                        — comparison with adjacent research on
                          history-aware selection, memory and runtime governance
```

---

## Building the Paper

From the repository root:

```text
cd paper_source
pdflatex paper.tex
pdflatex paper.tex
pdflatex paper.tex
```

The included `paper.bbl` means no separate BibTeX run is required.

---

## Scope and Claims

The paper makes a narrow engineering-level claim about middleware candidate selection.

It does **not** claim consciousness/sentience, AGI, quantum implementation, electromagnetic memory as an established CAAI mechanism, new established physics, universal emotional/psychological inference, universal hallucination prevention, or disclosure of proprietary Crown internals.

---

## Evidence and Validation Boundary

CAAI engineering tests establish bounded software behaviour under declared test conditions.

That is not automatically independent empirical confirmation of Verrell’s Law merely because CAAI was deliberately built around retained-state selection.

A runtime test that reuses a selector’s own internal retained-state score is an **engineering conformance / implementation validation** unless the analysis uses an independently frozen score or another non-circular empirical route.

---

## Relationship to Verrell’s Law

Verrell’s Law is a separate proposed falsifiable retained-state selection research framework.

CAAI can be assessed entirely as software without accepting speculative physical interpretation.

Canonical research archive:

- [collapsefield-verrells-law](https://github.com/collapsefield/collapsefield-verrells-law)

---

## Status

**Paper status:** working public engineering paper.  
**Core Gold status:** frozen current commercial selector foundation.  
**Evolution 2 status:** richer Engineering branch, not yet a finished Production commercial offer.  
**Independent empirical validation:** separate research track.

---

## Citation

Until a preprint identifier is assigned, cite the working paper as:

> Ross, Marcos. “Memory-Weighted Selection: Middleware for Continuity and Governed Behaviour in LLM Systems.” Working paper, 2026.

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).

---

## Licence and Authorship

Copyright © 2026 Inappropriate Media Limited.  
Licensed under CC BY-NC-ND 4.0 — see [LICENSE.md](LICENSE.md).

You may share this work with attribution. You may not use it commercially or distribute modified versions except as permitted by the licence.

For a CAAI paid audit, evaluation, pilot, integration or licensing discussion, use the [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack).
