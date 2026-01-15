# 5. Orthogonality to Agile and Process Frameworks

The Explicit Software Engineering Method is intentionally orthogonal to Agile frameworks, process models, and workflow prescriptions.

This is a design decision, not a limitation.

```mermaid
graph LR
    subgraph "Process Frameworks"
        A[Agile/Scrum]
        B[Kanban]
        C[Waterfall]
        D[RUP]
    end
    
    subgraph "Explicit Software Engineering Method"
        E[Intent Explicitness]
        F[Traceability]
        G[Validation]
        H[Evidence-based Diagnosis]
    end
    
    A -.orthogonal to.-> E
    B -.orthogonal to.-> F
    C -.orthogonal to.-> G
    D -.orthogonal to.-> H
    
    style E fill:#90EE90
    style F fill:#90EE90
    style G fill:#90EE90
    style H fill:#90EE90
    style A fill:#87CEEB
    style B fill:#87CEEB
    style C fill:#87CEEB
    style D fill:#87CEEB
```

## 5.1 Different Problem Spaces

Agile frameworks (such as Scrum or Kanban) primarily address:

- team coordination
- iteration and delivery cadence
- stakeholder feedback
- work prioritization

They optimize how work is organized and delivered.

The Explicit Software Engineering Method addresses a different problem:

- how engineering intent is made explicit
- how decisions are justified and traceable
- how assumptions and trade-offs are exposed
- how validation relates to intent
- how failures can be diagnosed with evidence

It optimizes how engineering reasoning is represented and evaluated, not how teams schedule or coordinate work.

```mermaid
flowchart TB
    subgraph "Agile Frameworks Focus"
        AF1[Team Coordination]
        AF2[Iteration & Delivery Cadence]
        AF3[Stakeholder Feedback]
        AF4[Work Prioritization]
    end
    
    subgraph "Explicit Software Engineering Method Focus"
        EM1[Engineering Intent]
        EM2[Decision Traceability]
        EM3[Assumptions & Trade-offs]
        EM4[Validation vs Intent]
        EM5[Evidence-based Diagnosis]
    end
    
    AF1 --> O1[Optimizes: Work Organization]
    AF2 --> O1
    AF3 --> O1
    AF4 --> O1
    
    EM1 --> O2[Optimizes: Engineering Reasoning]
    EM2 --> O2
    EM3 --> O2
    EM4 --> O2
    EM5 --> O2
    
    O1 -.Different Problem Spaces.-> O2
    
    style O1 fill:#87CEEB
    style O2 fill:#90EE90
```

## 5.2 Logical Dependencies vs Process Prescription

Software development involves real logical dependencies. For example, a solution cannot be validated without some understanding of the problem it addresses.

The method acknowledges such dependencies, but does not prescribe a fixed sequence of steps.

Instead, it defines:

- what must exist (intent, decisions, artifacts, validation)
- how these elements must relate
- how absence or incompleteness must be compensated explicitly

This allows:

- iterative discovery
- partial or evolving intent
- revisiting earlier decisions
- working under uncertainty

without enforcing a rigid lifecycle.

```mermaid
graph TD
    I[Intent] --> D[Decisions]
    D --> A[Artifacts]
    A --> V[Validation]
    V -.relates back to.-> I
    
    D -.must be.-> J[Justified & Traceable]
    I -.can be.-> P[Partial/Evolving]
    D -.can be.-> R[Revisited]
    A -.when absent.-> C[Compensated Explicitly]
    
    subgraph "What the Method Defines"
        I
        D
        A
        V
    end
    
    subgraph "Flexible Approach Allows"
        ID[Iterative Discovery]
        PE[Partial/Evolving Intent]
        RE[Revisiting Decisions]
        WU[Working Under Uncertainty]
    end
    
    I --> ID
    D --> RE
    A --> PE
    V --> WU
    
    style I fill:#FFD700
    style D fill:#FFD700
    style A fill:#FFD700
    style V fill:#FFD700
```

