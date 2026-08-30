# Independent Convergence Map — Retained-State Selection, Agent Memory and Runtime Governance

**Date:** 30 August 2026  
**Status:** Public research note / literature-positioning aid  
**Programme:** Memory-Weighted Selection / Collapse Aware AI (CAAI)  
**Evidence rule:** Adjacent work is evidence that the problem space is active. It is **not** independent validation of CAAI or Verrell’s Law.

---

## Why this note exists

Several independent research directions are converging on pieces of the same engineering problem:

- history should sometimes affect what happens next;
- memory should be selective rather than unlimited;
- models should not own final operational authority;
- runtime policy needs path/history context;
- actions should be bounded and auditable;
- durable evidence matters after a decision.

CAAI should not claim that any one of those ingredients is unique.

The commercially relevant question is whether the **combination and enforcement boundary** are distinct enough to solve a buyer problem better than ordinary memory, prompting or policy tooling.

---

# 1. HAVE — History-Aware VErifier

**Paper:** Yishu Li, Xinyi Mao, Ying Yuan, Kyutae Sim, Ben Eisner, David Held. *Learn from What We HAVE: History-Aware VErifier that Reasons about Past Interactions Online.* CoRL 2025 / PMLR 305.

Reference: https://proceedings.mlr.press/v305/li25e.html

### What it does

HAVE explicitly decouples action generation from history-aware verification:

```text
current observation
→ generator proposes multiple candidate actions
→ verifier reasons over past interactions
→ verifier scores candidates
→ highest-scoring action is selected
```

### Strong convergence with CAAI

- multiple candidates exist before final choice;
- historical interactions are evaluated downstream of generation;
- selection, not merely retrieval, is the operational point where history matters;
- generation and selection are separated.

### Important differences

HAVE is presented as a robot-manipulation architecture whose verifier predicts action success in ambiguous environments.

CAAI’s public engineering emphasis is broader:

- host-supplied/permitted action boundary;
- retained-state influence under explicit governance;
- clean/reference competition;
- persistence and lifecycle controls;
- replay/evidence lineage;
- provider-independent local final selection once candidates exist.

HAVE therefore prevents any blanket claim that “history-aware candidate selection” itself is unique to CAAI.

It also independently supports the importance of **decoupling generation from history-aware selection**.

---

# 2. Runtime Governance for AI Agents: Policies on Paths

**Paper:** Maurits Kaptein, Vassilis-Javed Khan, Andriy Podstavnychy. 2026.

Reference: https://arxiv.org/abs/2603.16586

### What it does

The framework treats the partial execution path as the central object for runtime governance. A deterministic policy function evaluates:

```text
agent identity
+ partial execution path
+ proposed next action
+ organisational state
→ policy violation probability
```

### Convergence

- history/path is relevant at the moment of action;
- runtime governance is external to prompt-level behaviour shaping;
- policy evaluation should be deterministic/auditable where possible;
- current action cannot be judged only from a stateless snapshot when policy is path-dependent.

### Difference

The framework asks whether a proposed action satisfies policy. It does not primarily define a retained-state scoring layer that ranks several permitted candidates relative to a clean reference path.

The relationship is therefore complementary:

```text
policy boundary: what is allowed?
retained-state selection: among what remains allowed, what should win given relevant history?
```

---

# 3. Aegis — Action-Boundary Runtime Governance

**Paper:** Adam Mazzocchetti. *Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution.* 2026.

Reference: https://arxiv.org/abs/2608.16891

### What it does

Aegis treats model outputs as action proposals and places final authority in a trusted runtime decision layer.

Its central separation is effectively:

```text
model proposes
→ trusted runtime mediates
→ authorised action executes or fails closed
```

### Convergence

- final authority belongs outside the model;
- provenance must not be self-declared by model output;
- consequential actions need a trusted execution boundary;
- auditable evidence matters.

### Difference

Aegis focuses on security/governance of proposed actions rather than retained-state weighting over a bounded candidate set.

For CAAI, this strengthens the architectural case for keeping the **governor/final authority outside the retained-memory or generative layer**.

---

# 4. Five Primitives for Governing Autonomous AI Agents at Runtime

**Paper:** Jiten Oswal, John Cadeddu. 27 August 2026.

Reference: https://arxiv.org/abs/2608.26696

### What it does

The paper argues that agent governance is a runtime problem and describes five primitives around discovery, identity, governance, attestation and supply chain.

Its implementation includes:

- mediation before action takes effect;
- per-tenant action vocabulary;
- durable/hash-linked evidence.

### Convergence

- bounded action vocabularies;
- runtime mediation;
- evidence after action selection;
- governance as infrastructure rather than prompt wording.

### Difference

The paper does not present retained historical state as a candidate-relative influence term for selecting one permitted action over another.

