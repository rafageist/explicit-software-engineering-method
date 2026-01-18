# 7. Esbozo de formalización - Método Explícito de Ingeniería de Software

Este documento proporciona un esbozo de formalización matemática y lógica del método.
Es intencionalmente mínimo y se concentra en: (1) entidades, (2) relaciones, (3) obligaciones normativas y (4) diagnosabilidad.
Describe restricciones sobre artefactos explícitos y relaciones, no un flujo de trabajo prescriptivo.
El objetivo es evaluabilidad y diagnosabilidad, no completitud matemática.

La formalización busca **objetividad operativa bajo contexto explícito**, no objetividad absoluta.

---

Antes de enunciar obligaciones, debemos fijar un universo de discurso. Sin un universo declarado, las restricciones no tienen objetivos estables y la evaluación se vuelve ambigua.

## 7.1 Universo de discurso

Modelamos el trabajo de ingeniería como un conjunto de entidades y relaciones tipadas.

### 7.1.1 Conjuntos de entidades

Sea la existencia de los siguientes conjuntos:

- **I** : conjunto de *Intenciones*
- **D** : conjunto de *Decisiones*
- **A** : conjunto de *Artefactos*
- **S** : conjunto de *Supuestos*
- **T** : conjunto de *Trade-offs*
- **V** : conjunto de *Validaciones*
- **C** : conjunto de *Compensaciones*
- **Ch** : conjunto de *Cambios* (cambios de ingeniería)
- **P** : conjunto de *Parámetros* (entradas contextuales)

Definimos el conjunto global de entidades:

- **E = I ∪ D ∪ A ∪ S ∪ T ∪ V ∪ C ∪ Ch ∪ P**

### 7.1.2 Predicados (tipado)

Usamos predicados unarios para tipar entidades:

- Intent(x), Decision(x), Artifact(x), Assumption(x), TradeOff(x), Validation(x), Compensation(x), Change(x), Parameter(x)

---

El razonamiento de ingeniería se captura mediante relaciones entre estas entidades, no mediante una secuencia impuesta. Un modelo de grafo hace explícita la trazabilidad sin prescribir orden.

## 7.2 Relaciones núcleo (modelo de grafo)

El razonamiento de ingeniería se representa como un multigrafo dirigido tipado sobre E.

### 7.2.1 Relaciones fundamentales

- **declares ⊆ Ch × I**  
  `declares(ch, i)` significa que el cambio `ch` declara la intención `i`.

- **serves ⊆ D × I**  
  `serves(d, i)` significa que la decisión `d` sirve a la intención `i`.

- **justifies ⊆ A × (I ∪ D)**  
  `justifies(a, x)` significa que el artefacto `a` está justificado por la intención o decisión `x`.

- **assumes ⊆ (D ∪ A) × S**  
  `assumes(x, s)` significa que la entidad `x` depende del supuesto `s`.

- **tradesOff ⊆ (D ∪ A) × T**  
  `tradesOff(x, t)` significa que la entidad `x` involucra el trade-off `t`.

- **validates ⊆ V × (A ∪ D ∪ I)**  
  `validates(v, x)` significa que la validación `v` aporta evidencia para la entidad `x`.

- **compensates ⊆ C × (I ∪ D ∪ A ∪ V)**  
  `compensates(c, x)` significa que la compensación `c` compensa explícitamente x faltante o insuficiente.

- **paramOf ⊆ P × Ch**  
  `paramOf(p, ch)` significa que el parámetro `p` aplica al cambio `ch` (o al alcance del proyecto que lo contiene).

### 7.2.2 Trazabilidad (derivada)

Definimos una relación derivada **traceableTo(x, y)** como la existencia de un camino desde x hasta y usando bordes permitidos.
Como mínimo, el grafo de trazabilidad usa los bordes:
- declares, serves, justifies, validates, assumes, tradesOff

Los requisitos de trazabilidad del método restringen la existencia de esos caminos y su navegabilidad.

---

