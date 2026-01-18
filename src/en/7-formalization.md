# 7. Formalization Sketch - Explicit Software Engineering Method

This document provides a mathematical and logical formalization sketch of the method.
It is intentionally minimal and focuses on: (1) entities, (2) relations, (3) normative obligations, and (4) diagnosability.
It describes constraints over explicit artifacts and relations, not a prescriptive workflow.
The goal is evaluability and diagnosability, not mathematical completeness.

The formalization aims for **operational objectivity under explicit context**, not absolute objectivity.

---

Before stating obligations, we must fix a universe of discourse. Without a declared universe, constraints have no stable targets and evaluation becomes ambiguous.

## 7.1 Universe of Discourse

We model engineering work as a set of entities and typed relations.

### 7.1.1 Entity Sets

Let the following sets exist:

- **I** : set of *Intents*
- **D** : set of *Decisions*
- **A** : set of *Artifacts*
- **S** : set of *Assumptions*
- **T** : set of *Trade-offs*
- **V** : set of *Validations*
- **C** : set of *Compensations*
- **Ch** : set of *Changes* (engineering changes)
- **P** : set of *Parameters* (contextual inputs)

Define the global entity set:

- **E = I ∪ D ∪ A ∪ S ∪ T ∪ V ∪ C ∪ Ch ∪ P**

### 7.1.2 Predicates (Typing)

We use unary predicates to type entities:

- Intent(x), Decision(x), Artifact(x), Assumption(x), TradeOff(x), Validation(x), Compensation(x), Change(x), Parameter(x)

---

Engineering reasoning is captured by relationships among these entities, not by an imposed sequence. A graph model makes traceability explicit without prescribing order.

## 7.2 Core Relations (Graph Model)

Engineering reasoning is represented as a typed directed multigraph over E.

### 7.2.1 Fundamental Relations

- **declares ⊆ Ch × I**  
  `declares(ch, i)` means change `ch` declares intent `i`.

- **serves ⊆ D × I**  
  `serves(d, i)` means decision `d` serves intent `i`.

- **justifies ⊆ A × (I ∪ D)**  
  `justifies(a, x)` means artifact `a` is justified by intent or decision `x`.

- **assumes ⊆ (D ∪ A) × S**  
  `assumes(x, s)` means entity `x` relies on assumption `s`.

- **tradesOff ⊆ (D ∪ A) × T**  
  `tradesOff(x, t)` means entity `x` involves trade-off `t`.

- **validates ⊆ V × (A ∪ D ∪ I)**  
  `validates(v, x)` means validation `v` provides evidence for entity `x`.

- **compensates ⊆ C × (I ∪ D ∪ A ∪ V)**  
  `compensates(c, x)` means compensation `c` explicitly compensates missing/insufficient x.

- **paramOf ⊆ P × Ch**  
  `paramOf(p, ch)` means parameter `p` applies to change `ch` (or project scope containing it).

### 7.2.2 Traceability (Derived)

Define a derived relation **traceableTo(x, y)** as the existence of a path from x to y using allowed relation edges.
At minimum, the trace graph uses edges:
- declares, serves, justifies, validates, assumes, tradesOff

Traceability requirements in the method constrain the existence of such paths and their navigability.

---

First-order logic is used here to express invariants over the graph. These are constraints to be evaluated, not computations to be executed.

## 7.3 First-Order Logic (FOL) Axioms / Invariants

The method is expressed as constraints that must hold regardless of workflow sequencing, reflecting orthogonality to process order. These constraints correspond directly to the normative rules defined earlier.

Below, `∀` means "for all" and `∃` means "there exists".

Rules 1-3 establish minimal explicitness and traceability for intent, decisions, and artifacts.

### 7.3.1 Rule 1 - Intent Declaration (Mandatory)

For any non-trivial change, an intent must be declared:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) → ∃i (Intent(i) ∧ declares(ch, i) ∧ Scoped(i)) )

If a non-trivial change has no declared intent, it is implicit work:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) ∧ ¬∃i (Intent(i) ∧ declares(ch, i)) → ImplicitWork(ch) )

### 7.3.2 Rule 2 - Decision Explicitness (Mandatory)

For any impactful decision, it must serve an intent (or be explicitly compensated):

- ∀d ( Decision(d) ∧ Impactful(d) → 
       (∃i (Intent(i) ∧ serves(d, i)) ∨ ∃c (Compensation(c) ∧ compensates(c, d))) )

And decisions that do not serve an intent are treated as assumptions unless compensated:

- ∀d ( Decision(d) ∧ Impactful(d) ∧ ¬∃i (Intent(i) ∧ serves(d, i)) ∧ ¬∃c (Compensation(c) ∧ compensates(c, d))
       → ∃s (Assumption(s) ∧ AssumptionByDefault(d, s)) )

### 7.3.3 Rule 3 - Artifact Traceability (Mandatory)

Any behavior-affecting artifact must trace to an intent or decision:

- ∀a ( Artifact(a) ∧ AffectsBehavior(a) → 
       (∃x ((Intent(x) ∨ Decision(x)) ∧ justifies(a, x)) ∨ ∃c (Compensation(c) ∧ compensates(c, a))) )

