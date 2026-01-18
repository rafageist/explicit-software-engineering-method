The Explicit Software Engineering Method is a prescriptive set of rules that defines what engineering work must be made explicit, how artifacts must relate to intent and decisions, and how absences must be compensated, in order for software to qualify as an engineered product rather than incidental functionality. It operates orthogonally to process frameworks by constraining what must be traceable and validated regardless of workflow sequence, accepting contextual parameters that shape the required level of explicitness without imposing a fixed lifecycle. The method transforms failure from narrative into evidence-based diagnosis by making intent, decisions, assumptions, trade-offs, and validation explicit and navigable, enabling systematic quality assessment and cumulative learning. By defining obligations and their consequences rather than activities, the method ensures that engineering reasoning is preserved as analyzable infrastructure across any development process. It exists to bridge the gap between software as executable output and software product as accountable engineering outcome.

This definition is normative.

# Explicit Software Engineering Method

## 1. Overview
The Explicit Software Engineering Method defines a minimal, executable set of rules for making engineering intent, decisions, and trade-offs explicit and traceable across the software lifecycle.
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
- Compensation: explicit documentation of missing artifacts or validations with stated accepted risk.

## 6. Method as Infrastructure
The method treats engineering as infrastructure: it defines enforceable rules about what must be explicit, how artifacts relate, and how gaps are compensated.
Because the rules are explicit, the method supports systematic checks, compensations, and analysis of engineering quality and risk.

## 7. Parameters and Balance
The method accepts contextual parameters (domain criticality, risk tolerance, regulatory demands, team scale) that shape how much explicitness is required.
Explicitness, effort, and risk are balanced rather than maximized; quality is optimized for context, not for maximal rigor.

## 8. Relationship to Standards
The method is compatible with IEEE and ISO software engineering process standards.
Standards define required activities and work products; this method defines how those activities and products become explicit, traceable, and analyzable in execution.
Process frameworks can host the method, but the method specifies the rules that make execution verifiable.

## 9. Expected Outcomes
- Improves: clarity of intent, consistency of artifacts, objective assessment of engineering quality, and reuse of knowledge across projects.
- Diagnosable failures: missing assumptions, invalid decisions, unvalidated artifacts, and unbalanced trade-offs become observable causes rather than after-the-fact narratives.
- Newly visible: rationale, risk exposure, and the actual cost of shortcuts that were previously implicit.

## 10. Scope and Evolution
The current scope defines the minimal concepts, explicitness rules, and traceability needed to make engineering work analyzable.
The method is intentionally minimal at this stage and does not prescribe a full lifecycle model.
Tooling (for example, Divengine Studio) is an implementation of the method, not the method itself.

## 11. Normative Core Rules (Draft)
See `src/en/3-normative-rules.md` (English) and `src/es/3-reglas-normativas.md` (Spanish copy).