La lógica de primer orden se usa aquí para expresar invariantes sobre el grafo. Son restricciones a evaluar, no cálculos a ejecutar.

## 7.3 Axiomas / invariantes de lógica de primer orden (FOL)

El método se expresa como restricciones que deben cumplirse independientemente de la secuencia de trabajo, reflejando la ortogonalidad al orden del proceso. Estas restricciones corresponden directamente a las reglas normativas definidas anteriormente.

A continuación, `∀` significa "para todo" y `∃` significa "existe".

Las reglas 1-3 establecen la explicitud y la trazabilidad mínimas para intención, decisiones y artefactos.

### 7.3.1 Regla 1 - Declaración de intención (obligatoria)

Para cualquier cambio no trivial, debe declararse una intención:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) → ∃i (Intent(i) ∧ declares(ch, i) ∧ Scoped(i)) )

Si un cambio no trivial no tiene intención declarada, es trabajo implícito:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) ∧ ¬∃i (Intent(i) ∧ declares(ch, i)) → ImplicitWork(ch) )

### 7.3.2 Regla 2 - Explicitación de decisiones (obligatoria)

Para cualquier decisión de impacto, debe servir a una intención (o compensarse explícitamente):

- ∀d ( Decision(d) ∧ Impactful(d) → 
       (?i (Intent(i) ? serves(d, i)) ? ?c (Compensation(c) ? compensates(c, d))) )

Y las decisiones que no sirven a una intención se tratan como supuestos salvo que se compensen:

- ∀d ( Decision(d) ∧ Impactful(d) ∧ ¬∃i (Intent(i) ∧ serves(d, i)) ∧ ¬∃c (Compensation(c) ∧ compensates(c, d))
       ? ?s (Assumption(s) ? AssumptionByDefault(d, s)) )

### 7.3.3 Regla 3 - Trazabilidad de artefactos (obligatoria)

Todo artefacto que afecta el comportamiento debe trazar a una intención o decisión:

- ∀a ( Artifact(a) ∧ AffectsBehavior(a) → 
       (?x ((Intent(x) ? Decision(x)) ? justifies(a, x)) ? ?c (Compensation(c) ? compensates(c, a))) )

Los artefactos huérfanos son injustificados:

- ∀a ( Artifact(a) ∧ AffectsBehavior(a) ∧ ¬∃x ((Intent(x) ∨ Decision(x)) ∧ justifies(a, x))
       ? Orphan(a) )

Las reglas 4-6 cubren validación, supuestos y compensación bajo riesgo contextual.

### 7.3.4 Regla 4 - Requisito de validación (contextual)

Los elementos críticos requieren validación, con criticidad dependiente de parámetros:

- ∀x ( Critical(x) → (∃v (Validation(v) ∧ validates(v, x)) ∨ ∃c (Compensation(c) ∧ compensates(c, x))) )

Critical(x) no es fijo; se deriva de parámetros:

- ∀x ( Critical(x) ↔ CriticalUnderParams(x, ParamsScope(x)) )

Los parámetros son entradas de evaluación. Determinan qué cuenta como crítico y qué profundidad de validación se requiere; no excusan obligaciones.

### 7.3.5 Regla 5 - Declaración de supuestos (obligatoria)

Cuando falta o se difiere evidencia, los supuestos deben ser explícitos:

- ∀x ( EvidenceMissing(x) → ∃s (Assumption(s) ∧ assumes(x, s) ∧ Explicit(s)) )

### 7.3.6 Regla 6 - Compensación explícita (obligatoria)

Cuando falta un elemento requerido, debe existir compensación y declarar el riesgo aceptado:

- ∀x ( Required(x) ∧ Missing(x) → ∃c (Compensation(c) ∧ compensates(c, x) ∧ StatesAcceptedRisk(c)) )

La regla 7 hace explícito el contexto para que la evaluación sea reproducible entre equipos y en el tiempo.

### 7.3.7 Regla 7 - Conciencia de parámetros (obligatoria)

Cada alcance relevante debe declarar los parámetros aplicables:

