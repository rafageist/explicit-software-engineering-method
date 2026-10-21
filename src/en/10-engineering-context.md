# 10. Engineering Context, Context Engineering and the Method

This chapter is non-normative. It places the method in relation to two neighboring ideas: the context of engineering, and the engineering of contexts. Both are discussed in the essay *Engineering Context and Context Engineering* [Rodríguez Ramírez 2026]. The aim is to keep the three ideas distinct, because conflating them would make the method depend on a particular way of storing or delivering knowledge.

## 10.1 Three Different Things

1. **Engineering context** is the knowledge, constraints and circumstances in which engineering happens and which explain a solution: requirements, models, decisions, rejected alternatives, assumptions, tests, defects, conversations, and the relationships among them. It exists whether or not anyone records it. Part of it is explicit, part is tacit, and part is lost.
2. **Context engineering** is the deliberate construction, selection, preservation and delivery of relevant context to someone or something that needs it to act: an engineer joining a team, a reviewer, or a language-model agent asked to modify code. It is an activity with its own design choices: granularity, identity, relationships, retrieval and freshness.
3. **The method** defines obligations that make part of the engineering context explicit, traceable and evaluable: intent, decisions, assumptions, trade-offs, validations and accepted deviations, at a level of explicitness set by declared parameters.

The method does not describe the engineering context; it requires that a defined part of it exist as a record. It does not perform context engineering; it is indifferent to how records are stored, retrieved or delivered.

## 10.2 How They Meet

- **The engineering record is a projection of the engineering context.** The snapshot $\Sigma$ of chapter 7 is the part of the engineering context that is explicit, within the declared scope and sources, at a baseline. Whatever stays tacit is outside $\Sigma$ and, for evaluation, does not exist.
- **The method sets a floor, not a ceiling.** A team may keep far more context than the method requires. The method only requires that, within scope, the obligations of chapter 3 can be evaluated.
- **Context engineering can consume the record.** Before an agent or a person modifies an artifact, a context-engineering step can retrieve the intents, decisions, assumptions and validations that the artifact traces to. The method makes these records exist and be linked. It does not define how they are selected or presented.
- **Context engineering can produce candidates for the record, not records.** Tools and models can propose links, reconstruct rationale or summarize history. Under the provenance model (8.4.2), such output is *inferred* until a responsible person confirms it. A relationship inferred by a model does not acquire the authority of an approved decision or of a test that was actually executed.
- **Evaluation needs stable identity and versions.** The evaluation contract (8.6) requires immutable references to evidence. Any context store that is used as an evidence source must provide them, whatever its technology: files in a repository, a database or a knowledge graph.

## 10.3 Independence from Platforms

Because the method is defined over records and relations, not over a storage model, it can be applied with Markdown files and a repository, an issue tracker, a model repository, a graph database or a dedicated platform. It must not acquire concepts that exist only in one of them.

Divengine Studio may implement an optional evaluator of the method over its own engineering-context model. Such an evaluator is one implementation among possible others. It would have to respect the boundaries of chapter 8.9: an exposed evaluation contract, immutable inputs, inferred links kept distinct from recorded ones, and manual review still possible. The method would not become a Studio method, and its vocabulary would not become mandatory for every project that Studio manages.

## 10.4 Why the Distinction Matters for the Method

Language-model agents make the absence of explicit engineering reasoning more visible. An agent can read code and propose a locally reasonable change, without knowing that the code implements a constraint, that an alternative was rejected for security reasons, or that an odd behavior is deliberate. Making that reasoning explicit is what the method has always required. What agents change is the number of readers, and the cost of the reasoning not being there.

They also add a new risk: that inferred reasoning is mistaken for recorded reasoning. The provenance distinctions of chapter 8 are the method's answer to that risk. They hold whether the inference comes from a model, a static analyzer or a well-meaning engineer reconstructing the past.
