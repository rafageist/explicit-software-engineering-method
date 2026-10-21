# Open Normative Decisions

Status: pending maintainer decision. Not part of the manuscript.

Each entry below is a question whose answer changes what the method requires. The 0.3 draft does not settle these questions silently. The manuscript keeps the 0.2.1 normative statements and adds the recommended interpretation, labeled *Proposed interpretation (OD-n)*, so the effect can be reviewed in context. Rejecting a recommendation means editing or removing the labeled paragraph; no other text depends on it unless noted.

Format: question, why it matters, alternatives, recommendation, where it appears.

---

## OD-1. Status and strength of Rule 8 (Diagnosability of Failure)

**Question.** Must every failure map to a method-level gap?

**Why it matters.** As written, R8 says that a failure which cannot be explained in method terms proves that the method was not applied. Chapter 6.6 admits external and irreducible failures. A system that meets every obligation can still fail (provider outage, hardware fault, a risk accepted correctly). The strong reading either declares such systems non-compliant or pushes analysts to find gaps after the fact (review F-13, F-14).

**Alternatives.**
- **A. Keep the strong reading.** Every failure must be attributed to at least one of the six listed reasons.
- **B. Diagnosability of the record (recommended).** R8 obliges the engineering record to be sufficient to classify each identified causal factor of a failure as one of: method-level gap (violated or inadequately compensated obligation), realized accepted risk (valid compensation or declared assumption), parameter misclassification, external or out-of-scope factor, or *unrelated* (within scope but not relatable to any element of the record). R8 is violated only by unrelated factors. If a relation exists but its evidence is inaccessible, the outcome is indeterminate. A factor traced to a violated obligation is a *diagnosed* gap: R8 is satisfied because the failure is explained, while the other rule is violated.
- **C. Demote R8 to an evaluation property.** Remove it from the rules and keep diagnosability as a derived measure of the record.

**Recommendation.** B. It keeps R8 as an obligation with an identifiable addressee (the record), aligns with chapter 6, and stops treating realized accepted risk as a defect.

**Where.** Ch. 3.8, 6.6, 7.7, 9 (Scenario E).

---

## OD-2. Meaning of "undocumented decisions are treated as assumptions by default" (R2)

**Question.** Does treating an undocumented decision as an assumption satisfy R2?

**Alternatives.**
- **A. Discharge.** Once the choice is classified as an assumption, R2 is satisfied for it and R5 takes over.
- **B. Diagnostic classification (recommended).** The obligation instance of R2 stays *violated* unless it is compensated. The classification only states how the unrecorded choice is treated in diagnosis: as an unvalidated premise, not as a reviewed decision.

**Recommendation.** B. Under A, recording nothing would be a cheaper way to meet R2 than recording the decision.

**Where.** Ch. 3.2, 7.3 (R2).

---

## OD-3. "The alternatives considered (at least implicitly)" (R2)

**Question.** What exactly must a decision record contain about alternatives?

**Alternatives.**
- **A. Keep the current text.** Alternatives may remain implicit, so in practice only the intent link is checkable.
- **B. Explicit alternatives or explicit absence (recommended).** The record MUST either list the alternatives considered or state explicitly that none were evaluated, with the reason.
- **C. At least one rejected alternative is mandatory.**

**Recommendation.** B. It removes the contradiction without forcing teams to invent alternatives they did not evaluate. C would encourage fabricated "straw" alternatives.

**Where.** Ch. 3.2, 7.3 (R2).

---

## OD-4. Normative coverage of trade-offs

**Question.** Trade-offs are named in the thesis, but no rule creates an obligation about them. Should one?

**Alternatives.**
- **A. Fold into R2 (recommended).** When an impactful decision balances competing quality attributes or constraints, the decision record MUST state the accepted trade-off.
- **B. New Rule 9.** A separate obligation for trade-offs.
- **C. Keep trade-offs non-normative.** They remain an optional entity and are removed from the thesis statement.

**Recommendation.** A. A trade-off is a property of a decision. A ninth rule would change the method's identity.

**Where.** Ch. 3.2, 7.3 (R2), glossary.

---

## OD-5. Which obligations are compensable

**Question.** R6 prose speaks of a missing "artifact or validation"; the 0.2.1 formulas allow compensation for intents and decisions as well.

**Alternatives.**
- **A. Everything compensable.**
- **B. R2, R3, R4, R5 compensable; R1 and R7 not (recommended).** A compensation must state what risk is accepted, which presupposes a stated intent and a declared context. Writing a valid compensation for a missing intent requires stating the intent, which already satisfies R1. R6 itself (a meta-rule) and R8 (an outcome rule) are not subject to compensation.
- **C. Only R4 (validation) and R3 (artifact) compensable, following the literal prose of R6.**

Independently of the alternative chosen, parameters MAY declare further obligations as non-compensable in a given context (for example, validation of safety functions).

**Recommendation.** B.

**Where.** Ch. 3.6, 7.4, 8.5. Formal: the set `K` of compensable rules.

---

## OD-6. Compensation expiry and retroactive compensation

**Questions.** (a) Must a compensation declare when it expires or is reviewed? (b) Does a compensation recorded *after* the deviation was exposed (for example after a failure) count?

**Alternatives for (a).**
- **A1. Mandatory review condition (recommended).** A date or an event. An open-ended acceptance is allowed only if parameters explicitly permit permanent acceptance for that kind of obligation.
- **A2. Optional (SHOULD).**

