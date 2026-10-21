# 7. Formalization Sketch - Explicit Software Engineering Method

This chapter provides a mathematical and logical formalization of the method.
It is intentionally minimal and focuses on: (1) entities, (2) relations, (3) normative obligations, (4) evaluation under incomplete evidence, and (5) diagnosability.
It describes constraints over explicit records and relations, not a prescriptive workflow.
The goal is evaluability and diagnosability, not mathematical completeness.

The formalization aims for **operational objectivity under explicit context**, not absolute objectivity. Two evaluators who use the same method version, evaluated scope, parameter set, evidence snapshot, evaluation time and recorded judgments obtain the same outcomes (7.6). Different contexts, or different judgments where a policy requires judgment, can legitimately lead to different outcomes.

---

## 7.0 Status of Statements

Statements in this chapter are labeled by status:

- **Definition.** Part of the formal semantics of the method. Definitions marked *(proposed, OD-n)* depend on an open decision (`docs/open-decisions.md`).
- **Proposition.** A property that follows from the definitions. Arguments are given informally; they are not machine-checked proofs.
- **Sketch.** A conceptual direction that is not part of the evaluation semantics.
- **Example.** Illustrative only.

Version 0.2.1 of this chapter contained invariants that, read literally, made compensated states indistinguishable from satisfied ones and treated missing evidence as proof of absence. Section 7.3.9 lists every change against 0.2.1 and the reason for it.

---

Before stating obligations, we must fix a universe of discourse. Without a declared universe, constraints have no stable targets and evaluation becomes ambiguous.

## 7.1 Universe of Discourse

We model engineering work as a set of entities and typed relations.

### 7.1.1 Entity Sets

**Definition 7.1 (entity sets).** Let the following finite sets exist:

- $I$: *Intents*
- $D$: *Decisions*
- $A$: *Artifact versions*
- $S$: *Assumptions* (premises relied upon)
- $T$: *Trade-offs*
- $V$: *Validations*
- $C$: *Compensations*
- $Ch$: *Changes* (engineering changes)
- $P$: *Parameters* (context descriptors and policies)
- $G$: *Agents* (persons or roles that record, assess or accept)
- $F$: *Failures* (observed failures)

and the global entity set $E = I \cup D \cup A \cup S \cup T \cup V \cup C \cup Ch \cup P \cup G \cup F$.

The sets are pairwise disjoint. Entities are typed by the role they play in engineering reasoning, not by how they are stored. A decision written in a Markdown file is an element of $D$, not of $A$.

Elements of $A$ are *versions*: a source file at two commits gives two elements of $A$. The relation $\mathsf{supersedes} \subseteq A \times A$ links a version to its predecessor.

$D$ contains recorded decisions and also choices identified by review or failure analysis for which no record exists. The predicate $\mathsf{Recorded}(d)$ distinguishes them. Likewise, $S$ contains declared assumptions and premises identified as relied upon without declaration; $\mathsf{Declared}(s)$ distinguishes them. Unrecorded elements are what the evaluation of Rules 2 and 5 is about (review F-03, F-09).

### 7.1.2 Predicates (Typing)

We use unary predicates to type entities: $\mathsf{Intent}(x)$, $\mathsf{Decision}(x)$, $\mathsf{Artifact}(x)$, $\mathsf{Assumption}(x)$, $\mathsf{TradeOff}(x)$, $\mathsf{Validation}(x)$, $\mathsf{Compensation}(x)$, $\mathsf{Change}(x)$, $\mathsf{Parameter}(x)$, $\mathsf{Agent}(x)$, $\mathsf{Failure}(x)$. When a variable is named after a set (for example $ch$, $d$, $a$), its type is implied and the typing predicate is omitted.

### 7.1.3 Record Attributes

**Definition 7.2 (record attributes).** Every element $x \in E$ that is a record has:

- $\mathrm{src}(x)$: the evidence source that holds it;
- $\tau(x)$: the time it was recorded;
- $\mathrm{prov}(x) \in \{\textit{contemporaneous}, \textit{retrospective}, \textit{reconstructed}, \textit{inferred}\}$: its provenance (8.4);
- $\mathrm{acc}(x) \in \{\textit{accessible}, \textit{inaccessible}\}$: whether the evaluator can read its content.

---

Engineering reasoning is captured by relationships among these entities, not by an imposed sequence. A graph model makes traceability explicit without prescribing order.

