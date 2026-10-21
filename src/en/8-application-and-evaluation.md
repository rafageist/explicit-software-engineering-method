# 8. Method Application and Evaluation

The rules in chapter 3 state obligations, and chapter 7 defines how they are evaluated. This chapter states what a team or an evaluator must declare so that the evaluation can be performed, reproduced and contested. It is a protocol of *declarations*, not of activities. It does not say when to evaluate, who evaluates or in which order records are produced.

Status: the evaluation contract and outcome model are proposed for 0.3 and depend on open decisions OD-6 to OD-11 where noted. They do not add obligations to rules 1-8; they make the existing ones evaluable.

## 8.1 Application, Evaluation and Process

A *method application* is the decision to hold a defined part of engineering work accountable to the method. An *evaluation* is one act of determining the outcomes of the obligations of an application against a snapshot of evidence. An application can be evaluated many times; each evaluation is a separate, versioned result.

Neither depends on a process. A team using Scrum may evaluate at each merge; a team under a plan-driven contract may evaluate at each milestone; an auditor may evaluate once, years later. The method defines what the evaluation needs, not when it happens.

## 8.2 Evaluated Scope

An evaluated scope declares:

1. **System boundary.** Which system, components or services are included. Elements outside the boundary are *out of scope*: they produce no obligation instances, and failures caused there are *external* for diagnosis (7.7).
2. **Change set.** Which engineering changes are evaluated, by baselines: for example "all changes merged into `main` between tags `v4.2.0` and `v4.3.0`", or "model revisions 18 to 25 and the code generated from them".
3. **Change unit.** What counts as one change (a commit, a merge request, a model revision, a deployment of configuration). The unit determines the subjects of Rule 1.
4. **Evidence sources.** Where records are looked for: repositories, issue trackers, decision logs, model repositories, CI systems, review tools, document stores. A record outside the declared sources does not exist for the evaluation.
5. **Completeness declarations.** For which relations and sources the evaluation claims completeness (7.5.1), for example "every CI run on `main` is in the CI system" or "all decisions of component X are in `docs/adr/`". Where no completeness is declared, absence produces *indeterminate*, not *violated*.
6. **Adoption boundary** (optional). For systems that adopt the method after years of operation, a baseline before which artifacts are *inherited*. Inherited artifacts produce obligation instances only when a change in scope modifies them or when the criticality policy classifies them as critical (chapter 9, Scenario D).

*Out of scope* and *not applicable* are different. An out-of-scope element is not evaluated. A not-applicable instance is evaluated, and the parameter set decides that the rule does not apply to it. Both must be visible in the report.

## 8.3 Parameter Set

A parameter set (7.2.4) is a versioned record bound to the application. It has two layers.

**Context descriptors** characterize the situation: domain criticality, risk tolerance, regulatory pressure, team scale, expected lifespan, and others the team finds relevant. They are inputs to policies; the rules do not read them directly.

**Policies** decide the predicates the rules use. Under OD-9, a parameter set must contain a policy for each of the following:

| Policy | Decides | Example |
|---|---|---|
| Change unit and triviality | $\mathsf{NonTrivial}$ | "A merge request is trivial if it changes only comments, formatting or test fixtures." |
| Impact and irreversibility | $\mathsf{Impactful}$, $\mathsf{Irreversible}$, $\mathsf{Balances}$ | "Impactful: affects a public API, a persisted data format, a security control or a dependency. Irreversible: data migrations without rollback." |
| Behavior-affecting artifacts | $\mathsf{AffectsBehavior}$ | "Source, configuration, schemas, infrastructure code and models used for generation." |
| Criticality | $\mathsf{Critical}$ | "Critical: anything under `payments/` or `auth/`, and any change to a regulated calculation." |
| Validation adequacy | $\mathsf{Adequate}$ | "Critical artifacts: automated tests at the affected interface plus a review by someone other than the author. Declared assumptions a critical artifact relies on are validated or covered by a compensation of the artifact's Rule 4 instance." |
| Compensation admissibility | $\mathsf{Admissible}$, $\mathsf{PermitsPermanent}$ | "Validation of dosage calculations is not compensable. Permanent acceptance is not permitted for critical artifacts." |
| Risk-acceptance authority | $\mathsf{MayAccept}$ | "Risks on critical artifacts: the service owner or, during a declared incident, the incident commander. Never the change author alone." |

A policy is a criterion, not necessarily a threshold, and it may require judgment. When it does, the judgment is recorded as an assessment with its author (7.6). Policies may be strict or permissive. The method does not decide how strict a context should be; it requires that the strictness be declared, so that it can be evaluated and questioned.