## 5.3 Why This Is Not Competing with Agile or RUP

The method does not attempt to replace:

- Scrum ceremonies
- backlog management
- sprint planning
- incremental delivery models

Nor does it attempt to revive heavyweight lifecycle frameworks such as RUP.

Those approaches define process structure.

This method defines engineering constraints and obligations that remain valid regardless of process choice.

A team may use:

- Scrum
- Kanban
- Waterfall
- ad-hoc exploratory workflows

and still apply the Explicit Software Engineering Method, provided that engineering work is made explicit, traceable, and analyzable.

```mermaid
flowchart TB
    subgraph "Layer 1: Process Choice (How Work is Organized)"
        P1[Scrum]
        P2[Kanban]
        P3[Waterfall]
        P4[Ad-hoc]
    end
    
    subgraph "Layer 2: Explicit Software Engineering Method (Engineering Constraints)"
        M1[Explicit Intent]
        M2[Traceable Decisions]
        M3[Validated Artifacts]
        M4[Evidence-based Diagnosis]
    end
    
    subgraph "Outcome"
        O[Engineered Product
with Explicit Reasoning]
    end
    
    P1 --> M1 & M2 & M3 & M4
    P2 --> M1 & M2 & M3 & M4
    P3 --> M1 & M2 & M3 & M4
    P4 --> M1 & M2 & M3 & M4
    
    M1 & M2 & M3 & M4 --> O
    
    style P1 fill:#87CEEB
    style P2 fill:#87CEEB
    style P3 fill:#87CEEB
    style P4 fill:#87CEEB
    style M1 fill:#90EE90
    style M2 fill:#90EE90
    style M3 fill:#90EE90
    style M4 fill:#90EE90
    style O fill:#FFD700
```

## 5.4 Why a Method Is Sufficient

Current gaps in software development practice are not primarily caused by missing processes.

They are caused by:

- undocumented decisions
- implicit assumptions
- untraceable artifacts
- validation detached from intent
- post-failure explanations based on narrative rather than evidence

These gaps cannot be closed by introducing another process framework.

They require a method that:

- enforces explicitness
- exposes absences
- makes trade-offs visible
- allows failure to be explained in method terms

This is the role of the Explicit Software Engineering Method.

```mermaid
graph LR
    subgraph "Current Gaps (Root Causes)"
        G1[Undocumented Decisions]
        G2[Implicit Assumptions]
        G3[Untraceable Artifacts]
        G4[Validation Detached from Intent]
        G5[Narrative-based Explanations]
    end
    
    subgraph "What's NOT Needed"
        N[Another Process Framework]
    end
    
    subgraph "What's NEEDED: A Method That"
        S1[Enforces Explicitness]
        S2[Exposes Absences]
        S3[Makes Trade-offs Visible]
        S4[Enables Evidence-based Diagnosis]
    end
    
    G1 & G2 & G3 & G4 & G5 -.cannot be closed by.-> N
    G1 --> S1
    G2 --> S1
    G3 --> S2
    G4 --> S3
    G5 --> S4
    
    S1 & S2 & S3 & S4 --> R[Recognition as
Engineered Product]
    
    style N fill:#FFB6C6,stroke:#FF0000
    style S1 fill:#90EE90
    style S2 fill:#90EE90
    style S3 fill:#90EE90
    style S4 fill:#90EE90
    style R fill:#FFD700
```

## 5.5 Summary

- **Processes organize work; the method makes engineering explicit.**
- **Agile frameworks manage delivery; the method enables diagnosis and learning.**
- **The method does not compete with processes; it constrains them.**
- **Engineering quality emerges from explicit reasoning, not from workflow choice.**

The Explicit Software Engineering Method exists to ensure that, regardless of how software is built, the result can be recognized as an engineered product rather than accidental functionality.