## 7.2 Core Relations (Graph Model)

Engineering reasoning is represented as a typed directed multigraph over $E$.

### 7.2.1 Fundamental Relations

**Definition 7.3 (relations).**

| Relation | Signature | Reading |
|---|---|---|
| $\mathsf{declares}(ch, i)$ | $Ch \times I$ | change $ch$ declares intent $i$ |
| $\mathsf{modifies}(ch, a)$ | $Ch \times A$ | change $ch$ produces artifact version $a$ |
| $\mathsf{serves}(d, i)$ | $D \times I$ | decision $d$ serves intent $i$ |
| $\mathsf{justifies}(a, x)$ | $A \times (I \cup D)$ | artifact $a$ is justified by intent or decision $x$ |
| $\mathsf{derivedFrom}(a, b)$ | $A \times A$ | $a$ is generated or derived from $b$ (e.g. code from a model) |
| $\mathsf{assumes}(x, s)$ | $(D \cup A) \times S$ | $x$ is recorded as relying on assumption $s$ |
| $\mathsf{relies}(x, s)$ | $(D \cup A) \times S$ | $x$ relies on $s$, as established by review or analysis |
| $\mathsf{tradesOff}(x, t)$ | $(D \cup A) \times T$ | $x$ involves trade-off $t$ |
| $\mathsf{validates}(v, x)$ | $V \times (A \cup D \cup I)$ | validation $v$ provides evidence for $x$ |
| $\mathsf{equiv}(a, b)$ | $A \times A$ | the record declares $b$ equivalent to $a$ for validation purposes |
| $\mathsf{compensates}(c, o)$ | $C \times O$ | compensation $c$ covers obligation instance $o$ (7.2.3) |
| $\mathsf{acceptedBy}(c, g)$ | $C \times G$ | agent $g$ accepted the risk stated in $c$ |

Version 0.2.1 had $\mathsf{compensates} \subseteq C \times (I \cup D \cup A \cup V)$, which requires the missing element to exist in order to be compensated (review F-10). Compensations now target obligation instances. The 0.2.1 relation $\mathsf{paramOf} \subseteq P \times Ch$ is replaced by binding a parameter set to the method application (7.2.4).

$\mathsf{assumes}$ is part of the record; $\mathsf{relies}$ is a finding. The difference between them is what Rule 5 evaluates.

### 7.2.2 Traceability (Derived)

**Definition 7.4 (justification paths).** Let $x \to_J y$ hold iff $\mathsf{justifies}(x,y) \lor \mathsf{serves}(x,y) \lor \mathsf{derivedFrom}(x,y)$. Then $\mathsf{traceableTo}$ is the reflexive-transitive closure $\to_J^{*}$.

Only justification edges are used for Rule 3: an artifact is not *justified* by the test that validates it or by the assumption it relies on. The full trace graph also includes $\mathsf{declares}$, $\mathsf{modifies}$, $\mathsf{validates}$, $\mathsf{assumes}$ and $\mathsf{tradesOff}$ edges and is used for navigation and diagnosis (7.7).

**Proposition 7.1.** $\mathsf{traceableTo}$ is not definable in first-order logic over the relations above, because transitive closure is not first-order definable [Aho and Ullman 1979]. The rules therefore use first-order logic extended with a transitive-closure operator (equivalently, a recursive query). Evaluation over a finite record remains polynomial in its size. Version 0.2.1 defined the path relation but did not use it (review F-05).

**Bidirectional navigability.** Any relation in the model can be read in both directions, so the requirement in Rule 3 is not a property of the graph. It constrains the representation: $\mathsf{Navigable}(x, y)$ holds when, using only the declared evidence sources, the link can be resolved starting from $x$ and starting from $y$ (8.4).

### 7.2.3 Obligation Instances

**Definition 7.5 (subjects and instances).** The rules $\mathcal{R} = \{R1, \dots, R8\}$ of ruleset version $\rho$ have subject domains:

| Rule | Subject domain |
|---|---|
| R1 | $Ch$ |
| R2 | $D$ |
| R3 | $A$ |
| R4 | $A \cup D$ (OD-12) |
| R5 | $S$ |
| R7 | $\{\alpha\}$, the method application |
| R8 | $F$ |

