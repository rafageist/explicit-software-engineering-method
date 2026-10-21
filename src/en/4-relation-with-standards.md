# 4. Relationship to Standards

The Explicit Software Engineering Method is designed to operate within software engineering standards rather than replace them. It assumes that standards define the context of work and clarifies how engineering accountability is established within that context.

Earlier versions of this chapter described IEEE and ISO standards collectively as process frameworks that "generally do not enforce explicit capture of engineering reasoning". That is not accurate for several of them. This chapter identifies the standards concerned and states the relationship for each.

## 4.1 What Identifiable Standards Address

| Standard | What it addresses | Relationship to the method |
|---|---|---|
| ISO/IEC/IEEE 12207 (software) and ISO/IEC/IEEE 15288 (systems) life cycle processes | Process definitions, including Decision Management, Risk Management, Configuration Management, Information Management, Verification and Validation | These standards define processes whose outcomes include recorded decisions, rationale and risks. The method does not define processes. It defines obligations over the records such processes produce, and it evaluates those records whatever process produced them. |
| ISO/IEC/IEEE 42010 | Architecture description, including architecture rationale and decisions | A conforming architecture description is a source of decision and intent records for Rules 2 and 3 at the architectural level. The method also covers decisions below the architectural level and their link to individual changes. |
| ISO/IEC/IEEE 29148 | Requirements engineering, including requirement attributes and traceability | Requirements are a common form of intent (Rule 1) and requirements traceability is a part of Rule 3 [Gotel and Finkelstein 1994]. The method adds intents for individual changes, compensation for missing links, and evaluation under incomplete evidence. |
| IEEE 1012 | Verification and validation, with integrity levels that scale V&V tasks to criticality | Integrity levels are a ready-made criticality and adequacy policy for Rule 4. The method generalizes the idea to every parameter-dependent predicate and adds explicit compensation when required V&V is missing. |
| ISO/IEC/IEEE 16085 | Risk management in the life cycle | A compensation is a recorded risk acceptance. Risk-management practice can supply the authority policy and the risk statements that Rule 6 requires. |
| ISO/IEC/IEEE 15289 | Content of life-cycle information items | Provides content structures that can serve as records (8.4.1). The method requires certain content and links, not a particular document. |
| ISO/IEC 25010 | Product quality model | Supplies vocabulary for the quality attributes named in intents and trade-offs. |
| ISO/IEC/IEEE 24765 | Systems and software engineering vocabulary | Terminological reference. Where the method's terms differ, the difference is deliberate (see below). |

These relationships are based on the published scope and process descriptions of each standard. A clause-by-clause mapping against current editions is future work, and it should be made against the normative texts, not from this summary.

**A note on terminology.** In ISO/IEC/IEEE usage, *verification* confirms that specified requirements are fulfilled, and *validation* confirms that the requirements for a specific intended use are fulfilled. The method uses *validation* for any explicit evidence that an artifact or decision satisfies its stated intent under the declared context (glossary). It therefore covers what the standards call verification as well as validation. Evaluators applying the method within a standards-based process can record which of the two each validation record is.

## 4.2 What the Method Adds, and What It Does Not

Standards define where engineering happens and, in several cases, which records it should produce. The method adds three things that the standards above do not provide as such:

1. **Evaluation independent of the process that produced the records.** A record produced under 12207, under Scrum, or by a solo developer is evaluated by the same rules (chapter 5).
2. **Explicit semantics for deviation and uncertainty.** These are the outcomes *compensated* and *indeterminate*, the requirement that compensation not erase obligations, and the rule that missing evidence is not proof of absence (chapter 7.5).
3. **A defined relation between failure and the engineering record.** This is the factor classification of chapter 7.7.

The method is not a conformity assessment scheme. Applying it does not demonstrate conformance with any standard, and conformance with a standard does not imply that the method's obligations are met. A team can follow a standards-compliant process and still produce software that cannot be diagnosed after failure, because the reasoning behind key choices was never made explicit. The same process can also produce an engineered product, when intent and decisions are captured in a way that allows later evaluation of why the system behaves as it does.

## 4.3 Process Frameworks vs Method Execution

The method is orthogonal to process standards. It constrains engineering outcomes, not workflows, and allows the same process to be compliant or non-compliant depending on whether explicit reasoning is preserved. This separation means the method does not require changes to lifecycle phases or organizational routines.

This is not a conflict with Agile, plan-driven, or hybrid approaches. The method can be adopted incrementally within any of them, because it evaluates what exists rather than prescribing how work must be ordered or coordinated.

Compatibility with standards matters because it enables diagnosability and evaluation across different contexts. Standards can specify activities and artifacts, but they cannot by themselves explain failure as engineering evidence. The method fills that gap without altering the standard-defined structure of work.

The result is a clear division of responsibility: standards define where engineering happens and, often, what it should record; the method defines what must be true of the record for the work to count as accountable engineering, and how that is evaluated.
