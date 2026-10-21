# Change Log

All notable changes to the method and its publication. Versions follow the policy proposed in `docs/open-decisions.md` (OD-11). Each entry says whether a change is **normative** (it can change evaluation outcomes), **clarifying** (it makes existing obligations evaluable without changing what they require), or **editorial**.

## 0.3.0-draft (unreleased, pending maintainer review)

Issues #1, #2, #3. Review findings `F-nn` refer to `docs/review-0.2.1.md`.

### Normative (proposed, pending decision)

These changes are labeled in the text as *Proposed interpretation (OD-n)* and do not take effect until the maintainer gives final approval. The 0.2.1 rule statements are unchanged. In the review of PR #4, the recommendations for OD-2 to OD-4 and OD-6 to OD-12 were accepted as the basis for the next draft; OD-1 and OD-5 were refined as described below.

- Rule 8 reinterpreted as diagnosability of the engineering record, with five factor classes. External factors and realized accepted risks no longer count as non-application of the method (OD-1; F-13, F-14).
- Refinement of OD-1: a missing engineering-context relationship (an established factor, acting within scope, with no relation to a record declared complete) is distinguished from causal uncertainty and incomplete investigation. Factors are *established* or *provisional*; unresolved factors make Rule 8 *indeterminate*, and *satisfied* requires a final set of factors. Failure analysis never makes an obligation *violated* on its own (Proposition 7.8). Scenario E gains an *investigation still open* variant.
- "Undocumented decisions are treated as assumptions" read as a diagnostic classification that does not discharge Rule 2 (OD-2; F-03).
- Decision records must list alternatives or state that none were evaluated (OD-3; F-02).
- Trade-offs governed as part of Rule 2 (OD-4; F-17).
- Compensable rules: R2-R4. Rules 1, 5 and 7 are not compensable (OD-5; F-04). Refinement of OD-5: the declaration of an assumption cannot be compensated; evidence gaps associated with a declared assumption are evaluated through the validation-adequacy policy under Rule 4 and compensated there. Scenarios C and E updated.
- New open decisions raised by the refinements: OD-13 (adequacy policy and declared assumptions), OD-14 (final set of factors for Rule 8), OD-15 (changes made outside the record).
- Compensation review condition, retroactive compensations and risk-acceptance authority (OD-6, OD-7; F-11).
- Provenance classes; inferred records never satisfy obligations (OD-8).
- Minimum parameter set for Rule 7 (OD-9; F-12).
- Outcome classes and aggregate verdict (OD-10; F-15, F-16).
- Method versioning and its effect on earlier evaluations (OD-11).
- Rule 4 applies to artifacts and decisions (OD-12; F-07).

### Clarifying

- Ch. 3: normative keywords per BCP 14; common terms (method application, engineering change, engineering record, obligation instance, policy); the five outcomes; a *Precision* paragraph for every rule (subject, applicability, satisfaction, evidence, formal counterpart).
- Ch. 7 rewritten. Changes: statement status labels; record attributes and provenance; versioned artifacts; compensations targeting obligation instances instead of missing entities (F-10); traceability as a justification path with transitive closure (F-05); parameters as interpretations of policy predicates (F-01); rules as applicability/requirement pairs, with compensation removed from the formulas (F-15); contrary-to-duty reading of Rule 6; three-valued evaluation with local completeness declarations (F-16); outcome function and verdict; time, version and reproducibility (F-19); factor classification for diagnosis; expressiveness assessment of first-order logic.
- New ch. 8, *Method Application and Evaluation*: evaluated scope, parameter set, evidence and provenance, compensation lifecycle, evaluation contract, reporting, tooling independence (F-06, F-20, F-21).
- New ch. 9, *Worked Examples*: code-first, model-first, emergency change, legacy system, failure investigation.
- New ch. 10, *Engineering Context, Context Engineering and the Method* (non-normative).

### Editorial

- Ch. 0: hypothesis marked as untested; objectivity claim aligned with ch. 7 (F-21, F-22).
- Ch. 4 rewritten with identified IEEE/ISO standards and a terminology note on verification/validation (F-23).
- Ch. 5: the timing of compensation as the explicit limit of order independence.
- Ch. 6: new section 6.6, *Limits of Diagnosability*.
- New references chapter. Glossary converted from raw LaTeX to Markdown, with missing terms added (trade-off, outcome, provenance, ...) (F-27).
- Spanish edition synchronized with the English edition; corrupted formulas in the Spanish ch. 7 repaired (F-25).
- README: "executable" replaced by "evaluable"; objectivity and standards claims qualified (F-24).

### Publication

- Formulas typeset as TeX math (F-26); the build fails on glyphs missing from the PDF fonts.
- Both PDFs use the LaTeX table of contents only; index files are checked, not rewritten, by the build (F-28).
- `lang` metadata per edition (F-29). Byte-order marks removed (F-30). Generated Mermaid images untracked (F-31).
- `SOURCE_DATE_EPOCH`, pinned tool versions, `Dockerfile` and `Makefile` for reproducible builds (F-32).
- `scripts/check_manuscript.py`: EN/ES structural and formula parity, corrupted formulas, BOMs, index freshness.
- CI builds on pull requests and pushes; releases only on a matching `v*` tag or manual dispatch (F-33). See `docs/release-checklist.md`.

## 0.2.1 and earlier

Released without a change log. See the git history and the GitHub releases `v0.1.0` to `v0.2.1`.
