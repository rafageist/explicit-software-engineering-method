# Review of ESEM 0.2.1: Rules, Formalization and Publication

Status: maintainer-facing review. Not part of the manuscript.
Scope: `README.md`, `manifest.yaml`, `src/en/*`, `src/es/*`, `scripts/*`, `.github/workflows/build-pdf.yml` at commit `6bc6dd0`.
Related issues: #1, #2, #3.

This review records what the 0.2.1 text says, where the prose and the formalization disagree, and which defects are editorial versus normative. Normative questions that change the meaning of the method are not resolved here; they are listed in [`open-decisions.md`](open-decisions.md) with alternatives and a recommendation.

Finding identifiers (`F-nn`) are referenced from the change log and the pull request.

---

## 1. Rule-to-formalization map (0.2.1)

| Rule (ch. 3) | Prose obligation | Formal counterpart (ch. 7) | Agreement |
|---|---|---|---|
| R1 Intent Declaration | Non-trivial change MUST declare a scoped intent | `∀ch (Change ∧ NonTrivial → ∃i declares(ch,i) ∧ Scoped(i))` | Structurally aligned. `NonTrivial` and `Scoped` are undefined (F-01). |
| R2 Decision Explicitness | Irreversible or impactful decision MUST be explicit, reference its intent and alternatives "(at least implicitly)"; undocumented decisions are treated as assumptions | Impactful decision serves an intent **or is compensated**; otherwise `AssumptionByDefault` | Diverges: formula omits alternatives and irreversibility; adds a compensation exit not in the prose; applies "treated as assumption" to *documented* decisions lacking an intent link, while the prose applies it to *undocumented* ones (F-02, F-03, F-04). |
| R3 Artifact Traceability | Behavior-affecting artifact MUST trace to an intent or decision; navigable both ways | Direct `justifies(a,x)` edge **or compensation**; `Orphan(a)` otherwise | Diverges: prose says *traceable* (path), formula requires a *direct* edge; bidirectionality is not represented; compensation exit not in prose (F-05, F-06). |
| R4 Validation Requirement | Critical artifacts and decisions MUST have explicit validation; criticality is a parameter | `∀x (Critical(x) → validated ∨ compensated)`, `Critical ↔ CriticalUnderParams(x, ParamsScope(x))` | Partly aligned. Formula quantifies over all entities (prose: artifacts and decisions). Validation depth, adequacy and version are absent. `ParamsScope` undefined (F-07, F-08). |
| R5 Assumption Declaration | Assumptions MUST be declared when evidence is missing or deferred; SHOULD be tracked | `∀x (EvidenceMissing(x) → ∃s assumes(x,s) ∧ Explicit(s))` | Domain mismatch (`assumes ⊆ (D∪A)×S`, but `x` is unrestricted). SHOULD-tracking is not formalized. Overlap with R6 undefined (F-09). |
| R6 Explicit Compensation | Missing required artifact or validation MUST be compensated: documented, references the missing element, states accepted risk | `∀x (Required(x) ∧ Missing(x) → ∃c compensates(c,x) ∧ StatesAcceptedRisk(c))` | Ill-formed: a missing element is not in the universe `E`, so it cannot be quantified over or be the target of `compensates` (F-10). Authority, expiry and remediation are absent in both prose and formula (F-11). |
| R7 Parameter Awareness | The method MUST be applied with explicit contextual parameters | `∀ch (NonTrivial(ch) → ∃p paramOf(p,ch))` | Too weak: any single parameter satisfies it. The prose obligation is on the *application*, not on each change. No link from parameters to the predicates they are supposed to define (F-12). |
| R8 Diagnosability of Failure | When failure occurs, at least one of six method-level reasons MUST be identifiable; otherwise "the method was not applied" | `∀f (Failure(f) → ∃r ExplainsInMethodTerms(r,f))` | Formally aligned but substantively problematic: contradicts ch. 6.6 (external and irreducible failures), mixes violations with legitimate realized risks, and has no clear deontic addressee (F-13, F-14). |
| Deontic layer (7.4) | MUST/MAY/SHOULD | `P(Missing(x)) IF O(...)` | Not a well-formed deontic formula; compensation semantics in 7.4.3 make a compensated state indistinguishable from a satisfied one (F-15). |

