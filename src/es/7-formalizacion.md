# 7. Esbozo de formalización - Método Explícito de Ingeniería de Software

Este capítulo proporciona una formalización matemática y lógica del método.
Es intencionalmente mínimo y se concentra en: (1) entidades, (2) relaciones, (3) obligaciones normativas, (4) evaluación con evidencia incompleta y (5) diagnosabilidad.
Describe restricciones sobre registros explícitos y relaciones, no un flujo de trabajo prescriptivo.
El objetivo es evaluabilidad y diagnosabilidad, no completitud matemática.

La formalización busca **objetividad operativa bajo contexto explícito**, no objetividad absoluta. Dos evaluadores que usan la misma versión del método, el mismo alcance evaluado, el mismo conjunto de parámetros, la misma instantánea de evidencia, el mismo instante de evaluación y los mismos juicios registrados obtienen los mismos resultados (7.6). Contextos distintos, o juicios distintos donde una política requiere juicio, pueden conducir legítimamente a resultados distintos.

---

## 7.0 Estatus de los enunciados

Los enunciados de este capítulo se etiquetan según su estatus:

- **Definición.** Parte de la semántica formal del método. Las definiciones marcadas *(propuesta, OD-n)* dependen de una decisión abierta (`docs/open-decisions.md`).
- **Proposición.** Una propiedad que se sigue de las definiciones. Los argumentos se dan de manera informal; no son demostraciones verificadas por máquina.
- **Esbozo.** Una dirección conceptual que no forma parte de la semántica de evaluación.
- **Ejemplo.** Solo ilustrativo.

La versión 0.2.1 de este capítulo contenía invariantes que, leídos literalmente, hacían indistinguibles los estados compensados de los satisfechos y trataban la evidencia faltante como prueba de ausencia. La sección 7.3.9 enumera cada cambio respecto a 0.2.1 y su motivo.

---

Antes de enunciar obligaciones, debemos fijar un universo de discurso. Sin un universo declarado, las restricciones no tienen objetivos estables y la evaluación se vuelve ambigua.

## 7.1 Universo de discurso

Modelamos el trabajo de ingeniería como un conjunto de entidades y relaciones tipadas.

### 7.1.1 Conjuntos de entidades

**Definición 7.1 (conjuntos de entidades).** Sea la existencia de los siguientes conjuntos finitos:

- $I$: *Intenciones*
- $D$: *Decisiones*
- $A$: *Versiones de artefactos*
- $S$: *Supuestos* (premisas de las que se depende)
- $T$: *Trade-offs*
- $V$: *Validaciones*
- $C$: *Compensaciones*
- $Ch$: *Cambios* (cambios de ingeniería)
- $P$: *Parámetros* (descriptores de contexto y políticas)
- $G$: *Agentes* (personas o roles que registran, valoran o aceptan)
- $F$: *Fallos* (fallos observados)

y el conjunto global de entidades $E = I \cup D \cup A \cup S \cup T \cup V \cup C \cup Ch \cup P \cup G \cup F$.

Los conjuntos son disjuntos dos a dos. Las entidades se tipan por el papel que desempeñan en el razonamiento de ingeniería, no por cómo se almacenan. Una decisión escrita en un archivo Markdown es un elemento de $D$, no de $A$.

Los elementos de $A$ son *versiones*: un archivo fuente en dos commits da dos elementos de $A$. La relación $\mathsf{supersedes} \subseteq A \times A$ vincula una versión con su predecesora.

$D$ contiene las decisiones registradas y también las elecciones identificadas por revisión o por análisis de fallos para las que no existe registro. El predicado $\mathsf{Recorded}(d)$ las distingue. Del mismo modo, $S$ contiene los supuestos declarados y las premisas identificadas como base de una dependencia sin haber sido declaradas; $\mathsf{Declared}(s)$ las distingue. Los elementos no registrados son el objeto de la evaluación de las Reglas 2 y 5 (revisión F-03, F-09).

### 7.1.2 Predicados (tipado)

Usamos predicados unarios para tipar entidades: $\mathsf{Intent}(x)$, $\mathsf{Decision}(x)$, $\mathsf{Artifact}(x)$, $\mathsf{Assumption}(x)$, $\mathsf{TradeOff}(x)$, $\mathsf{Validation}(x)$, $\mathsf{Compensation}(x)$, $\mathsf{Change}(x)$, $\mathsf{Parameter}(x)$, $\mathsf{Agent}(x)$, $\mathsf{Failure}(x)$. Cuando una variable lleva el nombre de un conjunto (por ejemplo $ch$, $d$, $a$), su tipo queda implícito y se omite el predicado de tipado.

### 7.1.3 Atributos de los registros

**Definición 7.2 (atributos de los registros).** Todo elemento $x \in E$ que es un registro tiene:

- $\mathrm{src}(x)$: la fuente de evidencia que lo contiene;
- $\tau(x)$: el instante en que se registró;
- $\mathrm{prov}(x) \in \{\textit{contemporánea}, \textit{retrospectiva}, \textit{reconstruida}, \textit{inferida}\}$: su procedencia (8.4);
- $\mathrm{acc}(x) \in \{\textit{accesible}, \textit{inaccesible}\}$: si el evaluador puede leer su contenido.