The strongest relationship is architectural adjacency rather than duplication.

---

# 5. Weighted Memory Tree (WMT)

**Paper:** Quang Dao, Purvi Kathalkar, Kenneth Eaton. *Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents.* 21 August 2026.

Reference: https://arxiv.org/abs/2608.20631

### What it does

WMT organises long-horizon execution history into a hierarchy and assigns memories dynamic retention scores. It can:

- preserve useful history;
- decay lower-utility history;
- fold completed branches;
- suppress obsolete information;
- later recover folded context.

The paper reports, relative to linear memory in its tested GAIA settings:

- average accuracy improvement of 9.97 percentage points;
- average prompt-token reduction of 32.8%.

### Convergence

- retained information should not remain equally active forever;
- relevance/utility/lifecycle matter;
- stale or poisoned history can degrade behaviour;
- selective retained state can reduce prompt burden.

### Difference

WMT primarily controls **which memories remain active in model context**.

CAAI’s narrower engineering distinction is downstream:

> **What should retained information be allowed to change when several permitted behaviours/actions are available?**

WMT therefore supports the importance of selective memory, but its published token result must not be reused as if it were a measured CAAI saving.

---

# 6. Agent Memory — Governed Reference Architecture

**Repository:** MythologIQ-Labs-LLC/agent-memory

Reference: https://github.com/MythologIQ-Labs-LLC/agent-memory

The repository defines agentic memory as retained state capable of altering future interpretation, reasoning, planning, tool use, action or adaptation across a meaningful persistence boundary.

### Convergence

- retained state is defined by future causal relevance rather than storage alone;
- provenance and authority boundaries matter;
- memory needs lifecycle/governance;
- state may change future action.

### Difference

It is a broad governed-memory reference architecture rather than the specific CAAI final-selection architecture.

This is another reason CAAI should avoid claiming that “retained state can affect action” is itself unique.

---

# Convergence Matrix

| Capability / question | HAVE | Policies on Paths | Aegis | Five Primitives | WMT | Agent Memory | Public CAAI direction |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multiple candidate actions before final choice | Yes | Not primary | Proposal-centric | Action vocabulary | No | Broad | Yes |
| History affects downstream decision | Yes | Yes | Policy state/path | Not primary | Memory activation | Yes | Yes |
| Final authority outside generator/model | Partial separation | Policy engine | Yes | Yes | No | Governance-oriented | Yes |
| Explicit bounded permitted candidate set | Candidate batch | Proposed action | Policy-mediated | Yes | No | Depends on implementation | Yes |
| Retained-state lifecycle / suppression | Interaction history | Path history | Policy/provenance | Not primary | Yes | Yes | Yes |
| Clean/reference comparison | Not central | Not central | Comparator possible | Not central | Baselines | Depends | Yes |
| Deterministic/replayable local selection evidence | Not central | Deterministic policy | Strong provenance | Attestation/ledger | No | Conformance-oriented | Yes in tested engineering lineage |
| Reported prompt-token reduction | No | No | No | No | Yes | No | Must be measured separately |

The table is intentionally conservative. “Yes” means the cited system or paper clearly exposes that element; it does not mean identical implementation.

---

# Commercial Interpretation

The convergence picture argues against selling CAAI as:

> “We invented AI memory.”

or:

> “Nobody has ever used history to choose an action.”

Those claims would be weak.

A stronger description is:

> **CAAI combines governed history-conditioned candidate selection with an external final-selection authority, persistent retained-state controls and replayable decision evidence as provider-independent middleware.**

That is narrower, more testable and better aligned with the current public engineering record.

---

# Research Interpretation

Independent systems appearing near parts of the architecture can provide **convergence evidence that the problem is real**.

They do not establish:

- that CAAI is globally unique;
- that Verrell’s Law is empirically validated;
- that the CAAI implementation is superior without direct benchmarking;
- that similar terminology implies shared mechanism.

The correct research response is comparative testing, not ownership by assertion.

---

# Next Useful Public Tests

1. **Candidate-selection benchmark** — matched candidate sets with history varied/ablated.
2. **Continuity-integrity benchmark** — stale, contradicted, revoked and falsely recalled history.
3. **Runtime-authority benchmark** — verify retained memory cannot escape the permitted action boundary.
4. **Replay benchmark** — freeze state/config/candidates and reproduce local final choice/evidence.
5. **Cost benchmark** — measure provider calls/tokens when local final selection replaces a genuine provider decision call.

The corresponding public benchmark proposal is maintained in the Verrell’s Law repository:

https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md

---

**Bottom line:** the surrounding field is converging on selective memory, history-aware action choice and external runtime governance. The defensible CAAI position is the specific governed combination and demonstrated system behaviour, not ownership of the underlying ingredients.