The set of obligation instances is $O = \{\langle k, x \rangle \mid k \in \mathcal{R},\ k \ne R6,\ x \in \mathrm{Subj}_k \cap \mathrm{scope}(\alpha)\}$. Rule 6 has no subjects of its own; it is a rule over the outcomes of other instances (7.4).

### 7.2.4 Parameters as Interpretations

**Definition 7.6 (policy predicates).** The rules use a fixed set of *policy predicates*:

$$\begin{aligned}\mathcal{P}_{pol} = \{&\mathsf{NonTrivial},\ \mathsf{Impactful},\ \mathsf{Irreversible},\ \mathsf{Balances},\ \mathsf{AffectsBehavior},\\ &\mathsf{Critical},\ \mathsf{Adequate},\ \mathsf{Admissible},\ \mathsf{MayAccept},\ \mathsf{PermitsPermanent}\}\end{aligned}$$

A parameter set $\Pi = (\Delta, \Lambda)$ consists of context descriptors $\Delta$ (domain criticality, risk tolerance, regulatory pressure, team scale, expected lifespan, ...) and policies $\Lambda$. Each policy gives an interpretation of one or more policy predicates. An interpretation may be *partial*: a policy can leave cases undecided, and a missing policy leaves its predicate undecided everywhere.

This is how the method can be context-dependent without having context-dependent rules. The formulas of the rules are fixed for a ruleset version; the parameter set fixes what the policy predicates mean in a context. Two applications with different parameter sets evaluate the same formulas under different interpretations.

A policy may be mechanical (for example, "an artifact is critical iff it is under `payments/`") or may require judgment (for example, "a decision is impactful if it constrains a public interface"). A judgment is recorded as an *assessment*, with its author and the record it concerns, and becomes an input of the evaluation (7.6). An evaluation never re-judges silently.

---

First-order logic is used here to express invariants over the graph. These are constraints to be evaluated, not computations to be executed.

## 7.3 Rules as Applicability and Requirement

The method is expressed as constraints that must hold regardless of workflow sequencing, reflecting orthogonality to process order. These constraints correspond directly to the normative rules of chapter 3.

**Definition 7.7 (rule form).** Each rule $k \in \mathcal{R}$ other than R6 and R8 is a pair of formulas with one free variable $x$ for its subject: an *applicability condition* $\mathrm{App}_k(x)$ and a *requirement* $\mathrm{Req}_k(x)$. The 0.2.1 invariant for rule $k$ corresponds to

$$\forall x\ (\mathrm{App}_k(x) \rightarrow \mathrm{Req}_k(x))$$

with the compensation disjunct removed. Compensation is handled by the outcome function (7.5), so that it can never make a requirement true (review F-15).

### 7.3.1 Rule 1 - Intent Declaration

$$\mathrm{App}_1(ch) \equiv \mathsf{NonTrivial}(ch) \qquad \mathrm{Req}_1(ch) \equiv \exists i\ (\mathsf{declares}(ch, i) \land \mathsf{Scoped}(i))$$

$\mathsf{Scoped}(i)$ holds when the intent record states the part of the system, the stakeholders or the quality attribute concerned. The 0.2.1 consequence $\mathsf{ImplicitWork}(ch)$ is the name of the case $\mathrm{App}_1(ch) \land \lnot \mathrm{Req}_1(ch)$.

### 7.3.2 Rule 2 - Decision Explicitness

$$\mathrm{App}_2(d) \equiv \mathsf{Impactful}(d) \lor \mathsf{Irreversible}(d)$$

$$\mathrm{Req}_2(d) \equiv \mathsf{Recorded}(d) \land \exists i\ \mathsf{serves}(d, i) \land \mathsf{AltsRecorded}(d) \land (\mathsf{Balances}(d) \rightarrow \exists t\ \mathsf{tradesOff}(d, t))$$

$\mathsf{AltsRecorded}(d)$ holds when the record lists the alternatives considered or states that none were evaluated and why *(proposed, OD-3)*. The last conjunct *(proposed, OD-4)* requires the accepted trade-off when the decision balances competing attributes; without OD-4 it is omitted.

For an unrecorded decision, $\mathrm{Req}_2(d)$ is false. Treating it "as an assumption by default" is a classification used in diagnosis (7.7), not a way to satisfy $\mathrm{Req}_2$ *(proposed, OD-2)*.

### 7.3.3 Rule 3 - Artifact Traceability

$$\mathrm{App}_3(a) \equiv \mathsf{AffectsBehavior}(a)$$