---

El razonamiento de ingeniería se captura mediante relaciones entre estas entidades, no mediante una secuencia impuesta. Un modelo de grafo hace explícita la trazabilidad sin prescribir orden.

## 7.2 Relaciones núcleo (modelo de grafo)

El razonamiento de ingeniería se representa como un multigrafo dirigido tipado sobre $E$.

### 7.2.1 Relaciones fundamentales

**Definición 7.3 (relaciones).**

| Relación | Signatura | Lectura |
|---|---|---|
| $\mathsf{declares}(ch, i)$ | $Ch \times I$ | el cambio $ch$ declara la intención $i$ |
| $\mathsf{modifies}(ch, a)$ | $Ch \times A$ | el cambio $ch$ produce la versión de artefacto $a$ |
| $\mathsf{serves}(d, i)$ | $D \times I$ | la decisión $d$ sirve a la intención $i$ |
| $\mathsf{justifies}(a, x)$ | $A \times (I \cup D)$ | el artefacto $a$ está justificado por la intención o decisión $x$ |
| $\mathsf{derivedFrom}(a, b)$ | $A \times A$ | $a$ se genera o deriva de $b$ (p. ej., código a partir de un modelo) |
| $\mathsf{assumes}(x, s)$ | $(D \cup A) \times S$ | $x$ consta en el registro como dependiente del supuesto $s$ |
| $\mathsf{relies}(x, s)$ | $(D \cup A) \times S$ | $x$ depende de $s$, según se establece por revisión o análisis |
| $\mathsf{tradesOff}(x, t)$ | $(D \cup A) \times T$ | $x$ involucra el trade-off $t$ |
| $\mathsf{validates}(v, x)$ | $V \times (A \cup D \cup I)$ | la validación $v$ aporta evidencia para $x$ |
| $\mathsf{equiv}(a, b)$ | $A \times A$ | el registro declara $b$ equivalente a $a$ a efectos de validación |
| $\mathsf{compensates}(c, o)$ | $C \times O$ | la compensación $c$ cubre la instancia de obligación $o$ (7.2.3) |
| $\mathsf{acceptedBy}(c, g)$ | $C \times G$ | el agente $g$ aceptó el riesgo declarado en $c$ |

La versión 0.2.1 tenía $\mathsf{compensates} \subseteq C \times (I \cup D \cup A \cup V)$, lo que exige que el elemento faltante exista para poder compensarlo (revisión F-10). Las compensaciones ahora tienen como objetivo instancias de obligación. La relación $\mathsf{paramOf} \subseteq P \times Ch$ de 0.2.1 se sustituye por la vinculación de un conjunto de parámetros a la aplicación del método (7.2.4).

$\mathsf{assumes}$ forma parte del registro; $\mathsf{relies}$ es un hallazgo. La diferencia entre ambas es lo que evalúa la Regla 5.

### 7.2.2 Trazabilidad (derivada)

**Definición 7.4 (caminos de justificación).** Sea $x \to_J y$ verdadero si y solo si $\mathsf{justifies}(x,y) \lor \mathsf{serves}(x,y) \lor \mathsf{derivedFrom}(x,y)$. Entonces $\mathsf{traceableTo}$ es la clausura reflexiva y transitiva $\to_J^{*}$.

Para la Regla 3 solo se usan aristas de justificación: un artefacto no queda *justificado* por la prueba que lo valida ni por el supuesto del que depende. El grafo de trazabilidad completo incluye además aristas $\mathsf{declares}$, $\mathsf{modifies}$, $\mathsf{validates}$, $\mathsf{assumes}$ y $\mathsf{tradesOff}$, y se usa para la navegación y el diagnóstico (7.7).

**Proposición 7.1.** $\mathsf{traceableTo}$ no es definible en lógica de primer orden sobre las relaciones anteriores, porque la clausura transitiva no es definible en primer orden [Aho and Ullman 1979]. Por ello las reglas usan lógica de primer orden extendida con un operador de clausura transitiva (equivalentemente, una consulta recursiva). La evaluación sobre un registro finito sigue siendo polinómica en su tamaño. La versión 0.2.1 definía la relación de camino pero no la usaba (revisión F-05).

**Navegabilidad bidireccional.** Cualquier relación del modelo puede leerse en ambas direcciones, de modo que el requisito de la Regla 3 no es una propiedad del grafo. Restringe la representación: $\mathsf{Navigable}(x, y)$ se cumple cuando, usando solo las fuentes de evidencia declaradas, el vínculo puede resolverse partiendo de $x$ y partiendo de $y$ (8.4).

### 7.2.3 Instancias de obligación

**Definición 7.5 (sujetos e instancias).** Las reglas $\mathcal{R} = \{R1, \dots, R8\}$ de la versión de conjunto de reglas $\rho$ tienen los siguientes dominios de sujetos:

