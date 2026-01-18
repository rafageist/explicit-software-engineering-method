# 4. Relationship to Standards

The Explicit Software Engineering Method is designed to operate within software engineering standards rather than replace them. It assumes that standards define the context of work and clarifies how engineering accountability is established within that context.

## 4.1 Compatibility with IEEE and ISO Standards
IEEE / ISO software engineering standards define process frameworks, describing activities, roles, and lifecycle structures expected of engineering practice. They set the stage for what must be done, but they generally do not enforce explicit capture of engineering reasoning or ensure that rationale is preserved in an analyzable form.

This method complements those standards by constraining outcomes: it requires that engineering reasoning be explicit enough to support evaluation and diagnosis. Used together, standards define where engineering happens, while the method defines what must be true for those activities to count as accountable engineering.

It is possible to follow a standards-compliant process and still produce software that cannot be diagnosed after failure because the reasoning behind key choices was never made explicit. The same process can also produce an engineered product when intent and decisions are captured in a way that allows later evaluation of why the system behaves as it does.

## 4.2 Process Frameworks vs Method Execution
The method is orthogonal to process standards. It constrains engineering outcomes, not workflows, and allows the same process to be compliant or non-compliant depending on whether explicit reasoning is preserved. This separation means the method does not require changes to lifecycle phases or organizational routines.

This is not a conflict with Agile, plan-driven, or hybrid approaches. The method can be adopted incrementally within any of them, because it evaluates what exists rather than prescribing how work must be ordered or coordinated.

Compatibility with standards matters because it enables diagnosability and evaluation across different contexts. Standards can specify activities and artifacts, but they cannot by themselves explain failure as engineering evidence. The method fills that gap without altering the standard-defined structure of work.

The result is a clear division of responsibility: standards define where engineering happens, and the method defines what must be true for it to count as engineering.