**Alternatives for (b).**
- **B1. Count it, flagged as retroactive (recommended).** It counts for evaluation at times after it was recorded. For diagnosing a failure that occurred before it was recorded, it is not evidence that the risk was accepted.
- **B2. Never count retroactive compensations.**
- **B3. Count them without distinction.**

**Recommendation.** A1 + B1. This makes compensation timing the one place where *when* something was recorded matters. Section 5.4 explains why this does not breach orthogonality: accepting a risk is meaningful only before exposure to it.

**Where.** Ch. 3.6, 7.6, 8.5, 9 (Scenario C).

---

## OD-7. Risk acceptance authority

**Question.** Who may accept the risk recorded in a compensation?

**Alternatives.**
- **A. Declared authority policy (recommended).** The method requires that the parameter set declare who may accept which risk, and that each compensation identify the accepting party. The method does not prescribe roles.
- **B. A + independence for critical obligations.** For obligations classified as critical, the method itself forbids self-acceptance by the author of the change.
- **C. Leave authority entirely implicit.**

**Recommendation.** A. Independence (B) is valuable but depends on organization size and domain, so it should be a parameter, not a method constant. C fails the purpose of compensation.

**Where.** Ch. 3.6, 3.7, 8.3, 8.5.

---

## OD-8. Reconstructed and inferred records

**Question.** Can intents, decisions or links reconstructed after the fact, or inferred by tools (including language models), satisfy obligations?

**Alternatives.**
- **A. Provenance-qualified satisfaction (recommended).**
  - *Contemporaneous* and *retrospective* records written by a responsible person satisfy obligations.
  - *Reconstructed* records (historical rationale recovered from evidence and confirmed by a responsible person) satisfy obligations prospectively and must be marked as reconstructed. They are never presented as original rationale.
  - *Inferred* records (proposed by analysis or tooling, not confirmed) never satisfy obligations. At most they make an outcome *indeterminate* instead of *violated*.
- **B. Only contemporaneous records count.** This makes adoption on legacy systems impossible.
- **C. Any record counts regardless of provenance.**

**Recommendation.** A.

**Where.** Ch. 8.4, 9 (Scenario D), 10.

---

## OD-9. Minimum parameter set (R7)

**Question.** Which parameters must an application declare for R7 to be satisfied?

**Alternatives.**
- **A. Policies for every parameter-dependent predicate (recommended).** The parameter set MUST declare a policy (a criterion, not necessarily a numeric threshold) for each predicate the rules depend on: change unit and triviality, impact/irreversibility, behavior-affecting artifact, criticality, validation adequacy, compensation admissibility and authority. Context descriptors (domain criticality, risk tolerance, regulatory pressure, team scale, expected lifespan) are recommended inputs to those policies.
- **B. Context descriptors only.** Keep the 0.2.1 list. Evaluators derive the policies themselves.
- **C. Free-form.** Any explicit declaration.

**Recommendation.** A. Under B, two evaluators with the same declared context can disagree on every applicability question.

**Where.** Ch. 3.7, 7.2.4, 8.3.

---

## OD-10. Outcome classes and aggregate verdict

**Question.** Should the method adopt the five outcomes (*satisfied, violated, compensated, not applicable, indeterminate*) and the aggregate verdict proposed in ch. 7.5 and 8.7?

**Alternatives.**
- **A. Adopt as normative evaluation semantics (recommended).** An evaluation with any *indeterminate* outcome MUST NOT be reported as compliant.
- **B. Adopt the outcomes as informative only.** Evaluators may use other schemes.
- **C. Fewer classes.** Merge *indeterminate* into *violated*.

**Recommendation.** A. C reintroduces the conflation of missing evidence with absence (F-16).

**Where.** Ch. 7.5, 8.7.

---

## OD-11. Method versioning and earlier evaluations

**Question.** How do method versions relate to earlier evaluation results?

**Proposal.**
- An evaluation is bound to the ruleset version it used. A new method version never changes an earlier result. Re-evaluation produces a new result.
- Version numbers follow `MAJOR.MINOR.PATCH`. MAJOR: an obligation is added, removed or strengthened in a way that can turn an earlier *satisfied* or *not applicable* outcome into *violated*. MINOR: clarifications or new evaluation semantics that can change outcomes only from *indeterminate* to another class, or add new non-normative chapters. PATCH: editorial changes with no effect on outcomes.
- While the method is below 1.0, MINOR increments may contain normative changes, which the changelog must list.

**Recommendation.** Adopt. Without this, issue #2 ("how method version changes affect previous assessment results") has no answer.

**Where.** Ch. 8.6, `CHANGELOG.md`, `docs/release-checklist.md`.

---

## OD-12. Subjects of Rule 4

**Question.** R4 prose says "Artifacts and Decisions"; the 0.2.1 formula quantifies over any entity.

**Alternatives.** **A. Artifacts and decisions (recommended, follows prose).** Intent validation is permitted and recorded, but not required. **B. Any entity, as in the formula.**

**Recommendation.** A.

**Where.** Ch. 3.4, 7.3 (R4).

---

## Non-normative decisions needed for the pull request

- **Version number.** The draft uses `0.3.0-draft` in `manifest.yaml`. Choose the final number at release time.
- **Release gating.** The workflow now publishes only on a `v*` tag that matches the manifest, or on manual dispatch (review F-33). Confirm that this replaces the previous publish-on-push behavior.