$$\mathrm{Req}_3(a) \equiv \exists y\ \big((\mathsf{Intent}(y) \lor \mathsf{Decision}(y)) \land \mathsf{Recorded}(y) \land \mathsf{traceableTo}(a, y) \land \mathsf{Navigable}(a, y)\big)$$

The 0.2.1 consequence $\mathsf{Orphan}(a)$ is the name of the case $\mathrm{App}_3(a) \land \lnot \mathrm{Req}_3(a)$.

### 7.3.4 Rule 4 - Validation Requirement

$$\mathrm{App}_4(x) \equiv \mathsf{Critical}(x)$$

$$\mathrm{Req}_4(x) \equiv \exists v\ \exists x'\ \big(\mathsf{validates}(v, x') \land (x' = x \lor \mathsf{equiv}(x', x)) \land \mathsf{Passed}(v) \land \mathsf{Adequate}(v, x)\big)$$

Three conditions are new with respect to 0.2.1 (review F-08). Validation is bound to a version, because elements of $A$ are versions. The validation must have passed: a failing test run is evidence, but not evidence that $x$ satisfies its intent. Adequacy is decided by the validation-adequacy policy, which makes the "validation depth" of Rule 7 operative.

### 7.3.5 Rule 5 - Assumption Declaration

$$\mathrm{App}_5(s) \equiv \exists x\ \mathsf{relies}(x, s) \land \lnot \exists v\ (\mathsf{validates}(v, s) \land \mathsf{Passed}(v))$$

$$\mathrm{Req}_5(s) \equiv \mathsf{Declared}(s) \land \forall x\ (\mathsf{relies}(x, s) \rightarrow \mathsf{assumes}(x, s))$$

The 0.2.1 formula $\forall x\ (\mathsf{EvidenceMissing}(x) \rightarrow \exists s\ \mathsf{assumes}(x,s))$ quantified over all entities and could not tell a declared premise from an undeclared one (review F-09). The SHOULD on tracking is a recommendation (7.4): an assumption whose status is not tracked is reported but is not a violation.

### 7.3.6 Rule 6 - Explicit Compensation

Rule 6 has no subject of its own. It is the contrary-to-duty obligation attached to the other rules (7.4.2), and its effect is defined by the validity of compensations and the outcome function (7.5).

### 7.3.7 Rule 7 - Parameter Awareness

$$\mathrm{App}_7(\alpha) \equiv \top \qquad \mathrm{Req}_7(\alpha) \equiv \mathsf{Explicit}(\Pi_\alpha) \land \mathsf{Versioned}(\Pi_\alpha) \land \mathsf{Covers}(\Pi_\alpha, \mathcal{P}_{pol})$$

$\mathsf{Covers}$ *(proposed, OD-9)* requires a policy for every policy predicate. Without OD-9, the last conjunct is omitted. The 0.2.1 formula $\forall ch\ \exists p\ \mathsf{paramOf}(p, ch)$ was satisfied by any single parameter (review F-12).

### 7.3.8 Rule 8 - Diagnosability of Failure

Rule 8 is evaluated per failure and depends on the classification defined in 7.7.

### 7.3.9 Rule-to-Predicate Matrix and Changes from 0.2.1

| Rule | Subject | $\mathrm{App}_k$ (policy) | $\mathrm{Req}_k$ | Compensable (OD-5) | Change from 0.2.1 |
|---|---|---|---|---|---|
| R1 | $ch \in Ch$ | $\mathsf{NonTrivial}$ | scoped intent declared | no | applicability tied to policy |
| R2 | $d \in D$ | $\mathsf{Impactful} \lor \mathsf{Irreversible}$ | recorded, serves intent, alternatives, trade-off | yes | irreversibility, alternatives and trade-off added; compensation moved out of formula |
| R3 | $a \in A$ | $\mathsf{AffectsBehavior}$ | justification path, navigable | yes | path instead of direct edge; compensation moved out |
| R4 | $x \in A \cup D$ | $\mathsf{Critical}$ | passed, adequate validation of same version | yes | version, result and adequacy added; domain restricted |
| R5 | $s \in S$ | relied upon, unvalidated | declared and linked | yes | quantifies over premises, not all entities |
| R6 | outcomes of R1-R5, R7 | — | valid compensation | — | targets obligation instances |
| R7 | $\alpha$ | always | explicit, versioned, covering parameter set | no | addressed to the application |
| R8 | $f \in F$ | failure in scope | every factor classified | — | classification instead of a single reason |