| Regla | Dominio de sujetos |
|---|---|
| R1 | $Ch$ |
| R2 | $D$ |
| R3 | $A$ |
| R4 | $A \cup D$ (OD-12) |
| R5 | $S$ |
| R7 | $\{\alpha\}$, la aplicación del método |
| R8 | $F$ |

El conjunto de instancias de obligación es $O = \{\langle k, x \rangle \mid k \in \mathcal{R},\ k \ne R6,\ x \in \mathrm{Subj}_k \cap \mathrm{scope}(\alpha)\}$. La Regla 6 no tiene sujetos propios; es una regla sobre los resultados de otras instancias (7.4).

### 7.2.4 Los parámetros como interpretaciones

**Definición 7.6 (predicados de política).** Las reglas usan un conjunto fijo de *predicados de política*:

$$\begin{aligned}\mathcal{P}_{pol} = \{&\mathsf{NonTrivial},\ \mathsf{Impactful},\ \mathsf{Irreversible},\ \mathsf{Balances},\ \mathsf{AffectsBehavior},\\ &\mathsf{Critical},\ \mathsf{Adequate},\ \mathsf{Admissible},\ \mathsf{MayAccept},\ \mathsf{PermitsPermanent}\}\end{aligned}$$

Un conjunto de parámetros $\Pi = (\Delta, \Lambda)$ consta de descriptores de contexto $\Delta$ (criticidad del dominio, tolerancia al riesgo, presión regulatoria, escala del equipo, vida útil esperada, ...) y de políticas $\Lambda$. Cada política da una interpretación de uno o más predicados de política. Una interpretación puede ser *parcial*: una política puede dejar casos sin decidir, y una política ausente deja su predicado sin decidir en todos los casos.

Así es como el método puede depender del contexto sin tener reglas que dependan del contexto. Las fórmulas de las reglas son fijas para una versión del conjunto de reglas; el conjunto de parámetros fija lo que significan los predicados de política en un contexto. Dos aplicaciones con conjuntos de parámetros distintos evalúan las mismas fórmulas bajo interpretaciones distintas.

Una política puede ser mecánica (por ejemplo, "un artefacto es crítico si y solo si está bajo `payments/`") o requerir juicio (por ejemplo, "una decisión es de impacto si restringe una interfaz pública"). Un juicio se registra como una *valoración*, con su autor y el registro al que se refiere, y pasa a ser una entrada de la evaluación (7.6). Una evaluación nunca vuelve a juzgar en silencio.

---

La lógica de primer orden se usa aquí para expresar invariantes sobre el grafo. Son restricciones a evaluar, no cálculos a ejecutar.

## 7.3 Las reglas como aplicabilidad y requisito

El método se expresa como restricciones que deben cumplirse independientemente de la secuencia de trabajo, reflejando la ortogonalidad al orden del proceso. Estas restricciones corresponden directamente a las reglas normativas del capítulo 3.

**Definición 7.7 (forma de las reglas).** Cada regla $k \in \mathcal{R}$ distinta de R6 y R8 es un par de fórmulas con una variable libre $x$ para su sujeto: una *condición de aplicabilidad* $\mathrm{App}_k(x)$ y un *requisito* $\mathrm{Req}_k(x)$. El invariante de 0.2.1 para la regla $k$ corresponde a

$$\forall x\ (\mathrm{App}_k(x) \rightarrow \mathrm{Req}_k(x))$$

sin el disyunto de compensación. La compensación se trata en la función de resultado (7.5), de modo que nunca pueda hacer verdadero un requisito (revisión F-15).

### 7.3.1 Regla 1 - Declaración de intención

$$\mathrm{App}_1(ch) \equiv \mathsf{NonTrivial}(ch) \qquad \mathrm{Req}_1(ch) \equiv \exists i\ (\mathsf{declares}(ch, i) \land \mathsf{Scoped}(i))$$

$\mathsf{Scoped}(i)$ se cumple cuando el registro de la intención indica la parte del sistema, las partes interesadas o el atributo de calidad afectados. La consecuencia $\mathsf{ImplicitWork}(ch)$ de 0.2.1 es el nombre del caso $\mathrm{App}_1(ch) \land \lnot \mathrm{Req}_1(ch)$.

### 7.3.2 Regla 2 - Explicitación de decisiones

$$\mathrm{App}_2(d) \equiv \mathsf{Impactful}(d) \lor \mathsf{Irreversible}(d)$$

$$\mathrm{Req}_2(d) \equiv \mathsf{Recorded}(d) \land \exists i\ \mathsf{serves}(d, i) \land \mathsf{AltsRecorded}(d) \land (\mathsf{Balances}(d) \rightarrow \exists t\ \mathsf{tradesOff}(d, t))$$

$\mathsf{AltsRecorded}(d)$ se cumple cuando el registro enumera las alternativas consideradas o declara que no se evaluó ninguna y por qué *(propuesta, OD-3)*. El último conjunto *(propuesta, OD-4)* exige el trade-off aceptado cuando la decisión equilibra atributos en competencia; sin OD-4 se omite.

Para una decisión no registrada, $\mathrm{Req}_2(d)$ es falso. Tratarla "como supuesto por defecto" es una clasificación usada en el diagnóstico (7.7), no una manera de satisfacer $\mathrm{Req}_2$ *(propuesta, OD-2)*.