---

## 2. Findings

### 2.1 Normative and formal consistency

**F-01. Undefined applicability predicates.**
`NonTrivial`, `Impactful`, `AffectsBehavior`, `Critical`, `Scoped` and `Required` carry the whole applicability of the rules but have no definition, and the text does not say who decides them. Only `Critical` is tied (informally) to parameters. Without a declared criterion, two evaluators can produce different results on the same record, which contradicts "operational objectivity under explicit context" (7, preamble).
*Resolution in 0.3 draft:* each applicability predicate is interpreted by a declared policy in the parameter set (ch. 3.0, ch. 7.2.4, ch. 8.3). Non-controversial: this makes the existing statement that "parameters shape what counts as critical" uniform across rules.

**F-02. "Alternatives considered (at least implicitly)".**
An explicit record cannot reference something implicitly. The parenthesis either weakens R2 to "intent only" or is a contradiction. → OD-3.

**F-03. "Treated as assumptions by default".**
The prose says undocumented decisions become assumptions by default. Two readings are possible: (a) reclassification *discharges* R2, or (b) the classification is diagnostic and R2 remains unmet. The 0.2.1 formula applies the rule to documented decisions without an intent link, which is a third case. → OD-2.

**F-04. Compensation exits added only in the formalization.**
R2 and R3 formulas include `∨ ∃c compensates(c, ·)`; the prose of R2/R3 does not mention compensation, while R6 prose restricts compensation to "artifact or validation". Which obligations are compensable is therefore undetermined. → OD-5.

**F-05. Direct edge versus traceability path.**
R3 prose requires that an artifact be *traceable* to an intent or decision; the formula requires a direct `justifies` edge. An artifact linked to a decision that serves an intent is traceable but only satisfies the formula because the decision is itself in the allowed target set; an artifact linked to an intermediate artifact (e.g. generated code to its model) fails the formula. *Resolution:* use the derived `traceableTo` path relation defined in 7.2.2, which 0.2.1 defines but never uses. Non-controversial.

**F-06. Bidirectional navigability is not a property of the graph.**
In a relational model every relation can be read in both directions, so "navigable in both directions" is trivially true of the formal model and says nothing. The real obligation is about the *representation*: a link must be resolvable from either end using the declared evidence sources (e.g. a commit that cites a ticket is navigable from the commit; it is navigable from the ticket only if the repository is in scope and searchable). *Resolution:* state it as a requirement on evidence sources (ch. 8.4). Clarification, not a new obligation.

**F-07. Domain of R4.**
Prose: artifacts and decisions. Formula: any `x`, including intents, assumptions and parameters. `validates ⊆ V × (A ∪ D ∪ I)` allows intent validation, which is meaningful (stakeholder confirmation) but not required by the prose. → OD-12 (recommendation: follow the prose).

**F-08. Validation without version or adequacy.**
Any `validates` edge satisfies R4, including a validation of an older version of the artifact or one whose depth is below what the parameters require. The prose says parameters influence "validation depth", but nothing in the formula uses it. *Resolution:* validation is bound to the version it examined, and adequacy is a parameter-interpreted predicate (ch. 7.2.4, 7.6). Version binding is non-controversial; adequacy criteria remain contextual.

**F-09. R5 and R6 overlap.**
A critical artifact without validation triggers both R5 (evidence missing → declare an assumption) and R6 (required validation missing → compensate). 0.2.1 does not say whether one discharges the other. *Resolution:* they record different things. An assumption records what is believed; a compensation records which obligation is unmet and which risk is accepted. Both may be required for the same gap. Clarification, stated in 3.5 and 3.6.

**F-10. Quantifying over missing elements.**
`Missing(x)` with `x ∈ E` is ill-formed: if the validation is missing, there is no `x` in `V` to refer to. The same problem affects `compensates ⊆ C × (I ∪ D ∪ A ∪ V)`. *Resolution:* introduce *obligation instances* `o = ⟨k, x⟩` (rule `k` applied to an existing subject `x`) and make compensation target obligation instances. This is a repair of the formal model that keeps the prose meaning ("reference the missing element"). Non-controversial.