---

## 7.4 Deontic Layer (Obligations, Permissions, Consequences)

FOL invariants describe truth conditions. The method is normative: it includes obligations.
The deontic operators [von Wright 1951] are interpretive layers over the invariants; they do not replace or extend the underlying constraints.

- $\mathbf{O}(\varphi \mid \psi)$: given $\psi$, it is obligatory that $\varphi$ (MUST)
- $\mathbf{P}(\varphi \mid \psi)$: given $\psi$, it is permitted that $\varphi$ (MAY)
- $\mathbf{R}(\varphi \mid \psi)$: given $\psi$, it is recommended that $\varphi$ (SHOULD)

### 7.4.1 MUST as Conditional Obligation

**Definition 7.8.** For each rule $k$ with applicability and requirement:

$$\mathbf{O}\big(\mathrm{Req}_k(x) \mid \mathrm{App}_k(x)\big)$$

Example (Rule 1): $\mathbf{O}\big(\exists i\ (\mathsf{declares}(ch,i) \land \mathsf{Scoped}(i)) \mid \mathsf{NonTrivial}(ch)\big)$.

### 7.4.2 Compensation as a Contrary-to-Duty Obligation

Version 0.2.1 wrote "$P(\mathsf{Missing}(x))$ IF $O(\exists c \ldots)$", which is not a well-formed deontic formula. What the prose describes is a *contrary-to-duty* obligation: an obligation that arises because another obligation is violated [Chisholm 1963].

**Definition 7.9.** For each compensable rule $k \in K$, where $K$ is the set of compensable rules, *(proposed, OD-5: $K = \{R2, R3, R4, R5\}$)*:

$$\mathbf{O}\big(\exists c\ \mathsf{Valid}_t(c, \langle k, x\rangle) \mid \mathrm{App}_k(x) \land \lnot \mathrm{Req}_k(x)\big)$$

The primary obligation $\mathbf{O}(\mathrm{Req}_k \mid \mathrm{App}_k)$ is not withdrawn when the secondary one is met. That is the formal content of "compensation does not erase the obligation".

Contrary-to-duty structures are known to produce paradoxes when reasoned with inside standard deontic logic. The method avoids this by not reasoning *within* a deontic logic. The operators are a reading of the outcome function (7.5), which is defined directly over the record. No deontic inference is required to evaluate the method.

### 7.4.3 Recommendations

A recommendation $\mathbf{R}(\varphi \mid \psi)$ that is not followed produces a *note* in the evaluation, not an outcome. Example: an assumption without tracked status (Rule 5, SHOULD).

---

## 7.5 Evaluation Under Incomplete Evidence

Classical first-order semantics assumes a complete model: a link that is not in the state is false. Applied to evaluation, this treats the evaluator's lack of access as the team's lack of work (review F-16). The method therefore evaluates formulas in a three-valued semantics over a *partial* record with declared completeness.

### 7.5.1 Snapshot and Completeness

**Definition 7.10 (snapshot).** A snapshot $\Sigma$ is the finite structure of entities, relations and attributes obtained from the declared evidence sources at declared baselines (7.6).

**Definition 7.11 (completeness declaration).** For a relation symbol $r$ and a part of the scope $\sigma$, the evaluation contract may declare $\mathsf{Complete}(r, \sigma)$: every true instance of $r$ whose first argument lies in $\sigma$ is in $\Sigma$. This is a *local closed-world assumption* [Reiter 1978; Etzioni, Golden and Weld 1997]. It is a claim made by the evaluation, recorded in the contract, and it can be wrong.

### 7.5.2 Three-Valued Evaluation

**Definition 7.12.** Let truth values be $\{\mathbf{t}, \mathbf{u}, \mathbf{f}\}$ with $\mathbf{f} < \mathbf{u} < \mathbf{t}$. The value $\mathrm{val}_\Sigma(\varphi)$ is defined by:

- *Atoms of the record.* $\mathrm{val}(r(\bar a)) = \mathbf{t}$ if $r(\bar a) \in \Sigma$ and every record it depends on is accessible. It is $\mathbf{f}$ if $r(\bar a) \notin \Sigma$ and $\mathsf{Complete}(r, \sigma)$ is declared for the scope part containing $\bar a$. It is $\mathbf{u}$ otherwise.
- *Policy predicates.* The value given by the policy in $\Pi$, or $\mathbf{u}$ if the policy is missing or does not decide the case.
- *Connectives* (strong Kleene [Kleene 1952]): $\mathrm{val}(\lnot\varphi)$ swaps $\mathbf{t}$ and $\mathbf{f}$ and keeps $\mathbf{u}$; $\mathrm{val}(\varphi \land \psi) = \min$; $\mathrm{val}(\varphi \lor \psi) = \max$; $\varphi \rightarrow \psi \equiv \lnot\varphi \lor \psi$.
- *Quantifiers.* $\mathrm{val}(\exists x\, \varphi) = \mathbf{t}$ if some known $x$ gives $\mathbf{t}$. It is $\mathbf{f}$ if all known $x$ give $\mathbf{f}$ and the domain of $x$ is declared complete. It is $\mathbf{u}$ otherwise. $\forall$ is dual.

**Proposition 7.2 (no violation from ignorance).** If no completeness is declared for the relations a requirement depends on, an existential requirement can evaluate to $\mathbf{t}$ or $\mathbf{u}$ but never to $\mathbf{f}$. Absent evidence becomes negative evidence only where the evaluation explicitly claims completeness.

**Proposition 7.3 (monotonicity).** Let $\Sigma \subseteq \Sigma'$, where $\Sigma'$ adds records only in places for which completeness was not declared, and adds no policies that contradict existing ones. Then every value $\mathbf{t}$ or $\mathbf{f}$ under $\Sigma$ is unchanged under $\Sigma'$; only $\mathbf{u}$ values can change. If new evidence changes a $\mathbf{f}$, a completeness declaration was false, and the earlier evaluation must be corrected, not merely updated. (Argument: strong Kleene connectives and the quantifier clauses are monotone in the information ordering $\mathbf{u} \sqsubset \mathbf{t}, \mathbf{f}$.)

### 7.5.3 Validity of Compensations

**Definition 7.13.** A compensation $c$ is valid at evaluation time $t$ for instance $o = \langle k, x\rangle$ iff:

$$\begin{aligned}\mathsf{Valid}_t(c, o) \equiv\ & \mathsf{compensates}(c, o) \land \mathsf{StatesRisk}(c) \land \mathsf{Admissible}(c, o)\\ & \land \exists g\ \big(\mathsf{acceptedBy}(c, g) \land \mathsf{MayAccept}(g, o)\big) \land \tau(c) \le t \land \mathsf{Unexpired}_{t_x}(c)\end{aligned}$$

where $t_x = \min(t, \mathrm{end}(x))$, and $\mathrm{end}(x)$ is the time the subject left operation (it was superseded, withdrawn or rolled back), or $\infty$ if it is still in operation. $\mathsf{Unexpired}_{t_x}(c)$ holds if the review condition of $c$ had not been reached at $t_x$, or if $c$ is open-ended and $\mathsf{PermitsPermanent}(o)$ holds *(proposed, OD-6)*. $\mathsf{MayAccept}$ is decided by the authority policy *(proposed, OD-7)*.

Using $t_x$ means that a compensation covers the exposure of its subject. If a hotfix version is replaced before its compensation expires, the hotfix instance stays *compensated* in later evaluations. If the compensation expires while the version is still in operation, the instance is *violated*, and remains so in later evaluations (chapter 9, Scenario C).

A compensation is *retroactive* if $\tau(c)$ is later than the exposure of the subject (the time the subject entered operation or delivery). Retroactivity does not affect $\mathsf{Valid}_t$; it is reported, and it matters for diagnosis (7.7) *(proposed, OD-6)*.

### 7.5.4 Outcome Function

**Definition 7.14 (outcome) (proposed, OD-10).** For an obligation instance $o = \langle k, x\rangle$ with $k \ne R8$, let

$$\mathit{app} = \mathrm{val}(\mathrm{App}_k(x)), \quad \mathit{req} = \mathrm{val}(\mathrm{Req}_k(x)), \quad \mathit{comp} = \begin{cases} \mathrm{val}(\exists c\ \mathsf{Valid}_t(c, o)) & k \in K \\ \mathbf{f} & k \notin K \end{cases}$$

Then