### 7.3.3 Regla 3 - Trazabilidad de artefactos

$$\mathrm{App}_3(a) \equiv \mathsf{AffectsBehavior}(a)$$

$$\mathrm{Req}_3(a) \equiv \exists y\ \big((\mathsf{Intent}(y) \lor \mathsf{Decision}(y)) \land \mathsf{Recorded}(y) \land \mathsf{traceableTo}(a, y) \land \mathsf{Navigable}(a, y)\big)$$

La consecuencia $\mathsf{Orphan}(a)$ de 0.2.1 es el nombre del caso $\mathrm{App}_3(a) \land \lnot \mathrm{Req}_3(a)$.

### 7.3.4 Regla 4 - Requisito de validación

$$\mathrm{App}_4(x) \equiv \mathsf{Critical}(x)$$

$$\mathrm{Req}_4(x) \equiv \exists v\ \exists x'\ \big(\mathsf{validates}(v, x') \land (x' = x \lor \mathsf{equiv}(x', x)) \land \mathsf{Passed}(v) \land \mathsf{Adequate}(v, x)\big)$$

Tres condiciones son nuevas respecto a 0.2.1 (revisión F-08). La validación queda ligada a una versión, porque los elementos de $A$ son versiones. La validación debe haber resultado satisfactoria: una ejecución de pruebas fallida es evidencia, pero no evidencia de que $x$ satisface su intención. La adecuación la decide la política de adecuación de la validación, lo que hace operativa la "profundidad de validación" de la Regla 7.

### 7.3.5 Regla 5 - Declaración de supuestos

$$\mathrm{App}_5(s) \equiv \exists x\ \mathsf{relies}(x, s) \land \lnot \exists v\ (\mathsf{validates}(v, s) \land \mathsf{Passed}(v))$$

$$\mathrm{Req}_5(s) \equiv \mathsf{Declared}(s) \land \forall x\ (\mathsf{relies}(x, s) \rightarrow \mathsf{assumes}(x, s))$$

La fórmula de 0.2.1 $\forall x\ (\mathsf{EvidenceMissing}(x) \rightarrow \exists s\ \mathsf{assumes}(x,s))$ cuantificaba sobre todas las entidades y no podía distinguir una premisa declarada de una no declarada (revisión F-09). El DEBERÍA sobre el seguimiento es una recomendación (7.4): un supuesto cuyo estado no se sigue se informa, pero no es una violación.

### 7.3.6 Regla 6 - Compensación explícita

La Regla 6 no tiene sujeto propio. Es la obligación contraria al deber asociada a las demás reglas (7.4.2), y su efecto queda definido por la validez de las compensaciones y la función de resultado (7.5).

### 7.3.7 Regla 7 - Conciencia de parámetros

$$\mathrm{App}_7(\alpha) \equiv \top \qquad \mathrm{Req}_7(\alpha) \equiv \mathsf{Explicit}(\Pi_\alpha) \land \mathsf{Versioned}(\Pi_\alpha) \land \mathsf{Covers}(\Pi_\alpha, \mathcal{P}_{pol})$$

$\mathsf{Covers}$ *(propuesta, OD-9)* exige una política para cada predicado de política. Sin OD-9 se omite el último conjunto. La fórmula de 0.2.1 $\forall ch\ \exists p\ \mathsf{paramOf}(p, ch)$ se satisfacía con cualquier parámetro aislado (revisión F-12).

### 7.3.8 Regla 8 - Diagnosabilidad del fallo

La Regla 8 se evalúa por fallo y depende de la clasificación definida en 7.7.

### 7.3.9 Matriz regla-predicado y cambios respecto a 0.2.1

| Regla | Sujeto | $\mathrm{App}_k$ (política) | $\mathrm{Req}_k$ | Compensable (OD-5) | Cambio respecto a 0.2.1 |
|---|---|---|---|---|---|
| R1 | $ch \in Ch$ | $\mathsf{NonTrivial}$ | intención con alcance declarada | no | aplicabilidad ligada a una política |
| R2 | $d \in D$ | $\mathsf{Impactful} \lor \mathsf{Irreversible}$ | registrada, sirve a una intención, alternativas, trade-off | sí | se añaden irreversibilidad, alternativas y trade-off; la compensación sale de la fórmula |
| R3 | $a \in A$ | $\mathsf{AffectsBehavior}$ | camino de justificación, navegable | sí | camino en lugar de arista directa; la compensación sale de la fórmula |
| R4 | $x \in A \cup D$ | $\mathsf{Critical}$ | validación satisfactoria y adecuada de la misma versión | sí | se añaden versión, resultado y adecuación; dominio restringido |
| R5 | $s \in S$ | se depende de él, sin validar | declarado y vinculado | sí | cuantifica sobre premisas, no sobre todas las entidades |
| R6 | resultados de R1-R5, R7 | — | compensación válida | — | apunta a instancias de obligación |
| R7 | $\alpha$ | siempre | conjunto de parámetros explícito, versionado y completo | no | dirigida a la aplicación |
| R8 | $f \in F$ | fallo dentro del alcance | todo factor clasificado | — | clasificación en lugar de una única razón |

