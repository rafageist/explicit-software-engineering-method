# 2. From Software to Software Product

Software and software products are not equivalent. Software consists of executable code, configurations, and data that produce behavior. A software product is the result of engineering: software whose behavior, constraints, and purpose can be explained, validated, and justified. This chapter focuses on the difference between working functionality and accountable engineering outcomes.

---

## 2.1 Software Is Output; a Product Is an Outcome

Software can exist without engineering intent. It may function, pass tests, or satisfy immediate needs, yet remain opaque with respect to why it exists in its current form, which decisions shaped it, which assumptions it relies on, which trade-offs were accepted, and how its correctness or fitness was established. A software product, by contrast, is an outcome whose properties are intentional and explainable.

Consider a data pipeline that has grown through urgent fixes. It produces correct outputs most days, but no one can explain why certain thresholds exist or which failure modes were accepted. The system works, yet its behavior cannot be justified without reconstructing past decisions from memory.

By contrast, a customer-facing service may behave within defined constraints, and when a latency regression appears, the team can trace the change to a specific decision and the condition it was meant to satisfy. The service still fails in real conditions, but the failure is diagnosable as an engineering outcome.

The distinction is not about size, polish, performance targets, or bug counts. It is about engineering accountability.

---

## 2.2 Engineering Makes the Difference

Engineering introduces structure between problem and solution. A product is not defined by having more features or fewer bugs; it is defined by the visibility and accountability of the reasoning that shaped it. This is why a prototype can be valid software while still not qualifying as a product: it may demonstrate behavior without preserving the engineering reasoning behind it.

Once accountability exists, diagnosability becomes a property of the product rather than a consequence of who remembers the history.

---

## 2.3 Products Are Diagnosable; Code Alone Is Not

A defining property of an engineered product is diagnosability. Success in production does not retroactively create engineering accountability; it only shows that the system is currently acceptable. When failures occur, an engineered product allows the team to explain the failure in terms of the reasoning that led to the behavior, rather than relying on retrospective narrative or individual recollection.

This distinction explains why organization alone cannot close the gap.

---

## 2.4 Process Does Not Create Products by Itself

Processes coordinate activities. They do not guarantee that engineering reasoning is preserved. A team can follow a well-defined process and still produce software whose behavior cannot be explained beyond surface defects. This is not a critique of process; it is a recognition that organization and accountability are distinct concerns.

The difference is structural, which is why it requires an explicit mechanism.

---

## 2.5 The Role of Explicitness

Explicitness is the mechanism by which software is elevated to a product. When reasoning is preserved, outcomes are intentional, quality becomes defensible in context, failures are explainable, and learning is cumulative rather than anecdotal. This is the structural difference between working software and an engineered product.

---

## 2.6 Summary

Software can exist without engineering; products cannot. A software product is defined by explicit reasoning, not by delivery mechanics. Processes may produce software; a method defines the obligations that allow software to qualify as a product.

This distinction motivates the need for explicit obligations. The next step is to define what those obligations are, without yet prescribing how teams organize their work.