| Condition | Outcome |
|---|---|
| $\mathit{app} = \mathbf{f}$ | **not applicable** |
| $\mathit{app} \ne \mathbf{f}$ and $\mathit{req} = \mathbf{t}$ | **satisfied** |
| $\mathit{app} \ne \mathbf{f}$, $\mathit{req} \ne \mathbf{t}$ and $\mathit{comp} = \mathbf{t}$ | **compensated** |
| $\mathit{app} = \mathbf{t}$, $\mathit{req} = \mathbf{f}$ and $\mathit{comp} = \mathbf{f}$ | **violated** |
| otherwise | **indeterminate** |

The conditions are mutually exclusive and exhaustive.

**Proposition 7.4 (compensation does not erase obligations).** No instance is *satisfied* because of a compensation: the outcome *satisfied* depends only on $\mathit{req}$. If every compensation is removed from $\Sigma$, a *compensated* instance becomes *violated* or *indeterminate*, never *satisfied*.

**Proposition 7.5 (violations are decided).** An instance is *violated* only if its applicability is decided true, its requirement is decided false, and no compensation is possibly valid. By Proposition 7.2, this requires a completeness declaration for the evidence the requirement depends on.

Rule 6 is then evaluated over the outcomes: the *violated* instances of compensable rules are exactly the cases in which the contrary-to-duty obligation of 7.4.2 is unmet. Violations of non-compensable rules are reported only under their own rule.

### 7.5.5 Aggregate Verdict

**Definition 7.15 (verdict) (proposed, OD-10).** For the set of outcomes of an evaluation:

- **non-compliant** if some instance is *violated*;
- otherwise **inconclusive** if some instance is *indeterminate*;
- otherwise **compliant with compensations** if some instance is *compensated*;
- otherwise **compliant**.

The verdict is always reported together with the full outcome profile (8.7). It replaces the 0.2.1 definition $\mathsf{Compliant}(State) \iff \mathsf{Violations}(State) = \emptyset$, under which compensated and indeterminate cases counted as compliant.

---

## 7.6 Time, Versions and Reproducibility

**Definition 7.16 (evaluation input).** An evaluation is a function of the tuple

$$\varepsilon = (M, \rho, \alpha, \Pi, \Sigma_b, t, J)$$

- $M$: method version;
- $\rho$: ruleset version, including the resolved open decisions or the proposed interpretations applied;
- $\alpha$: the method application and its evaluated scope;
- $\Pi$: the parameter set version;
- $\Sigma_b$: the snapshot at baselines $b$, identified by immutable references (commit hashes, document revisions, content digests) and with completeness declarations;
- $t$: the evaluation time, used only for the validity of compensations;
- $J$: the recorded judgments (assessments with author and date) used to interpret judgment-based policies.

**Proposition 7.6 (reproducibility).** For a fixed $\varepsilon$ the outcomes are determined. Re-assessing a judgment changes $J$ and therefore produces a different evaluation, which must be reported as such.

**Proposition 7.7 (order independence).** Outcomes do not depend on the recording times $\tau$ of intents, decisions, assumptions, validations or links. The only uses of $\tau$ are $\tau(c) \le t$ and the retroactivity flag for compensations. An intent recorded after the code it justifies yields the same outcome as one recorded before it. This is the formal content of orthogonality (chapter 5). The single exception, compensation timing, is explicit: accepting a risk is meaningful only relative to the exposure it covers.

**Validation and versions.** Because $A$ contains versions, a validation of $a$ does not validate a successor $a'$ unless $\mathsf{equiv}(a, a')$ is recorded. An equivalence declaration is itself a record and can be challenged.

**Method versions.** An evaluation is bound to $\rho$. Changing the method does not change past evaluations; re-evaluation under a new ruleset is a new evaluation $\varepsilon'$ (8.6).

**Sketch (temporal properties).** Properties of the evolution of a record, such as "every compensation is eventually remediated or renewed before it expires", are temporal properties over a sequence of snapshots. In linear temporal logic: $\square\big(\mathsf{compensated}(o) \rightarrow \lozenge(\mathsf{satisfied}(o) \lor \mathsf{renewed}(o))\big)$. Such properties can describe the health of an engineering record over time. They are not part of evaluation, which is defined on a single snapshot.

---

## 7.7 Diagnosability

Diagnosis starts from a failure $f$ and a set of *causal factors* $\Phi(f)$ identified by a causal analysis (incident analysis, debugging, root-cause investigation). The method does not identify causal factors; causal inference is outside its scope. What the method defines is how factors are related to the engineering record.