---

## 7.4 Capa deóntica (obligaciones, permisos, consecuencias)

Los invariantes de FOL describen condiciones de verdad. El método es normativo: incluye obligaciones.
Los operadores deónticos [von Wright 1951] son capas interpretativas sobre los invariantes; no reemplazan ni amplían las restricciones subyacentes.

- $\mathbf{O}(\varphi \mid \psi)$: dado $\psi$, es obligatorio que $\varphi$ (DEBE)
- $\mathbf{P}(\varphi \mid \psi)$: dado $\psi$, está permitido que $\varphi$ (PUEDE)
- $\mathbf{R}(\varphi \mid \psi)$: dado $\psi$, es recomendable que $\varphi$ (DEBERÍA)

### 7.4.1 DEBE como obligación condicional

**Definición 7.8.** Para cada regla $k$ con aplicabilidad y requisito:

$$\mathbf{O}\big(\mathrm{Req}_k(x) \mid \mathrm{App}_k(x)\big)$$

Ejemplo (Regla 1): $\mathbf{O}\big(\exists i\ (\mathsf{declares}(ch,i) \land \mathsf{Scoped}(i)) \mid \mathsf{NonTrivial}(ch)\big)$.

### 7.4.2 La compensación como obligación contraria al deber

La versión 0.2.1 escribía "$P(\mathsf{Missing}(x))$ IF $O(\exists c \ldots)$", que no es una fórmula deóntica bien formada. Lo que describe la prosa es una obligación *contraria al deber*: una obligación que surge porque se ha violado otra obligación [Chisholm 1963].

**Definición 7.9.** Para cada regla compensable $k \in K$, donde $K$ es el conjunto de reglas compensables, *(propuesta, OD-5: $K = \{R2, R3, R4, R5\}$)*:

$$\mathbf{O}\big(\exists c\ \mathsf{Valid}_t(c, \langle k, x\rangle) \mid \mathrm{App}_k(x) \land \lnot \mathrm{Req}_k(x)\big)$$

La obligación primaria $\mathbf{O}(\mathrm{Req}_k \mid \mathrm{App}_k)$ no se retira cuando se cumple la secundaria. Ese es el contenido formal de "la compensación no elimina la obligación".

Se sabe que las estructuras contrarias al deber producen paradojas cuando se razona con ellas dentro de la lógica deóntica estándar. El método lo evita al no razonar *dentro* de una lógica deóntica. Los operadores son una lectura de la función de resultado (7.5), que se define directamente sobre el registro. Evaluar el método no requiere ninguna inferencia deóntica.

### 7.4.3 Recomendaciones

Una recomendación $\mathbf{R}(\varphi \mid \psi)$ que no se sigue produce una *nota* en la evaluación, no un resultado. Ejemplo: un supuesto sin estado de seguimiento (Regla 5, DEBERÍA).

---

## 7.5 Evaluación con evidencia incompleta

La semántica clásica de primer orden supone un modelo completo: un vínculo que no está en el estado es falso. Aplicado a la evaluación, esto trata la falta de acceso del evaluador como falta de trabajo del equipo (revisión F-16). Por ello el método evalúa las fórmulas en una semántica trivalente sobre un registro *parcial* con completitud declarada.

### 7.5.1 Instantánea y completitud

**Definición 7.10 (instantánea).** Una instantánea $\Sigma$ es la estructura finita de entidades, relaciones y atributos obtenida de las fuentes de evidencia declaradas en las líneas base declaradas (7.6).

**Definición 7.11 (declaración de completitud).** Para un símbolo de relación $r$ y una parte del alcance $\sigma$, el contrato de evaluación puede declarar $\mathsf{Complete}(r, \sigma)$: toda instancia verdadera de $r$ cuyo primer argumento pertenece a $\sigma$ está en $\Sigma$. Es un *supuesto de mundo cerrado local* [Reiter 1978; Etzioni, Golden and Weld 1997]. Es una afirmación que hace la evaluación, queda registrada en el contrato y puede ser errónea.

### 7.5.2 Evaluación trivalente

**Definición 7.12.** Sean los valores de verdad $\{\mathbf{t}, \mathbf{u}, \mathbf{f}\}$ con $\mathbf{f} < \mathbf{u} < \mathbf{t}$. El valor $\mathrm{val}_\Sigma(\varphi)$ se define así:

- *Átomos del registro.* $\mathrm{val}(r(\bar a)) = \mathbf{t}$ si $r(\bar a) \in \Sigma$ y todo registro del que depende es accesible. Es $\mathbf{f}$ si $r(\bar a) \notin \Sigma$ y $\mathsf{Complete}(r, \sigma)$ está declarado para la parte del alcance que contiene $\bar a$. Es $\mathbf{u}$ en otro caso.
- *Predicados de política.* El valor que da la política en $\Pi$, o $\mathbf{u}$ si la política falta o no decide el caso.
- *Conectivas* (Kleene fuerte [Kleene 1952]): $\mathrm{val}(\lnot\varphi)$ intercambia $\mathbf{t}$ y $\mathbf{f}$ y mantiene $\mathbf{u}$; $\mathrm{val}(\varphi \land \psi) = \min$; $\mathrm{val}(\varphi \lor \psi) = \max$; $\varphi \rightarrow \psi \equiv \lnot\varphi \lor \psi$.
- *Cuantificadores.* $\mathrm{val}(\exists x\, \varphi) = \mathbf{t}$ si algún $x$ conocido da $\mathbf{t}$. Es $\mathbf{f}$ si todos los $x$ conocidos dan $\mathbf{f}$ y el dominio de $x$ está declarado completo. Es $\mathbf{u}$ en otro caso. $\forall$ es dual.

**Proposición 7.2 (ninguna violación por ignorancia).** Si no se declara completitud para las relaciones de las que depende un requisito, un requisito existencial puede evaluarse como $\mathbf{t}$ o $\mathbf{u}$, pero nunca como $\mathbf{f}$. La evidencia ausente se convierte en evidencia negativa solo donde la evaluación afirma explícitamente la completitud.

**Proposición 7.3 (monotonía).** Sea $\Sigma \subseteq \Sigma'$, donde $\Sigma'$ añade registros solo en lugares para los que no se declaró completitud y no añade políticas que contradigan las existentes. Entonces todo valor $\mathbf{t}$ o $\mathbf{f}$ bajo $\Sigma$ se mantiene bajo $\Sigma'$; solo pueden cambiar los valores $\mathbf{u}$. Si una evidencia nueva cambia un $\mathbf{f}$, una declaración de completitud era falsa, y la evaluación anterior debe corregirse, no solo actualizarse. (Argumento: las conectivas de Kleene fuerte y las cláusulas de los cuantificadores son monótonas en el orden de información $\mathbf{u} \sqsubset \mathbf{t}, \mathbf{f}$.)

### 7.5.3 Validez de las compensaciones

**Definición 7.13.** Una compensación $c$ es válida en el instante de evaluación $t$ para la instancia $o = \langle k, x\rangle$ si y solo si:

$$\begin{aligned}\mathsf{Valid}_t(c, o) \equiv\ & \mathsf{compensates}(c, o) \land \mathsf{StatesRisk}(c) \land \mathsf{Admissible}(c, o)\\ & \land \exists g\ \big(\mathsf{acceptedBy}(c, g) \land \mathsf{MayAccept}(g, o)\big) \land \tau(c) \le t \land \mathsf{Unexpired}_{t_x}(c)\end{aligned}$$

donde $t_x = \min(t, \mathrm{end}(x))$, y $\mathrm{end}(x)$ es el instante en que el sujeto salió de operación (fue sustituido, retirado o revertido), o $\infty$ si sigue en operación. $\mathsf{Unexpired}_{t_x}(c)$ se cumple si la condición de revisión de $c$ no se había alcanzado en $t_x$, o si $c$ no tiene plazo y se cumple $\mathsf{PermitsPermanent}(o)$ *(propuesta, OD-6)*. $\mathsf{MayAccept}$ lo decide la política de autoridad *(propuesta, OD-7)*.

Usar $t_x$ significa que una compensación cubre la exposición de su sujeto. Si una versión de hotfix se sustituye antes de que expire su compensación, la instancia del hotfix sigue *compensada* en evaluaciones posteriores. Si la compensación expira mientras la versión sigue en operación, la instancia queda *violada*, y así permanece en evaluaciones posteriores (capítulo 9, Escenario C).

Una compensación es *retroactiva* si $\tau(c)$ es posterior a la exposición del sujeto (el instante en que el sujeto entró en operación o fue entregado). La retroactividad no afecta a $\mathsf{Valid}_t$; se informa, y es relevante para el diagnóstico (7.7) *(propuesta, OD-6)*.

### 7.5.4 Función de resultado

**Definición 7.14 (resultado) (propuesta, OD-10).** Para una instancia de obligación $o = \langle k, x\rangle$ con $k \ne R8$, sean

$$\mathit{app} = \mathrm{val}(\mathrm{App}_k(x)), \quad \mathit{req} = \mathrm{val}(\mathrm{Req}_k(x)), \quad \mathit{comp} = \begin{cases} \mathrm{val}(\exists c\ \mathsf{Valid}_t(c, o)) & k \in K \\ \mathbf{f} & k \notin K \end{cases}$$

Entonces

| Condición | Resultado |
|---|---|
| $\mathit{app} = \mathbf{f}$ | **no aplicable** |
| $\mathit{app} \ne \mathbf{f}$ y $\mathit{req} = \mathbf{t}$ | **satisfecha** |
| $\mathit{app} \ne \mathbf{f}$, $\mathit{req} \ne \mathbf{t}$ y $\mathit{comp} = \mathbf{t}$ | **compensada** |
| $\mathit{app} = \mathbf{t}$, $\mathit{req} = \mathbf{f}$ y $\mathit{comp} = \mathbf{f}$ | **violada** |
| en otro caso | **indeterminada** |