Changing a parameter set produces a new version. Evaluations state which version they used. A parameter set changed in order to make a past evaluation pass is visible as such, because the old version and the old evaluation remain.

## 8.4 Evidence and Provenance

### 8.4.1 Minimum Content of a Record

Each record used as evidence has an identifier, a type (intent, decision, assumption, trade-off, validation, compensation, assessment), content or a reference to it, the version or digest of what it refers to, a responsible agent, the time it was recorded, its provenance and its source. The method does not prescribe a format: a pull-request description, an architecture decision record, a ticket, a model element or a database row can all be records if they carry this information.

### 8.4.2 Provenance

*Proposed interpretation (OD-8).* Records carry one of four provenance kinds. The distinction is compatible with general provenance models such as W3C PROV [Moreau and Missier 2013], which the method does not require.

| Provenance | Meaning | Satisfies obligations |
|---|---|---|
| contemporaneous | recorded while the work was done | yes |
| retrospective | recorded later by a person responsible for the work, from their own knowledge | yes |
| reconstructed | historical rationale recovered from evidence (history, tickets, interviews) and confirmed by a responsible person | yes, prospectively; never presented as original rationale |
| inferred | proposed by analysis or tooling (including language models) and not confirmed | no; at most turns *violated* into *indeterminate* |

The method does not fabricate history and does not let tools do it. An inferred link may be a good hypothesis, but until a responsible person confirms it, it does not have the authority of a recorded decision. The difference between *retrospective* and *reconstructed* matters. The first is the author's own account; the second is an interpretation of traces, and it can be wrong.

### 8.4.3 Accessibility

A record that is referenced but cannot be read by the evaluator (permissions, deleted storage, an external system) is *inaccessible*. Formulas that depend on its content evaluate to *unknown* (7.5.2). Inaccessibility is reported with the reference, so that someone with access can resolve it. Evaluators MUST NOT assume that inaccessible evidence would have been favorable or unfavorable.

### 8.4.4 Navigability

A link is navigable in both directions (Rule 3) when it can be resolved from each end using the declared sources. A commit message citing a ticket is navigable from the commit. It is navigable from the ticket if the repository is a declared source and can be searched for the ticket identifier, or if the ticket links back. A link that exists only in a person's memory, or in a source outside the evaluation, is not navigable.

### 8.4.5 Missing Evidence Is Not Evidence of Absence

When the scope is incomplete, absent evidence does not prove that work was not done. The evaluation decides between *violated* and *indeterminate* only through its completeness declarations. Declaring completeness is a responsibility: a declaration later found false invalidates the outcomes that depended on it (Proposition 7.3).

## 8.5 Compensation Lifecycle

A compensation records an accountable deviation. Its life has the following states:

| State | Meaning |
|---|---|
| recorded | the compensation exists with its required content |
| accepted | an agent authorized by the authority policy has accepted the stated risk |
| active | accepted and unexpired; the referenced instance is *compensated* |
| remediated | the missing work was done; the instance becomes *satisfied* for the versions the remediation covers, and the compensation is closed |
| expired | the review condition was reached while the subject was still in operation, without remediation or renewal; the instance is no longer *compensated* and becomes *violated* (or *indeterminate*, if the requirement cannot be decided) |
| renewed | a new compensation, with a new acceptance, supersedes the expired one |
| withdrawn | the deviation was reverted (for example the change was rolled back) |

**Required content.** Reference to the obligation instance (rule and subject version). Statement of accepted risk (what can go wrong, how likely, with what consequence, as far as known). Accepting agent and time of acceptance. Review condition: a date or an event *(proposed, OD-6)*. Remediation plan (SHOULD).

**History.** Compensations are never edited in place or deleted. A renewed or corrected compensation supersedes the previous one, and both remain in the record. This history is what allows a later evaluation or diagnosis to establish what risk was accepted, by whom and when.

**Retroactive compensations.** A compensation recorded after the exposure it covers is flagged as retroactive *(proposed, OD-6)*. It counts from the time it is recorded. It cannot show that a failure before that time realized an accepted risk.

## 8.6 Evaluation Contract

An evaluation is reproducible only if its inputs are fixed (Definition 7.16). The *evaluation contract* is the record of those inputs and of the results.

