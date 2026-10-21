# 5. Orthogonality to Process Frameworks

Orthogonality here is a structural property: the method evaluates engineering state independently of the sequence used to reach it. Order flexibility does not remove obligation; it only means there are multiple valid paths to a compliant outcome.

## 5.1 Different Problem Spaces
Process frameworks organize work through stages, roles, and coordination practices. They optimize how teams plan and deliver, but they do not determine whether the reasoning behind the work remains accountable. The method addresses that gap by evaluating what exists and how it is justified, regardless of how the work was scheduled.

## 5.2 Logical Dependencies vs Process Prescription
Engineering has logical dependencies, such as understanding a problem before validating a solution. Orthogonality does not deny those dependencies; it separates them from fixed sequencing. Real work is rarely linear: constraints are discovered late, assumptions are revised, and solutions evolve as understanding deepens.

One team might start from existing code, reverse-engineer the intent, and then record the reasoning that makes the current behavior defensible. Another team might start from models, define the intent first, and refine implementation until the behavior matches. Both can be compliant if the required reasoning is explicit and traceable. The method evaluates the state they reached, not the route they took.

## 5.3 Coexistence with Process Structure
A process can impose order while the method remains orthogonal. The method can be adopted within structured lifecycles because it does not require changes to phases or timelines. Compliance is evaluated on artifacts and traceability, not on whether a particular milestone happened first.

This makes incremental adoption possible: a team can introduce explicit reasoning in the parts of the system that matter most, without reorganizing the entire lifecycle.

## 5.4 What Orthogonality Does and Does Not Mean
Orthogonality does not mean anything goes. Obligations still apply, and missing reasoning remains a gap regardless of how the work was organized. The method is strict about outcomes while remaining flexible about paths.

Orthogonality has one deliberate limit. When an intent, decision, assumption or validation was recorded does not change any outcome: an intent written after the code is as valid as one written before it (chapter 9, Scenarios A and B; Proposition 7.7). Compensation is different. Accepting a risk means something only before exposure to it, so a compensation counts from the moment it is recorded, and one recorded after the fact is flagged as retroactive (OD-6). This does not prescribe an order of activities. It recognizes that accepting a risk is itself an act located in time.

## 5.5 Summary
Orthogonality makes the method applicable across teams, domains, and processes because it evaluates engineering state rather than activity sequence. It enables post-failure reconstruction by allowing accountability to be assessed even when the original work unfolded non-linearly. This is what allows the method to be universal without becoming prescriptive about workflow.