Orphan artifacts are unjustified:

- ∀a ( Artifact(a) ∧ AffectsBehavior(a) ∧ ¬∃x ((Intent(x) ∨ Decision(x)) ∧ justifies(a, x))
       → Orphan(a) )

Rules 4-6 cover validation, assumptions, and compensation under contextual risk.

### 7.3.4 Rule 4 - Validation Requirement (Contextual)

Critical elements require validation, with criticality dependent on parameters:

- ∀x ( Critical(x) → (∃v (Validation(v) ∧ validates(v, x)) ∨ ∃c (Compensation(c) ∧ compensates(c, x))) )

Critical(x) is not fixed; it is derived from parameters:

- ∀x ( Critical(x) ↔ CriticalUnderParams(x, ParamsScope(x)) )

Parameters are inputs to evaluation. They shape what counts as critical and what depth of validation is required; they do not excuse obligations.

### 7.3.5 Rule 5 - Assumption Declaration (Mandatory)

Whenever evidence is missing/deferred, assumptions must be explicit:

- ∀x ( EvidenceMissing(x) → ∃s (Assumption(s) ∧ assumes(x, s) ∧ Explicit(s)) )

### 7.3.6 Rule 6 - Explicit Compensation (Mandatory)

Whenever a required element is missing, compensation must exist and declare accepted risk:

- ∀x ( Required(x) ∧ Missing(x) → ∃c (Compensation(c) ∧ compensates(c, x) ∧ StatesAcceptedRisk(c)) )

Rule 7 makes context explicit so that evaluation is reproducible across teams and time.

### 7.3.7 Rule 7 - Parameter Awareness (Mandatory)

Each relevant scope must declare applicable parameters:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) → ∃p (Parameter(p) ∧ paramOf(p, ch)) )

Parameters affect obligations by defining thresholds and scopes; they are not tuning knobs for correctness.

Rule 8 ties the constraints to diagnosability, aligning the method with failure analysis.

### 7.3.8 Rule 8 - Diagnosability of Failure (Outcome Rule)

For any observed failure f, at least one method-level explanation must be identifiable:

- ∀f ( Failure(f) → ∃r (Reason(r) ∧ ExplainsInMethodTerms(r, f)) )

Minimal admissible reasons:

ExplainsInMethodTerms(r, f) implies at least one of:
- MissingIntent(f)
- InvalidDecision(f)
- UnvalidatedArtifact(f)
- FalseAssumption(f)
- InadequateCompensation(f)
- MisconfiguredParameters(f)

---

## 7.4 Deontic Layer (Obligations, Permissions, Consequences)

FOL invariants describe truth conditions. The method is normative: it includes obligations.
The deontic operators O, P, and R are interpretive layers over the invariants; they do not replace or extend the underlying FOL constraints.
We model this with a deontic operator:

- **O(φ)** : it is obligatory that φ holds (MUST)
- **P(φ)** : it is permitted that φ holds (MAY)
- **R(φ)** : it is recommended that φ holds (SHOULD)

### 7.4.1 MUST as Obligation

Example (Rule 1):

- O( Change(ch) ∧ NonTrivial(ch) → ∃i (Intent(i) ∧ declares(ch,i) ∧ Scoped(i)) )

### 7.4.2 Compensation as Permission Under Obligation

The method permits shortcuts only if compensated:

- P( Missing(x) )  IF  O( ∃c (Compensation(c) ∧ compensates(c, x) ∧ StatesAcceptedRisk(c)) )

This expresses: missing artifacts/validation may occur, but only under explicit compensation.
Compensation is permission under obligation; it records accepted risk and does not remove the obligation.

### 7.4.3 Consequences (Violation Semantics)

Define a violation predicate:

- Violation(rule_k, scope)

For example:

- ¬∃i (Intent(i) ∧ declares(ch,i))  implies  Violation(Rule1, ch)

A compliance check is then a function from a repository state to the set of violations:

- Violations(State) = { (rule_k, scope) | State ⊭ rule_k(scope) }

This is the basis for tooling without prescribing workflow.

---

## 7.5 Minimal Compliance and Diagnosability as Functions

### 7.5.1 Compliance Function

Given a state containing entities and relations:

- **Compliant(State)** iff Violations(State) = ∅

### 7.5.2 Diagnosability Function

Given a failure f and a state:

- **Diagnosable(f, State)** iff ∃r ExplainsInMethodTerms(r, f)

This can be implemented as querying the explicit graph for missing links, missing validation, missing compensation, or parameter mismatches. It is the formal counterpart to the diagnosability requirement discussed earlier.

---

## 7.6 Practical Notes (Non-Normative)

This level of formalization is sufficient to support objective evaluation, failure diagnosis, and tooling implementation without prescribing workflow.
- This formalization is compatible with graph databases and constraint checking.
- It is intentionally independent of any specific development process or lifecycle.
- Temporal logics (e.g., TLA+) and execution semantics may be introduced later to model evolution, reconstruction post-hoc, or concurrency, but are intentionally excluded from the method core.

---