- ∀ch ( Change(ch) ∧ NonTrivial(ch) → ∃p (Parameter(p) ∧ paramOf(p, ch)) )

Los parámetros afectan las obligaciones al definir umbrales y alcances; no son perillas de ajuste para la corrección.

La regla 8 vincula las restricciones con la diagnosabilidad, alineando el método con el análisis de fallos.

### 7.3.8 Regla 8 - Diagnosabilidad del fallo (regla de resultado)

Para cualquier fallo observado f, debe identificarse al menos una explicación a nivel de método:

- ∀f ( Failure(f) → ∃r (Reason(r) ∧ ExplainsInMethodTerms(r, f)) )

Razones mínimas admisibles:

ExplainsInMethodTerms(r, f) implica al menos uno de:
- MissingIntent(f)
- InvalidDecision(f)
- UnvalidatedArtifact(f)
- FalseAssumption(f)
- InadequateCompensation(f)
- MisconfiguredParameters(f)

---

## 7.4 Capa deóntica (obligaciones, permisos, consecuencias)

Los invariantes de FOL describen condiciones de verdad. El método es normativo: incluye obligaciones.
Los operadores deónticos O, P y R son capas interpretativas sobre los invariantes; no reemplazan ni amplían las restricciones de FOL.
Lo modelamos con un operador deóntico:

- **O(φ)** : es obligatorio que φ se cumpla (DEBE)
- **P(φ)** : es permitido que φ se cumpla (PUEDE)
- **R(φ)** : es recomendable que φ se cumpla (DEBERÍA)

### 7.4.1 DEBE como obligación

Ejemplo (Regla 1):

- O( Change(ch) ∧ NonTrivial(ch) → ∃i (Intent(i) ∧ declares(ch,i) ∧ Scoped(i)) )

### 7.4.2 Compensación como permiso bajo obligación

El método permite atajos solo si se compensan:

- P( Missing(x) )  IF  O( ∃c (Compensation(c) ∧ compensates(c, x) ∧ StatesAcceptedRisk(c)) )

Esto expresa: pueden faltar artefactos o validación, pero solo bajo compensación explícita.
La compensación es permiso bajo obligación; registra riesgo aceptado y no elimina la obligación.

### 7.4.3 Consecuencias (semántica de violación)

Definimos un predicado de violación:

- Violation(rule_k, scope)

Por ejemplo:

- ¬∃i (Intent(i) ∧ declares(ch,i))  implies  Violation(Rule1, ch)

Una verificación de cumplimiento es entonces una función del estado del repositorio al conjunto de violaciones:

- Violations(State) = { (rule_k, scope) | State ⊭ rule_k(scope) }

Esta es la base para herramientas sin prescribir flujo de trabajo.

---

## 7.5 Cumplimiento mínimo y diagnosabilidad como funciones

### 7.5.1 Función de cumplimiento

Dado un estado que contiene entidades y relaciones:

- **Compliant(State)** iff Violations(State) = ∅

### 7.5.2 Función de diagnosabilidad

Dado un fallo f y un estado:

- **Diagnosable(f, State)** iff ∃r ExplainsInMethodTerms(r, f)

Esto puede implementarse consultando el grafo explícito en busca de enlaces faltantes, validación faltante, compensación faltante o desajustes de parámetros. Es la contraparte formal del requisito de diagnosabilidad discutido antes.

---

## 7.6 Notas prácticas (no normativas)

Este nivel de formalización es suficiente para soportar evaluación objetiva, diagnóstico de fallos e implementación de herramientas sin prescribir flujo de trabajo.
- Esta formalización es compatible con bases de datos de grafos y verificación de restricciones.
- Es intencionalmente independiente de cualquier proceso de desarrollo o ciclo de vida específico.
- Las lógicas temporales (por ejemplo, TLA+) y la semántica de ejecución pueden introducirse más adelante para modelar evolución, reconstrucción post hoc o concurrencia, pero se excluyen intencionalmente del núcleo del método.

---