| Field | Content |
|---|---|
| Method and ruleset version | e.g. ESEM 0.3.0, ruleset with the open decisions resolved or the proposed interpretations applied (listed) |
| Evaluated scope | system boundary, change set by baselines, change unit, adoption boundary |
| Parameter set | identifier and version |
| Evidence sources | each source with immutable references (commit hashes, revision identifiers, content digests) |
| Completeness declarations | per relation and source |
| Evaluation time | the instant $t$ used for compensation validity |
| Judgments | assessments used, with author and date |
| Obligation instances | rule, subject, applicability |
| Outcomes | per instance, with diagnostic explanation and evidence references |
| Trace paths | for Rule 3 instances, the path found, or the point where it breaks |
| Compensations | referenced instances, validity, state, retroactivity |
| Notes | recommendations not followed, inaccessible evidence |
| Verdict and profile | aggregate verdict and counts per outcome (8.7) |
| Evaluator | who performed the evaluation, with which tools if any |

An illustrative serialization (non-normative; any format with the same content is valid):

```yaml
evaluation:
  method: ESEM 0.3.0
  ruleset: {version: 0.3.0, interpretations: [OD-1/D, OD-2/B, OD-5/D, OD-6/A1+B1]}
  scope:
    boundary: [orders-api, payment-adapter]
    change_set: {repo: git@example.org:shop/orders.git, from: v4.2.0, to: v4.3.0}
    change_unit: merge-request
  parameters: {id: PS-shop, version: 7}
  sources:
    - {id: repo, ref: 9f2c1e0}
    - {id: tracker, ref: "export 2026-10-20T09:00Z sha256:3b1d..."}
    - {id: ci, ref: "runs on main, 2026-09-01..2026-10-20"}
  completeness:
    - {relation: validates, source: ci, part: "main branch"}
  time: 2026-10-21T10:00Z
  judgments: [{id: J-12, author: m.ortiz, on: D-31, about: Impactful}]
  outcomes:
    - {instance: [R4, payment-adapter@a41b2c], outcome: compensated, by: C-9,
       explanation: "no adequate validation of a41b2c; C-9 valid until 2026-10-24"}
    - {instance: [R3, orders-api/retry.yaml@9f2c1e0], outcome: satisfied,
       path: [retry.yaml, D-31, I-14]}
  verdict: compliant-with-compensations
  profile: {satisfied: 41, compensated: 1, violated: 0, not_applicable: 12, indeterminate: 0}
```

**Method versions and earlier evaluations** *(proposed, OD-11)*. An evaluation is bound to its ruleset version and is never changed by a later method version. Re-evaluating under a new version produces a new contract, and comparisons must state both versions. Method versions follow `MAJOR.MINOR.PATCH`. A MAJOR change can turn earlier *satisfied* or *not applicable* outcomes into *violated*. A MINOR change can only resolve *indeterminate* outcomes or add non-normative material. A PATCH is editorial. Below 1.0, MINOR versions may contain normative changes, which the change log must list.

## 8.7 Reporting Outcomes

Each obligation instance is reported with its outcome and an explanation that names what decided it: applicability (which policy, which judgment), the requirement (which records, or which absence under which completeness declaration) and the compensation (which record, and why it is valid or invalid). An outcome without an explanation cannot be contested, and an evaluation that cannot be contested is not accountable.

The aggregate verdict (Definition 7.15) is reported together with the full profile of outcomes. A summary that hides compensated or indeterminate instances behind "compliant" misrepresents the evaluation.

An evaluation MUST NOT claim:

- that the system is correct, safe or fit for purpose. The method evaluates the engineering record, not the product's behavior;
- that work was not done, where it only lacks evidence of it under declared completeness;
- completeness of failure diagnosis (7.7, *Limits*);
- objectivity beyond its declared inputs. Where policies required judgment, the judgments are part of the result.

## 8.8 Evaluation Points

The method does not prescribe evaluation points. Common choices are: before merging a change, before a release, periodically for audit, and after a failure. Evaluating early finds missing records while the people who can write them still remember. Evaluating late measures what actually survived. A team may combine them. In every case the evaluation uses the contract above, so results from different points are comparable.

## 8.9 Tooling Independence

An evaluation can be performed by hand, with a spreadsheet, with queries over repositories, or with a dedicated evaluator. The method depends on none of them. A tool that implements the method must:

- expose the evaluation contract and the explanation of each outcome;
- keep the method version, parameter set and evidence references immutable for a given evaluation;
- keep inferred links distinct from recorded ones;
- leave manual review possible.

Divengine Studio may provide an optional evaluator for this method. The method is defined independently of it and of any other platform, and its vocabulary does not depend on how any tool stores context (chapter 10).
