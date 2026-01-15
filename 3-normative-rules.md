# 3. Normative Core Rules (Draft)

These rules are normative constraints and obligations of the method.
Each rule is stated to be verifiable, to imply consequences when violated, and to support analysis without dependence on tooling.
They are independent of workflow sequencing and do not prescribe a process.

## 3.1 Rule 1 - Intent Declaration (Mandatory)
Every non-trivial engineering change MUST declare an explicit Intent.
Intent defines the desired outcome, property, or constraint the change aims to satisfy.
Intent MUST have a defined scope.
Changes without declared intent are considered implicit work.

Rationale:
Without intent, no validation or traceability is possible. Quality becomes accidental.

## 3.2 Rule 2 - Decision Explicitness (Mandatory)
Every irreversible or impactful engineering decision MUST be made explicit.
A Decision MUST reference:
- the Intent it serves
- the alternatives considered (at least implicitly)
Undocumented decisions are treated as assumptions by default.

Rationale:
Undocumented decisions prevent post-failure analysis and learning.

## 3.3 Rule 3 - Artifact Traceability (Mandatory)
Every Artifact that affects system behavior MUST be traceable to at least one Intent or Decision.
Orphan artifacts are considered unjustified artifacts.
Traceability MUST be navigable in both directions.

Rationale:
Untraceable artifacts increase complexity without accountable value.

## 3.4 Rule 4 - Validation Requirement (Contextual)
Artifacts and Decisions with critical impact MUST have explicit Validation.
What is considered critical is a method parameter, not a fixed threshold.
Validation MAY take different forms:
- tests
- reviews
- proofs
- simulations
- external evidence

Rationale:
Critical work without validation is indistinguishable from speculation.

## 3.5 Rule 5 - Assumption Declaration (Mandatory)
Assumptions MUST be explicitly declared when evidence is missing or deferred.
Assumptions MUST be identifiable as such.
Assumptions SHOULD be tracked until validated or invalidated.

Rationale:
Implicit assumptions silently accumulate risk.

## 3.6 Rule 6 - Explicit Compensation (Mandatory)
When a required artifact or validation is missing, the absence MUST be explicitly compensated.
Compensation MUST:
- be documented
- reference the missing element
- state the accepted risk

Rationale:
Shortcuts are allowed; silent shortcuts are not.

## 3.7 Rule 7 - Parameter Awareness (Mandatory)
The method MUST be applied with explicit contextual parameters.
Examples of parameters:
- domain criticality
- risk tolerance
- regulatory pressure
- team scale
- expected lifespan of the system

These parameters influence:
- required explicitness level
- validation depth
- acceptable compensations

Rationale:
Quality is contextual; rigor without context is waste.

## 3.8 Rule 8 - Diagnosability of Failure (Outcome Rule)
When failure occurs, it MUST be possible to explain it in terms of method application.
At least one of the following MUST be identifiable:
- missing intent
- invalid decision
- unvalidated artifact
- false assumption
- inadequate compensation
- misconfigured parameters

Rationale:
If failure cannot be explained in method terms, the method was not applied.

## 3.9 Meta-Note
These rules do not describe a process.
They define constraints and obligations that must hold regardless of workflow.
That is what makes them rules of a method, not of a process.
