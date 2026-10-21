The Explicit Software Engineering Method is a prescriptive set of rules that defines what engineering work must be made explicit, how artifacts must relate to intent and decisions, and how absences must be compensated, in order for software to qualify as an engineered product rather than incidental functionality. It operates orthogonally to process frameworks by constraining what must be traceable and validated regardless of workflow sequence, accepting contextual parameters that shape the required level of explicitness without imposing a fixed lifecycle. The method transforms failure from narrative into evidence-based diagnosis by making intent, decisions, assumptions, trade-offs, and validation explicit and navigable, enabling systematic quality assessment and cumulative learning. By defining obligations and their consequences rather than activities, the method ensures that engineering reasoning is preserved as analyzable infrastructure across any development process. It exists to bridge the gap between software as executable output and software product as accountable engineering outcome.

This definition is normative.

# Explicit Software Engineering Method

## 1. Overview
The Explicit Software Engineering Method defines a minimal, evaluable set of rules for making engineering intent, decisions, and trade-offs explicit and traceable across the software lifecycle.
It addresses a structural problem: critical engineering work often remains implicit, leaving quality, accountability, and learning dependent on tacit knowledge rather than evidence.
Implicitness is structural because delivery pressure and tooling defaults reward output over explicit reasoning, so implicit work accumulates unless a method enforces explicitness.

## 2. What This Is Not
- Not a project management framework
- Not a development methodology
- Not a rigid process
- Not a replacement for existing tools

## 3. Method vs Methodology vs Process
- Method: a prescriptive, executable way of working defined by explicit artifacts, rules, and constraints; it is parameterizable and analyzable.
- Methodology: the study and justification of methods; it explains why methods are chosen and under which assumptions they hold.
- Process: an ordered sequence of activities or phases; it can be implemented by, or combined with, a method.

This work is a method because it defines explicit artifacts and relationships that can be instantiated, checked, and analyzed, while remaining adaptable through parameters.

## 4. Core Principle: Explicit vs Implicit Engineering
Implicit engineering work is real work that remains undocumented or unstructured: decisions, assumptions, and trade-offs exist but are not recorded as artifacts.
Explicit engineering work captures those elements as traceable artifacts with stated intent and validation.
Explicitness enables quality, traceability, and learning because the work can be inspected, validated, and improved with evidence instead of memory.

## 5. Core Concepts
- Intent: the desired outcome or property a system or change must achieve, with stated scope.
- Artifact: a produced, versioned work product that can be inspected and validated.
- Decision: a committed choice among alternatives with rationale and consequences.
- Assumption: a statement treated as true for reasoning or planning until validated or disproven.
- Trade-off: a deliberate balance between competing constraints or quality attributes.
- Validation: evidence that an artifact or decision satisfies its stated intent.
- Traceability: explicit, navigable links among intents, decisions, assumptions, artifacts, and validations.
- Compensation: explicit, authorized acceptance of the risk of an unmet obligation; it does not remove the obligation.
- Obligation instance: a rule applied to one subject; evaluation gives it one outcome: satisfied, violated, compensated, not applicable or indeterminate.

## 6. Method as Infrastructure
The method treats engineering as infrastructure: it defines enforceable rules about what must be explicit, how artifacts relate, and how gaps are compensated.
Because the rules are explicit, the method supports systematic checks, compensations, and analysis of engineering quality and risk.

## 7. Parameters and Balance
The method accepts contextual parameters (domain criticality, risk tolerance, regulatory demands, team scale) that shape how much explicitness is required.
Explicitness, effort, and risk are balanced rather than maximized; quality is optimized for context, not for maximal rigor.

## 8. Relationship to Standards
The method is designed to operate within IEEE and ISO software engineering standards. Several of them already ask for recorded decisions, rationale, traceability and risk acceptance (for example ISO/IEC/IEEE 12207, 15288, 42010, 29148, IEEE 1012). The method adds an evaluation of the resulting record that is independent of the process that produced it, explicit semantics for compensation and missing evidence, and a defined relation between failure and the record. It is not a conformity assessment scheme. See chapter 4.

## 9. Expected Outcomes
These are expected outcomes that follow from the method's hypothesis (chapter 0); they have not been demonstrated empirically.
- Improves: clarity of intent, consistency of artifacts, evidence-based assessment of engineering quality against a declared context, and reuse of knowledge across projects.
- Diagnosable failures: causal factors identified by failure analysis can be related to the engineering record, as missing intent, unrecorded decisions, unvalidated artifacts, false assumptions or unbalanced trade-offs, or as external factors the record does not need to explain.
- Newly visible: rationale, risk exposure, and the actual cost of shortcuts that were previously implicit.

## 10. Scope and Evolution
The current scope defines the minimal concepts, explicitness rules, and traceability needed to make engineering work analyzable.
The method is intentionally minimal at this stage and does not prescribe a full lifecycle model.
Tooling (for example, Divengine Studio) may implement an evaluator of the method; it is not the method itself, and the method does not depend on it.

## 11. Normative Core Rules (Draft)
See `src/en/3-normative-rules.md` (English) and `src/es/3-reglas-normativas.md` (Spanish edition). The formal semantics are in chapter 7, the evaluation contract in chapter 8 and worked examples in chapter 9.

## 12. Status of Version 0.3 (Draft)
Version 0.3 keeps the eight rules of 0.2.1 unchanged and makes them evaluable: applicability through declared policies, evaluation under incomplete evidence, compensation that never erases an obligation, and versioned, reproducible evaluations. Interpretations that would change the meaning of a rule are labeled *Proposed interpretation (OD-n)* and are pending maintainer decision:

- `docs/review-0.2.1.md`: review of 0.2.1 and its inconsistencies.
- `docs/open-decisions.md`: open normative decisions, with alternatives and recommendations.
- `CHANGELOG.md`: changes by kind (normative, clarifying, editorial).

## 13. Repository and Build
- `src/en`, `src/es`: the English and Spanish editions. Both express the same normative content; `make check` verifies structure and formulas.
- `scripts/build_pdf.py`: PDF build (pandoc, XeLaTeX, wkhtmltopdf, Mermaid CLI). `make tex` produces LaTeX only.
- `Dockerfile`, `make docker-pdf`: the CI toolchain, for reproducible local builds.
- Releases are published only from a `v*` tag that matches `manifest.yaml`; see `docs/release-checklist.md`.
