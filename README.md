# Memory-Weighted Selection

**A public engineering working paper on governed, retained-state candidate selection**  
**Author: Marcos Verrell Moss Ross (M.R.) — Independent Researcher**  
**Edition: October 2026, second public working-paper edition**

[Read the full paper (PDF)](Memory-Weighted-Selection.pdf) · [LaTeX source](paper_source/paper.tex) · [Bibliography](paper_source/references.bib)

---

## Abstract and contribution

The paper presents a public reference model for selecting between host-provided candidate actions or responses using declared retained state, host utility and explicit governance. It separates the **candidate eligibility gate** from optional preference or utility ranking, and describes how memory might influence scoring and selection without retraining an upstream foundation model. The included numerical scenarios are **illustrative**, not independent runtime or participant results.

The reference formulation is intentionally not a disclosure of CAAI's proprietary Crown implementation. Candidate re-ranking, memory retrieval, history-based decisions and policy controls all have substantial prior art; the narrower engineering research programme evaluates their bounded combination and auditability.

---

## Read in this order

1. [Paper (full PDF)](Memory-Weighted-Selection.pdf) — formal framework, worked examples, limitations and future work.
2. [LaTeX manuscript](paper_source/paper.tex) — LaTeX manuscript source.
3. [Bibliography](paper_source/references.bib) — cited research.
4. [Adjacent evidence note](research_notes/QUANTUM_MEMORY_AND_CARBON_ADJACENT_EVIDENCE.md) — contextual, not claimed to validate the engineering mechanism.
5. [Independent convergence map](research_notes/INDEPENDENT_CONVERGENCE_MAP_2026-08-30.md) — related research and novelty boundaries.

---

## Architecture and scope

- An upstream host supplies candidate actions or outputs.
- Eligibility and veto conditions constrain which candidates may be selected.
- An illustrative scoring objective combines base utility with candidate-relative retained-state alignment and optional soft preferences.
- A defined influence-disabled reference case and evidence record enable comparison in **tested conditions**.
- Stored records, deterministic reruns and exact historical-snapshot replay are different capabilities and must not be conflated.

### Engineering evidence boundary

This paper describes a public reference model. It makes no performance or acceptance claim about any commercial implementation; such claims, where made, are published separately with their evidence. The numerical worked examples are not independent runtime measurements.

---

## Relationship to Verrell's Law

[Verrell's Law Research Archive](https://github.com/collapsefield/collapsefield-verrells-law) explores broader history-sensitive selection questions and independently testable predictions. The present manuscript is a **middleware engineering reference**, not a proof of a general physical law. The wider research historically considered electromagnetic and quantum-field analogies; those remain open **theoretical lines of inquiry**, not implemented or evidenced mechanisms of this middleware.

---

## Where this work may be relevant

Governed AI agents, audit/evaluation tooling, simulation and prospective game/NPC decision systems. Integration suitability, reliability, policy enforcement and latency must be shown in the target runtime and workflow.

---

## Reproduce the worked example

Run `python reference_impl/reproduce.py` (standard-library Python). This reproduces the four ablation rows and the winner-change threshold without any proprietary code.

---

## Build from source

```bash
cd paper_source
pdflatex paper.tex
pdflatex paper.tex
```

The compiled bibliography (`paper.bbl`) is supplied for reproducibility.

---

## Cite

Marcos.Verrell (M.R.) *Memory-Weighted Selection: Middleware for Continuity and Governed Behaviour in LLM Systems*. Working paper, 2026. See [CITATION.cff](CITATION.cff) for machine-readable metadata. Any later Zenodo DOI should be version-specific and added only after an actual deposit.

---

## Licensing and IP

The pre-existing [LICENSE.md](LICENSE.md) remains in effect. The author credit is Marcos Verrell; ownership and licensing are distinct matters. No change of legal ownership is asserted by this edition. Public manuscript access is not a licence to use unpublished Crown code or internal implementation. No private Crown code, audit pack, secrets or commercial source material is included here.

---

## Edition history

- First working-paper edition: 13 July 2026.
- Second edition: 20 October 2026; corrected selection/ablation example, explicit hard gate, updated prior art and reproducible reference code.