Las condiciones son mutuamente excluyentes y exhaustivas.

**Proposición 7.4 (la compensación no elimina obligaciones).** Ninguna instancia está *satisfecha* a causa de una compensación: el resultado *satisfecha* depende solo de $\mathit{req}$. Si se eliminan de $\Sigma$ todas las compensaciones, una instancia *compensada* pasa a *violada* o *indeterminada*, nunca a *satisfecha*.

**Proposición 7.5 (las violaciones están decididas).** Una instancia está *violada* solo si su aplicabilidad está decidida como verdadera, su requisito está decidido como falso y ninguna compensación es posiblemente válida. Por la Proposición 7.2, esto requiere una declaración de completitud para la evidencia de la que depende el requisito.

La Regla 6 se evalúa entonces sobre los resultados: las instancias *violadas* de reglas compensables son exactamente los casos en que no se cumple la obligación contraria al deber de 7.4.2. Las violaciones de reglas no compensables se informan solo bajo su propia regla.

### 7.5.5 Veredicto agregado

**Definición 7.15 (veredicto) (propuesta, OD-10).** Para el conjunto de resultados de una evaluación:

- **no conforme** si alguna instancia está *violada*;
- en otro caso, **no concluyente** si alguna instancia está *indeterminada*;
- en otro caso, **conforme con compensaciones** si alguna instancia está *compensada*;
- en otro caso, **conforme**.

El veredicto se informa siempre junto con el perfil completo de resultados (8.7). Sustituye a la definición de 0.2.1 $\mathsf{Compliant}(State) \iff \mathsf{Violations}(State) = \emptyset$, bajo la cual los casos compensados e indeterminados contaban como conformes.

---

## 7.6 Tiempo, versiones y reproducibilidad

**Definición 7.16 (entrada de la evaluación).** Una evaluación es función de la tupla

$$\varepsilon = (M, \rho, \alpha, \Pi, \Sigma_b, t, J)$$

- $M$: versión del método;
- $\rho$: versión del conjunto de reglas, incluidas las decisiones abiertas resueltas o las interpretaciones propuestas aplicadas;
- $\alpha$: la aplicación del método y su alcance evaluado;
- $\Pi$: la versión del conjunto de parámetros;
- $\Sigma_b$: la instantánea en las líneas base $b$, identificada mediante referencias inmutables (hashes de commit, revisiones de documentos, resúmenes criptográficos del contenido) y con declaraciones de completitud;
- $t$: el instante de evaluación, usado solo para la validez de las compensaciones;
- $J$: los juicios registrados (valoraciones con autor y fecha) usados para interpretar las políticas basadas en juicio.

**Proposición 7.6 (reproducibilidad).** Para un $\varepsilon$ fijo, los resultados quedan determinados. Revalorar un juicio cambia $J$ y produce por tanto una evaluación distinta, que debe informarse como tal.

**Proposición 7.7 (independencia del orden).** Los resultados no dependen de los instantes de registro $\tau$ de intenciones, decisiones, supuestos, validaciones o vínculos. Los únicos usos de $\tau$ son $\tau(c) \le t$ y la marca de retroactividad de las compensaciones. Una intención registrada después del código que justifica produce el mismo resultado que una registrada antes. Este es el contenido formal de la ortogonalidad (capítulo 5). La única excepción, el momento de la compensación, es explícita: aceptar un riesgo solo tiene sentido en relación con la exposición que cubre.

**Validación y versiones.** Como $A$ contiene versiones, una validación de $a$ no valida una sucesora $a'$ salvo que se registre $\mathsf{equiv}(a, a')$. Una declaración de equivalencia es a su vez un registro y puede ser cuestionada.

**Versiones del método.** Una evaluación queda ligada a $\rho$. Cambiar el método no cambia las evaluaciones pasadas; reevaluar bajo un nuevo conjunto de reglas es una nueva evaluación $\varepsilon'$ (8.6).

**Esbozo (propiedades temporales).** Las propiedades de la evolución de un registro, como "toda compensación se remedia o se renueva antes de expirar", son propiedades temporales sobre una secuencia de instantáneas. En lógica temporal lineal: $\square\big(\mathsf{compensated}(o) \rightarrow \lozenge(\mathsf{satisfied}(o) \lor \mathsf{renewed}(o))\big)$. Tales propiedades pueden describir la salud de un registro de ingeniería a lo largo del tiempo. No forman parte de la evaluación, que se define sobre una única instantánea.

---

## 7.7 Diagnosabilidad

El diagnóstico parte de un fallo $f$ y de un conjunto de *factores causales* $\Phi(f)$ identificados por un análisis causal (análisis de incidentes, depuración, investigación de causa raíz). El método no identifica factores causales; la inferencia causal queda fuera de su alcance. Lo que el método define es cómo se relacionan los factores con el registro de ingeniería.

**Definición 7.17 (clasificación de factores) (propuesta, OD-1).** Sea $\varepsilon_f$ la entrada de evaluación en el momento de la exposición (la instantánea y el instante anteriores al fallo). Cada factor $\varphi \in \Phi(f)$ se clasifica como:

1. **brecha**: $\varphi$ está vinculado a un sujeto $x$ para el que alguna instancia $\langle k, x\rangle$ está *violada* bajo $\varepsilon_f$ (esto incluye instancias con una compensación que no era válida en ese momento), o *compensada* por una compensación cuyo riesgo declarado no cubre $\varphi$;
2. **riesgo aceptado**: $\varphi$ está vinculado a un sujeto cuya instancia está *compensada* bajo $\varepsilon_f$ por una compensación cuyo riesgo declarado cubre $\varphi$, o a un supuesto declarado $s$ ($\mathsf{Declared}(s)$) que resultó falso. Una compensación registrada después del fallo no está en $\varepsilon_f$ y no puede situar un factor en esta clase;
3. **clasificación errónea de parámetros**: $\varphi$ está vinculado a un sujeto cuya instancia fue *no aplicable* o *compensable* solo a causa de una política, y la consecuencia queda fuera de la tolerancia al riesgo declarada (esta clasificación es un juicio registrado);
4. **externo**: $\varphi$ queda fuera del alcance evaluado;
5. **no relacionado**: $\varphi$ está dentro del alcance pero no está vinculado a ningún elemento de $\Sigma$.

Si no puede decidirse si $\varphi$ está vinculado porque la evidencia es inaccesible, la clasificación es *indeterminada*.

**Definición 7.18 (resultado de la Regla 8) (propuesta, OD-1).** Para un fallo $f$ dentro del alcance, la instancia $\langle R8, f\rangle$ está *violada* si algún factor es *no relacionado*. Está *indeterminada* si ningún factor es no relacionado y alguna clasificación es indeterminada. En otro caso está *satisfecha*.

Por tanto, la Regla 8 puede estar satisfecha mientras otra regla está violada: un fallo explicado por una validación faltante está *diagnosticado*, y el diagnóstico es lo que exige la Regla 8. La definición de 0.2.1 $\mathsf{Diagnosable}(f) \iff \exists r\ \mathsf{ExplainsInMethodTerms}(r, f)$ corresponde a "algún factor se clasifica como 1, 2 o 3". Hacía que un registro correcto cuyo fallo tenía una causa externa contara como no aplicación del método.

**Límites.** Una clasificación relaciona un factor con el registro. No afirma que la brecha relacionada fuera una causa *suficiente*, ni que el análisis encontrara todos los factores. Calificar una decisión como errónea a posteriori debe basarse en el registro disponible cuando se tomó la decisión, porque el sesgo retrospectivo distorsiona el juicio sobre lo que podía saberse [Fischhoff 1975; Dekker 2006].

---

## 7.8 Expresividad: qué cubre la lógica de primer orden

| Aspecto | Lógica de primer orden sobre una instantánea | Añadido en este capítulo | Estatus |
|---|---|---|---|
| Aplicabilidad | fórmulas condicionales | pares $\mathrm{App}_k$ / $\mathrm{Req}_k$ | Definición |
| Obligaciones dependientes del contexto | símbolos de predicado no interpretados | parámetros como interpretaciones de los predicados de política (7.2.4) | Definición |
| Caminos de trazabilidad | no definibles (clausura transitiva) | operador de clausura transitiva | Definición |
| Desviaciones aceptadas | no representables: un estado compensado satisface o viola la fórmula | función de resultado que separa requisito y compensación (7.5.4) | Definición |
| Evidencia faltante o inaccesible | la semántica de mundo cerrado supone completitud | semántica trivalente con completitud local declarada (7.5.2) | Definición |
| Resultados diagnósticos | el razonamiento causal no puede expresarse como restricciones sobre el registro | clasificación de factores identificados externamente (7.7) | Definición; el análisis causal queda fuera del alcance |
| Tiempo y versiones | atributos con marca temporal y entidades versionadas bastan para evaluar | tupla de entrada de la evaluación (7.6) | Definición |
| Evolución en el tiempo | no es necesaria para evaluar | lógica temporal sobre secuencias de instantáneas | Esbozo |

La conclusión es que la lógica de primer orden sigue siendo el lenguaje objeto de las reglas. Lo que le falta lo aportan una semántica trivalente, un operador de clausura transitiva y una función de resultado. Ninguno de ellos requiere un motor de inferencia, un demostrador de teoremas ni un lenguaje nuevo. Sobre una instantánea finita, cada regla es una consulta finita.

---

## 7.9 Notas prácticas (no normativas)

- Esta formalización es compatible con bases de datos relacionales y de grafos, consultas recursivas y verificación de restricciones. No privilegia ninguna de ellas.
- Es independiente de cualquier proceso de desarrollo o ciclo de vida, y de cualquier herramienta que almacene el registro de ingeniería.
- Permite una evaluación reproducible bajo un contexto explícito (7.6). No hace objetiva la evaluación donde las políticas requieren juicio; hace esos juicios explícitos, atribuidos y reproducibles.
- No identifica las causas de los fallos. Relaciona las causas identificadas por el análisis con el registro de ingeniería e indica lo que el registro no pudo explicar.