**Definition 7.17 (factor classification) (proposed, OD-1).** Let $\varepsilon_f$ be the evaluation input at the time of exposure (the snapshot and time before the failure). Each factor $\varphi \in \Phi(f)$ is classified as:

1. **gap**: $\varphi$ is linked to a subject $x$ for which some instance $\langle k, x\rangle$ is *violated* under $\varepsilon_f$ (this includes instances with a compensation that was invalid at the time), or *compensated* by a compensation whose stated risk does not cover $\varphi$;
2. **accepted risk**: $\varphi$ is linked to a subject whose instance is *compensated* under $\varepsilon_f$ by a compensation whose stated risk covers $\varphi$, or to a declared assumption $s$ ($\mathsf{Declared}(s)$) that proved false. A compensation recorded after the failure is not in $\varepsilon_f$ and cannot place a factor in this class;
3. **parameter misclassification**: $\varphi$ is linked to a subject whose instance was *not applicable* or *compensable* only because of a policy, and the consequence lies outside the declared risk tolerance (this classification is a recorded judgment);
4. **external**: $\varphi$ lies outside the evaluated scope;
5. **unrelated**: $\varphi$ lies within the scope but is not linked to any element of $\Sigma$.

If whether $\varphi$ is linked cannot be decided because evidence is inaccessible, the classification is *indeterminate*.

**Definition 7.18 (Rule 8 outcome) (proposed, OD-1).** For a failure $f$ in scope, the instance $\langle R8, f\rangle$ is *violated* if some factor is *unrelated*. It is *indeterminate* if no factor is unrelated and some classification is indeterminate. Otherwise it is *satisfied*.

Rule 8 can therefore be satisfied while another rule is violated: a failure explained by a missing validation is *diagnosed*, and the diagnosis is what Rule 8 requires. The 0.2.1 definition $\mathsf{Diagnosable}(f) \iff \exists r\ \mathsf{ExplainsInMethodTerms}(r, f)$ corresponds to "some factor is classified 1, 2 or 3". It made a correct record whose failure had an external cause count as non-application of the method.

**Limits.** A classification relates a factor to the record. It does not assert that the related gap was a *sufficient* cause, nor that the analysis found every factor. Classifying a decision as wrong after the fact must use the record available when the decision was made, because hindsight biases judgment about what was knowable [Fischhoff 1975; Dekker 2006].

---

## 7.8 Expressiveness: What First-Order Logic Covers

| Concern | First-order logic over a snapshot | Addition in this chapter | Status |
|---|---|---|---|
| Applicability | conditional formulas | $\mathrm{App}_k$ / $\mathrm{Req}_k$ pairs | Definition |
| Context-dependent obligations | uninterpreted predicate symbols | parameters as interpretations of policy predicates (7.2.4) | Definition |
| Traceability paths | not definable (transitive closure) | transitive-closure operator | Definition |
| Accepted deviations | not representable: a compensated state either satisfies or violates the formula | outcome function separating requirement and compensation (7.5.4) | Definition |
| Missing or inaccessible evidence | closed-world semantics assumes completeness | three-valued semantics with declared local completeness (7.5.2) | Definition |
| Diagnostic outcomes | causal reasoning is not expressible as constraints over the record | classification of externally identified factors (7.7) | Definition; causal analysis out of scope |
| Time and versions | time-stamped attributes and versioned entities suffice for evaluation | evaluation input tuple (7.6) | Definition |
| Evolution over time | not needed for evaluation | temporal logic over snapshot sequences | Sketch |

The conclusion is that first-order logic remains the object language of the rules. What it lacks is supplied by a three-valued semantics, a transitive-closure operator and an outcome function. None of these requires an inference engine, a theorem prover or a new language. Over a finite snapshot, each rule is a finite query.

---

## 7.9 Practical Notes (Non-Normative)

- This formalization is compatible with relational and graph databases, recursive queries and constraint checking. It does not prefer any of them.
- It is independent of any development process or lifecycle, and of any tool that stores the engineering record.
- It supports reproducible evaluation under an explicit context (7.6). It does not make evaluation objective where policies require judgment; it makes those judgments explicit, attributed and replayable.
- It does not identify the causes of failures. It relates causes identified by analysis to the engineering record and states what the record could not explain.