**F-11. Compensation lifecycle is unspecified.**
No authority, no expiry or review condition, no remediation, no rule on compensations recorded after the fact. Compensation without accountable acceptance is indistinguishable from a note. → OD-6, OD-7.

**F-12. R7 is trivially satisfiable and mis-addressed.**
`∃p paramOf(p, ch)` is satisfied by any parameter, e.g. "team scale = 3", which does not determine criticality or any other predicate. The prose obligation is on the method application. → OD-9 (minimum parameter set). The re-addressing to the application scope is a clarification.

**F-13. R8 contradicts chapter 6.**
R8: "If failure cannot be explained in method terms, the method was not applied." Chapter 6.6: "some failures remain irreducible or external." A correctly engineered system can fail because of a hardware fault or a provider incident, with all obligations satisfied. Under R8 as written, such a failure proves non-application of the method, which is false and pushes analysts to find a gap where there is none (hindsight bias). → OD-1.

**F-14. R8 reasons mix violations with realized accepted risk.**
"False assumption" and "inadequate compensation" are listed together with "missing intent". A declared assumption that later proves false is R5 working as intended; it is not a violation. A failure that realizes a risk accepted by a valid compensation is the method working, not failing. The list needs classes. Addressed in the proposed R8 interpretation (ch. 3.8, 7.7) and OD-1.

**F-15. Compensation erases the obligation in the 0.2.1 semantics.**
Because R2, R3 and R4 formulas contain a compensation disjunct, a compensated state *satisfies* the formula. `Violations(State)` is then empty and `Compliant(State)` holds, exactly as if the obligation had been met. This contradicts 3.0 and 3.6 ("it does not erase the obligation"). *Resolution:* separate the requirement from the compensation in the formula and report `Compensated` as a distinct outcome (ch. 7.5). This is the most important formal correction in this review; it implements, rather than changes, the existing prose.

**F-16. Missing evidence is treated as proof of absence.**
Classical first-order semantics assumes a complete model: if a `validates` edge is not in the state, it is false. An evaluator that cannot access a CI system, or evaluates only part of a system, would report violations that are artifacts of its own blindness. *Resolution:* partial models with three-valued evaluation and declared evidence completeness (local closed-world assumption) (ch. 7.5). Required by issue #1.

**F-17. Trade-offs are named but not governed.**
The thesis (README, ch. 0, glossary) lists trade-offs among the things that must be explicit. Chapter 7 defines `T` and `tradesOff`, but no rule creates an obligation over trade-offs and the glossary has no entry. → OD-4.

**F-18. Artifact definition conflicts.**
README: "a produced, versioned work product". Glossary: "...that affects system behavior". If every artifact affects behavior, `AffectsBehavior(a)` in R3 is redundant; if not, the glossary is wrong. *Resolution:* artifact = versioned work product; behavior-affecting artifacts are a parameter-defined subset. Engineering records (intent, decision, assumption, validation, compensation) are typed by role even if stored in files. Clarification.

**F-19. Time and versions are absent.**
There is no notion of evaluation time, baseline or record version. Compensation expiry, validation of a specific version, method version changes and re-evaluation cannot be expressed. Required by issue #1 and #2. Addressed in ch. 7.6 and 8.6.

**F-20. Scope of application is undefined.**
"Each relevant scope" (7.3.7), "project scope containing it" (7.2.1) and "Method Application" (glossary) refer to a scope that is never defined: which system boundary, which changes, which evidence sources. Addressed in ch. 8.2.

### 2.2 Claims and limits

**F-21. Objectivity claims are inconsistent.**
README 9: "objective assessment of engineering quality". Ch. 0.4: "makes engineering work objectively evaluable". Ch. 7.6: "sufficient to support objective evaluation". Ch. 7 preamble, correctly: "operational objectivity under explicit context, not absolute objectivity". Several predicates (adequacy of validation, impact of a decision) require judgment. *Resolution:* align all claims with the ch. 7 formulation, and require judgment-based assessments to be recorded as inputs of the evaluation with their author (ch. 8.6).

**F-22. Hypothesis presented without evidence status.**
Ch. 0.3 states a hypothesis; elsewhere (README 9 "Expected Outcomes", ch. 2.5, 6.5) its consequences are stated as facts. No empirical evaluation is reported. *Resolution:* mark expected outcomes as expected, and state in 0.3 that the hypothesis is untested.

