# Glossary

::: glossary

- **Applicability.** The condition under which a rule applies to a subject. It is decided by a policy of the parameter set (7.3).
- **Artifact.** A produced, versioned and inspectable work product. Artifacts that affect system behavior, as decided by the behavior-affecting policy, must be traceable to intent or decisions (Rule 3). Engineering records (intents, decisions, assumptions, validations, compensations) are typed by their role, not counted as artifacts.
- **Assumption.** A statement treated as true for reasoning or planning when evidence is missing or deferred, and that must remain identifiable until validated or invalidated.
- **Causal Factor.** A condition that a causal analysis of a failure identifies as contributing to it. Its status is *established* or *provisional*. Only established factors whose place in the system is known can be related to the engineering record; the others leave the diagnosis indeterminate (7.7).
- **Compensation.** An explicit and auditable acceptance of risk for an unmet obligation instance, accepted by an authorized party and subject to a review condition. It does not remove the underlying obligation: the outcome is *compensated*, not *satisfied*.
- **Context Engineering.** The deliberate construction, selection, preservation and delivery of relevant context to a person or system that needs it to act. Distinct from the method (chapter 10).
- **Contextual Parameters.** The declared, versioned parameter set of a method application: context descriptors and the policies that decide the predicates the rules use.
- **Decision.** A committed engineering choice among alternatives, made explicit and linked to the intent it serves.
- **Diagnosability.** The ability to relate the causal factors of a failure to the engineering record: as gaps, accepted risks, parameter misclassifications, external factors, or factors the record cannot explain.
- **Engineering Change.** A modification of behavior-affecting artifacts within the evaluated scope, identified by a version delta. The change unit is declared by the method application.
- **Engineering Context.** The knowledge, constraints and circumstances in which engineering occurs and which explain a solution, whether explicit or tacit (chapter 10).
- **Engineering Record.** The intents, decisions, assumptions, trade-offs, validations, compensations and links that exist in the declared evidence sources.
- **Evaluated Scope.** The system boundary, change set, change unit, evidence sources and completeness declarations of a method application (8.2).
- **Evaluation.** One act of determining the outcomes of the obligation instances of a method application against a snapshot of evidence.
- **Evaluation Contract.** The record of an evaluation's inputs (method and ruleset version, scope, parameter set, evidence references, evaluation time, judgments) and results (8.6).
- **Evidence Completeness.** A declaration that, for a relation and part of the scope, every true instance is present in the evidence sources. Only under such a declaration does absent evidence count as absence (7.5.1).
- **Explicit.** Engineering reasoning captured as traceable records rather than remaining undocumented or tacit.
- **Explicitness.** The property of engineering work being made explicit in a form that is traceable, evaluable and diagnosable.
- **Failure.** An observed deviation from intended or required behavior or constraints that can be analyzed against explicit engineering reasoning.
- **Indeterminate.** The outcome of an obligation instance when the available evidence does not decide it. It is neither a violation nor compliance.
- **Intent.** The desired outcome, property or constraint that a change or system must satisfy, with a defined scope.
- **Method.** A prescriptive set of obligations and constraints over engineering records and relationships that can be parameterized and evaluated, and that is independent of workflow order.
- **Method Application.** The use of the method on a declared evaluated scope with a declared parameter set, such that compliance and diagnosability can be evaluated.
- **Normative Rule.** A statement of obligation that defines what must be explicit and the consequences of omission.
- **Obligation Instance.** A rule applied to one subject, written ⟨rule, subject⟩. Evaluation assigns one outcome to each instance.
- **Orthogonality.** Independence from workflow order or lifecycle sequence while maintaining fixed engineering obligations.
- **Outcome.** One of *satisfied*, *violated*, *compensated*, *not applicable* or *indeterminate*.
- **Policy.** A criterion in the parameter set that decides a parameter-dependent predicate, such as triviality, impact, criticality, validation adequacy, compensation admissibility or risk-acceptance authority.
- **Process.** An ordered sequence of activities or phases used to organize work, which may embed a method but does not define engineering obligations by itself.
- **Provenance.** How a record came to exist: contemporaneous, retrospective, reconstructed or inferred (8.4.2).
- **Risk-Acceptance Authority.** The party that the parameter set allows to accept a given kind of risk through a compensation.
- **Software.** Executable code, configurations and data that produce system behavior.
- **Software Product.** Software whose behavior, constraints and purpose are accountable through explicit intent, decisions, validation and traceability.
- **Trade-off.** A deliberate balance between competing constraints or quality attributes, accepted as part of a decision.
- **Traceability.** Explicit and navigable links among intents, decisions, assumptions, artifacts and validations that allow reasoning to be inspected and evaluated.
- **Validation.** Explicit evidence that an artifact or decision satisfies its stated intent under the declared context. It includes what ISO/IEC/IEEE terminology distinguishes as verification and validation (4.1).

:::
