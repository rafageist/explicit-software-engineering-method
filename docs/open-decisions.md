# Open Normative Decisions

Status: under maintainer review. Not part of the manuscript.

| Decision | Status (review of PR #4, 2026-10-21) |
|---|---|
| OD-2, OD-3, OD-4, OD-6, OD-7, OD-8, OD-9, OD-10, OD-11, OD-12 | Recommendation accepted as the basis for the next draft |
| OD-1 | Refined: alternative D below, pending final approval |
| OD-5 | Refined: alternative D below, pending final approval |
| OD-13, OD-14, OD-15 | New, raised by the refinements of OD-1 and OD-5; pending decision |

Until final approval, the manuscript keeps every interpretation labeled as *Proposed interpretation (OD-n)*. Removing the labels and incorporating the interpretations into the rule statements is a change to the method's normative identity and is done only after final approval.

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

**Recommendation (initial).** B. It keeps R8 as an obligation with an identifiable addressee (the record), aligns with chapter 6, and stops treating realized accepted risk as a defect.

**Review.** B was accepted in principle, with one refinement: distinguish a missing engineering-context relationship from causal uncertainty or an incomplete failure investigation, and do not classify an obligation as violated merely because a causal factor cannot yet be reliably related to the engineering record.

- **D. Diagnosability with established factors (recommended, refines B).**
  - The causal analysis produces an investigation record: factors, each *established* or *provisional*, the place in the system where each acts (or *undetermined*), and optionally a declaration that the set of factors is final. The method does not decide any of these; it reads them.
  - Only an established factor with a known place of action is classified. Classes 1 to 4 are those of B. Class 5, *unrelated*, now requires a decided absence: the place lies within scope, the record is declared complete for that part of the scope, and no element of it relates to the factor. This is the *missing engineering-context relationship*.
  - A provisional factor, an undetermined place, inaccessible evidence or a missing completeness declaration leaves the factor *unresolved*.
  - ⟨R8, f⟩ is *violated* if some factor is unrelated, *satisfied* if the set of factors is declared final and all are in classes 1 to 4, and *indeterminate* otherwise.
  - The failure analysis never creates violations of other rules. Class 1 points to instances already violated on the record before the failure. Findings of the analysis enter the evaluation only as recorded judgments about established facts.

**Normative implications of D.**
1. Rule 8 is addressed to the record, and its violation now requires positive knowledge: an established factor and a decided absence of any relation. Causal uncertainty is never evidence against the team.
2. An open investigation yields *indeterminate* for Rule 8, never *satisfied* (OD-14). The outcome changes only from *indeterminate* to another class as the analysis proceeds (Proposition 7.8).
3. Rule 5 violations discovered through failure analysis (a hidden premise) require that the reliance on the premise be established. A suspected premise gives *indeterminate* (ch. 3.5, 7.3.5).
4. Evaluators need a completeness declaration for the part of the scope where an unrelated factor acts. Without it, Rule 8 is *indeterminate*, as for any other rule (Proposition 7.2).
5. A change made outside the record (for example through a provider console) is reported under Rule 8 only. Whether it also produces instances of Rules 1 and 3 is OD-15.

**Where.** Ch. 3.5, 3.8, 6.6, 7.7 (Definitions 7.17, 7.18, Proposition 7.8), 8.6, 9 (Scenario E and its variant), glossary (*causal factor*).

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

**Recommendation (initial).** B.

**Review.** Reconsider the compensability of Rule 5. The minimum obligation to identify and declare an assumption should not disappear through compensation. Distinguish the declaration of an assumption from compensable validation or evidence gaps associated with it.

- **D. R2, R3, R4 compensable; R1, R5, R7 not; evidence gaps of assumptions compensated under R4 (recommended, refines B).**
  - Rule 5 requires the declaration: the premise is recorded as an assumption and linked to the elements that rely on it. It does not require evidence; an open, declared assumption satisfies it. The declaration cannot be compensated, because only a premise that has been declared can be the object of an accepted risk. A compensation whose risk statement mentions a premise does not count as declaring it.
  - Where the context requires evidence for a premise (a critical element relies on it), the validation-adequacy policy may include that evidence in the Rule 4 requirement of the element. The gap is then an instance of Rule 4, compensable under Rule 6, and the compensation references the declared assumption.
  - Tracking assumption status stays a SHOULD.

**Normative implications of D.**
1. $K = \{R2, R3, R4\}$. An undeclared premise that an element is established to rely on leaves the Rule 5 instance *violated* whatever compensations exist.
2. No outcome can be *compensated* under Rule 5. A case that B would have reported as *compensated* under Rule 5 is *satisfied* if the compensation itself recorded the premise as an assumption, and *violated* otherwise. Compared with B this is a tightening; compared with 0.2.1, whose formulas allowed compensation everywhere, it removes a way of meeting Rule 5. Under the versioning policy (OD-11) it is a normative change.
3. Evidence for premises becomes a matter of the validation-adequacy policy. If the policy does not mention premises, a declared but unvalidated premise produces no gap anywhere: the risk is visible but not required to be validated. Whether the policy must address premises is OD-13.
4. Scenario C (S-20 with C-9 under R4) and Scenario E (S-201 and ⟨R4, consumer.yaml@4c2⟩) illustrate the split.

**Where.** Ch. 3.1, 3.5, 3.6, 7.3.4, 7.3.5, 7.3.9, 7.4.2, 8.3, 9 (Scenarios C and E). Formal: the set `K` of compensable rules.

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

## OD-13. Validation adequacy and declared assumptions

Raised by OD-5/D.

**Question.** Must the validation-adequacy policy state how it treats declared assumptions that critical subjects rely on?

**Alternatives.**
- **A. Optional (current draft text).** The policy MAY require that such premises be validated. If it is silent, declared premises create no Rule 4 gap.
- **B. Mandatory coverage (recommended).** As part of OD-9, the adequacy policy MUST state whether, and which, premises of critical subjects require validation. The answer may be "none". A policy that is silent leaves the affected Rule 4 instances *indeterminate*.
- **C. Method constant.** Every premise a critical subject relies on MUST be validated or compensated under Rule 4.

**Recommendation.** B. It keeps strictness contextual (Rule 7) while making the choice explicit, so that a reliance on unvalidated premises in critical work is a declared policy rather than an omission. C would make the strictness of every context identical on this point.

**Where.** Ch. 3.5, 7.3.4, 8.3.

---

## OD-14. Final set of factors for Rule 8

Raised by OD-1/D.

**Question.** Can ⟨R8, f⟩ be *satisfied* before the investigation declares its set of factors final?

**Alternatives.**
- **A. No (recommended, current draft text).** *Satisfied* requires the declaration. Without it, the outcome is *indeterminate* unless a factor is already unrelated.
- **B. Yes.** *Satisfied* when every factor identified so far is in classes 1 to 4. A later factor can turn it into *violated*.

**Recommendation.** A. Under B a *satisfied* outcome could later become *violated* without any error in the earlier evaluation, which breaks the monotonicity that the rest of the evaluation semantics guarantees (Proposition 7.3). The declaration is made by the investigation, not by the method, and can be withdrawn as a correction.

**Where.** Ch. 3.8, 7.7 (Definition 7.18).

---

## OD-15. Changes made outside the engineering record

Raised by OD-1/D.

**Question.** When failure analysis establishes a change within the scope that was made outside the record (for example a setting changed through a provider console), is it only a Rule 8 finding, or also an engineering change subject to Rules 1 and 3?

**Alternatives.**
- **A. Rule 8 only (recommended, current draft text).** The change set of an evaluation is defined by its declared sources and baselines (8.2). A change outside them is exposed by Rule 8 as a missing engineering-context relationship.
- **B. Also an engineering change.** Once established, the change is added to the change set; ⟨R1⟩ and ⟨R3⟩ instances are created for it and are *violated*.

**Recommendation.** A for the method, with B available as a scope policy. Under B a single unrecorded change would produce several violations for one omission, and the size of the change set would depend on what failure analyses happen to find. A team that wants out-of-band changes to count as changes can declare it in its scope.

**Where.** Ch. 7.7, 8.2, 9 (Scenario E).

---

## Non-normative decisions

- **Version number.** Retained as `0.3.0-draft` in `manifest.yaml` (review of PR #4). Choose the final number at release time.
- **Release gating.** Confirmed in the review of PR #4: the workflow publishes only on a `v*` tag that matches the manifest, or on manual dispatch (review F-33).