**F-23. Standards are characterized generically.**
Ch. 4.1 says IEEE/ISO standards "generally do not enforce explicit capture of engineering reasoning". This is inaccurate for several identifiable standards: ISO/IEC/IEEE 12207 and 15288 define a Decision Management process; ISO/IEC/IEEE 42010 addresses architecture rationale; ISO/IEC/IEEE 29148 addresses requirements traceability. The precise relationship needs to be stated standard by standard (ch. 4, rewritten).

**F-24. "Executable" is ambiguous.**
README describes the method as "a minimal, executable set of rules". Nothing in the method is executed; rules are evaluated. *Resolution:* "evaluable".

### 2.3 Bilingual manuscript and publication

**F-25. Corrupted formulas in the Spanish formalization.**
`src/es/7-formalizacion.md`, Rules 2 and 3: logical symbols were replaced by `?` (e.g. `(?i (Intent(i) ? serves(d, i)) ? ?c ...`). The published Spanish PDF 0.2.1 therefore contains meaningless formulas. Fixed; a check prevents regressions.

**F-26. Unicode logic symbols outside math mode.**
Formulas are written as plain Unicode text (`∀`, `∃`, `∧`, `→`). With XeLaTeX and the default Latin Modern text font several of these glyphs are not available, so the PDF depends on font fallback. *Resolution:* formulas are written in TeX math (`$...$`), which renders consistently in PDF and on GitHub.

**F-27. Raw LaTeX in the glossary.**
Both glossaries are written as `\begin{description}` LaTeX blocks inside Markdown; they do not render on GitHub and cannot be checked for EN/ES parity. *Resolution:* Markdown glossary inside a fenced `glossary` div; a Lua filter produces the two-column layout in the PDF.

**F-28. Index duplication and language asymmetry.**
The English PDF includes both the LaTeX table of contents and the generated Markdown index (whose links point to `.md` files and are dead in the PDF); the Spanish PDF includes only the table of contents. The build also rewrites `00-index.md` / `00-indice.md` in the source tree. *Resolution:* both PDFs use only the table of contents; index files remain as repository navigation and are verified (not silently rewritten) by `make check`.

**F-29. Document language not declared.**
Pandoc is not given `lang`, so the Spanish PDF uses English LaTeX strings (e.g. "Contents"). *Resolution:* `lang` metadata per language.

**F-30. Byte-order marks.**
Fourteen tracked files start with a UTF-8 BOM (most Spanish chapters, `README.md`, `scripts/build_pdf.py`). The build works around it in one place only. Removed; checked.

**F-31. Generated files tracked.**
`mermaid-images/*` are outputs of the Mermaid filter and are regenerated on every build. Removed from version control and ignored.

**F-32. Non-reproducible build inputs.**
The generation timestamp is wall-clock time; Mermaid CLI, the Python filter and the runner image are unpinned. *Resolution:* `SOURCE_DATE_EPOCH` (default: commit time of `HEAD`) drives the date; tool versions are pinned; a `Dockerfile` reproduces the CI toolchain. Byte-identical PDFs are not claimed: `wkhtmltopdf` embeds creation metadata. Textual reproducibility is the target.

**F-33. Every push to `master` publishes a release.**
The workflow creates or updates the GitHub release `v<manifest version>` on each push to `master`. A push without a version bump silently replaces the assets of an already published version. This conflicts with "no release without approval". *Resolution:* build on pull requests and pushes; publish only on an explicit `v*` tag that matches `manifest.yaml`, or a manual dispatch. See `docs/release-checklist.md`.

**F-34. No change history.**
Twelve versions were released without a changelog; commit messages are the only record. *Resolution:* `CHANGELOG.md`.

---

## 3. What is not a defect

- The eight-rule structure, the deontic vocabulary (MUST / SHOULD / MAY) and the separation of method, methodology, process and tooling are coherent and are preserved.
- The statement that rules constrain outcomes and not activity order is consistent throughout; the formalization supports it because evaluation depends only on the recorded state. The one exception introduced in 0.3 (compensation timing, OD-6) is explicit.
- "Formalization sketch" is an accurate title for 0.2.1. The 0.3 draft keeps the title and labels each statement as definition, proposition, sketch or example.
