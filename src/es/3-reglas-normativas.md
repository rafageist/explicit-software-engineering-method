# 3. Reglas normativas centrales (borrador)

Estas reglas son restricciones y obligaciones normativas del método.
Cada regla se enuncia para ser verificable, implicar consecuencias cuando se viola y soportar análisis sin dependencia de herramientas.
Son independientes de la secuencia de trabajo y no prescriben un proceso.

## 3.0 Cómo leer estas reglas
Estas reglas restringen resultados, no el orden de las actividades. Un equipo puede cumplirlas mediante distintos flujos de trabajo y seguir siendo conforme, porque el método evalúa lo que existe y cómo se justifica, no cuándo se produjo.

La ausencia de artefactos solo se permite mediante compensación explícita. La compensación es un acto auditable que registra el riesgo aceptado; no elimina la obligación subyacente.

Las violaciones son condiciones diagnosticables, no fallas morales. La intención es hacer visibles y explicables las brechas para que puedan corregirse o aceptarse explícitamente.

### 3.0.1 Palabras clave normativas
Las palabras clave DEBE, NO DEBE, DEBERÍA y PUEDE se interpretan como se describe en BCP 14 [RFC 2119; RFC 8174] cuando, y solo cuando, aparecen en mayúsculas. En la edición inglesa corresponden a MUST, MUST NOT, SHOULD y MAY. Un DEBERÍA es una recomendación: apartarse de ella no es una violación, pero la razón para apartarse debería ser explícita.

### 3.0.2 Términos usados por todas las reglas
Los siguientes términos fijan a qué se aplican las reglas. Se definen con precisión en los capítulos 7 y 8; el resumen de esta sección basta para leer las reglas.

- **Aplicación del método.** El uso del método sobre un *alcance evaluado* declarado: una frontera del sistema, un conjunto de cambios de ingeniería, las fuentes de evidencia consideradas y un *conjunto de parámetros* declarado. Toda regla se evalúa dentro de una aplicación del método; fuera de ella, las reglas no afirman nada.
- **Cambio de ingeniería.** Una modificación de artefactos que afectan el comportamiento dentro del alcance evaluado, identificada por un delta de versión (por ejemplo, un rango de commits, una merge request, una revisión de modelo o un cambio de configuración). La *unidad de cambio* (qué cuenta como un cambio) la declara la aplicación; el método no la prescribe.
- **Registro de ingeniería.** El conjunto de intenciones, decisiones, supuestos, trade-offs, validaciones, compensaciones y vínculos que existen en las fuentes de evidencia declaradas. Los registros se tipan por su rol, no por su almacenamiento: una decisión escrita en un archivo Markdown es una decisión, no un artefacto.
- **Instancia de obligación.** Una regla aplicada a un sujeto, escrita ⟨regla, sujeto⟩; por ejemplo, ⟨R4, payment-adapter v2.3⟩. La evaluación produce un resultado por cada instancia de obligación.
- **Política.** Un criterio del conjunto de parámetros que decide un predicado dependiente de parámetros: qué cambios son no triviales, qué decisiones son de impacto, qué artefactos afectan el comportamiento, qué elementos son críticos, qué validación es adecuada, qué compensaciones son admisibles y quién puede aceptar riesgo. Las reglas se refieren a estos predicados; el conjunto de parámetros les da significado en un contexto.

### 3.0.3 Resultados
Evaluar una instancia de obligación produce exactamente uno de cinco resultados: *satisfecha*, *violada*, *compensada*, *no aplicable* o *indeterminada*. *Compensada* no es una forma de *satisfecha*: la obligación permanece, y el resultado registra que no se cumple bajo un riesgo aceptado. *Indeterminada* significa que la evidencia disponible no decide la cuestión; no es una violación y tampoco es conformidad. El capítulo 7.5 define formalmente los resultados y el capítulo 8.7 explica cómo se informan.

### 3.0.4 Estatus del texto
Cada regla conserva el enunciado normativo de la versión 0.2.1. Los párrafos titulados *Precisión* hacen evaluable el enunciado existente sin cambiar lo que exige. Los párrafos titulados *Interpretación propuesta (OD-n)* cambiarían o fijarían el significado de una regla. Están pendientes de decisión del mantenedor y se registran, con sus alternativas, en `docs/open-decisions.md`. Mientras no se tome una decisión, un evaluador DEBE indicar en la evaluación qué interpretaciones propuestas aplicó.

## 3.1 Regla 1 - Declaración de intención (obligatoria)
Todo cambio de ingeniería no trivial DEBE declarar una Intención explícita.
La Intención define el resultado, la propiedad o la restricción deseada que el cambio busca satisfacer.
La Intención DEBE tener un alcance definido.
Los cambios sin intención declarada se consideran trabajo implícito.

Esta regla garantiza que los cambios estén anclados a un objetivo declarado y puedan evaluarse contra él, independientemente de si el trabajo inicia desde código o desde modelos.

Ejemplo: Un equipo modifica el comportamiento de la caché con la intención de reducir la latencia para un límite de servicio definido, y registra ese alcance de forma explícita.

Justificación:
Sin intención, no es posible validar ni trazar. La calidad se vuelve accidental.

**Precisión.**
*Sujeto:* cada cambio de ingeniería del alcance evaluado.
*Aplica cuando:* el cambio es no trivial según la política de trivialidad del conjunto de parámetros. Si no se declara una política de trivialidad, la aplicabilidad queda sin decidir y el resultado es *indeterminada*, salvo que el requisito se cumpla; bajo OD-9, además se viola la Regla 7.
*Se satisface cuando:* el cambio está vinculado al menos a un registro de intención cuyo alcance está declarado (la parte del sistema, los interesados o el atributo de calidad afectados).
*Evidencia:* el registro de intención y el vínculo desde el cambio hacia él, en una fuente de evidencia declarada. Para esta regla no importa cuándo se registró la intención; una intención escrita después del código es válida (capítulo 9, Escenario A).
*Contraparte formal:* 7.3, R1.

**Interpretación propuesta (OD-5).** La Regla 1 no es compensable. Una compensación debe declarar qué riesgo se acepta, lo que no puede hacerse sin declarar qué buscaba lograr el cambio; y declarar eso es declarar la intención.

## 3.2 Regla 2 - Explicitación de decisiones (obligatoria)
Toda decisión de ingeniería irreversible o de impacto DEBE hacerse explícita.
Una Decisión DEBE referenciar:
- la Intención a la que sirve
- las alternativas consideradas (al menos implícitamente)
Las decisiones no documentadas se tratan como Supuestos por defecto.

Esta regla preserva el razonamiento y asegura que las elecciones de impacto puedan revisarse a posteriori, incluso cuando se toman bajo presión de tiempo.

Ejemplo: Bajo un plazo de producción, un equipo elige un modelo de datos más simple y registra la decisión junto con la alternativa descartada por razones de riesgo.

Justificación:
Las decisiones no documentadas impiden el análisis y el aprendizaje posteriores al fallo.

```mermaid
flowchart LR
  I[Intención] --> D[Decisión] --> A[Artefacto] --> V[Validación]
```

Este diagrama muestra la cadena mínima de trazabilidad que esperan las reglas: la intención informa decisiones, las decisiones moldean artefactos y la validación vincula los artefactos con su propósito previsto.

**Precisión.**
*Sujeto:* cada elección de ingeniería incorporada en el alcance evaluado, haya sido registrada o no. Las decisiones registradas se encuentran en el registro. Las decisiones no registradas se identifican mediante revisión o análisis de fallos como elecciones incorporadas en artefactos (un modelo de datos, un valor de timeout, una dependencia) para las que no existe registro de decisión.
*Aplica cuando:* la elección es irreversible o de impacto según la política de impacto.
*Se satisface cuando:* existe un registro de decisión, está vinculado a la intención a la que sirve y referencia las alternativas consideradas.
*Evidencia:* el registro de decisión y sus vínculos. Los registros de decisiones de arquitectura [Tyree and Akerman 2005] son una forma habitual. Una decisión no registrada solo puede estar *violada*, *compensada* o *indeterminada*; nunca *satisfecha*.
*Contraparte formal:* 7.3, R2.

**Interpretación propuesta (OD-2).** "Se tratan como Supuestos por defecto" es una clasificación diagnóstica. Durante la evaluación y el análisis de fallos, una decisión no registrada se trata como una premisa no validada, no como una elección revisada. La clasificación no descarga la Regla 2: la instancia de obligación permanece *violada* salvo que se compense.

**Interpretación propuesta (OD-3).** "Las alternativas consideradas (al menos implícitamente)" significa que el registro enumera las alternativas consideradas o declara explícitamente que no se evaluó ninguna alternativa y por qué. Un registro explícito no puede referenciar una alternativa de forma implícita.

**Interpretación propuesta (OD-4).** Cuando una decisión de impacto equilibra atributos de calidad o restricciones en competencia, el registro de decisión DEBE declarar el trade-off aceptado (qué se cedió y a cambio de qué). Los trade-offs se rigen así como parte de la Regla 2, no mediante una regla separada.

## 3.3 Regla 3 - Trazabilidad de artefactos (obligatoria)
Todo Artefacto que afecte el comportamiento del sistema DEBE ser trazable a al menos una Intención o Decisión.
Los artefactos huérfanos se consideran artefactos injustificados.
La trazabilidad DEBE ser navegable en ambas direcciones.

Esta regla garantiza que los artefactos existan por una razón localizable y revisable, en lugar de sobrevivir como residuo inexplicado de trabajo pasado.

Ejemplo: Un nuevo flag de configuración se vincula con la decisión que lo introdujo y con la intención que debía satisfacer.

Justificación:
Los artefactos no trazables aumentan la complejidad sin valor responsable.

**Precisión.**
*Sujeto:* cada versión de artefacto del alcance evaluado. Un *artefacto* es cualquier producto de trabajo versionado. La Regla 3 se aplica al subconjunto que afecta el comportamiento del sistema según la política de artefactos que afectan el comportamiento, que normalmente incluye código fuente, configuración, esquemas, definiciones de infraestructura y modelos usados para generar o configurar el sistema.
*Se satisface cuando:* existe un camino de trazabilidad desde el artefacto hasta al menos una intención o decisión. El camino puede pasar por otros registros o artefactos (por ejemplo, código generado → modelo → decisión → intención). Un vínculo directo es un caso particular.
*La navegabilidad bidireccional* es un requisito sobre cómo se registran los vínculos, no sobre el grafo, porque cualquier relación registrada puede leerse en ambas direcciones. Un vínculo la satisface cuando, usando solo las fuentes de evidencia declaradas, puede encontrarse la justificación desde el artefacto y los artefactos justificados desde la intención o la decisión (capítulo 8.4).
*Contraparte formal:* 7.3, R3.

## 3.4 Regla 4 - Requisito de validación (contextual)
Los Artefactos y Decisiones con impacto crítico DEBEN tener Validación explícita.
Lo que se considera crítico es un parámetro del método, no un umbral fijo.
La Validación PUEDE adoptar distintas formas:
- pruebas
- revisiones
- pruebas formales
- simulaciones
- evidencia externa

Esta regla vincula el esfuerzo de validación con la criticidad contextual, permitiendo distintas formas de evidencia mientras exige justificación explícita para trabajo de alto impacto.

Ejemplo: Un cambio de alto riesgo en un flujo de pagos se valida mediante una revisión específica y evidencia de pruebas acorde con su criticidad.

Justificación:
El trabajo crítico sin validación es indistinguible de la especulación.

**Precisión.**
*Sujeto:* cada versión de artefacto y cada decisión del alcance evaluado (OD-12).
*Aplica cuando:* el sujeto es crítico según la política de criticidad.
*Se satisface cuando:* existe un registro de validación que (a) se refiere a la misma versión del sujeto, o a una versión que el registro declara equivalente, y (b) es adecuado según la política de adecuación de la validación (por ejemplo, los tipos de validación exigidos para un nivel de criticidad). Una validación de la versión 1.4.0 no valida la versión 1.4.1.
*Evidencia:* el registro de validación, su resultado, la versión que examinó y, cuando la adecuación requiere juicio, quién la evaluó.
*Contraparte formal:* 7.3, R4.

## 3.5 Regla 5 - Declaración de supuestos (obligatoria)
Los Supuestos DEBEN declararse explícitamente cuando falta evidencia o se difiere.
Los Supuestos DEBEN ser identificables como tales.
Los Supuestos DEBERÍAN seguirse hasta ser validados o invalidados.

Esta regla hace visible la incertidumbre y evita que premisas ocultas se conviertan en dependencias silenciosas del sistema.

Ejemplo: Un equipo asume que una dependencia externa sostendrá un throughput definido hasta que puedan ejecutarse benchmarks, y registra ese supuesto de forma explícita.

Justificación:
Los supuestos implícitos acumulan riesgo en silencio.

**Precisión.**
*Sujeto:* cada decisión o artefacto del alcance evaluado que depende de una premisa no respaldada por evidencia en el registro.
*Se satisface cuando:* cada una de esas premisas está registrada como supuesto, tipada como tal y vinculada a los elementos que dependen de ella. El seguimiento (DEBERÍA) significa que el supuesto tiene un estado (*abierto*, *validado*, *invalidado*) y que el registro muestra cuándo cambió ese estado.
*Detectabilidad.* Una premisa oculta, por definición, no está en el registro. En general, las violaciones de la Regla 5 no pueden encontrarse inspeccionando mecánicamente el registro. Se establecen mediante revisión o análisis de fallos, cuando se identifica una premisa de la que se dependía y se constata que no estaba validada ni declarada. Las verificaciones mecánicas cubren solo la parte declarada: tipado, vínculos y estado.
*Relación con la Regla 6.* Un supuesto registra lo que se cree. Una compensación registra qué obligación no se cumple y qué riesgo se acepta. Ambos son complementarios: un artefacto crítico liberado sin validación bajo la premisa de que una dependencia se comporta como está documentado necesita tanto un supuesto declarado (Regla 5) como una compensación por la validación faltante (Regla 6). Un supuesto declarado que después resulta falso no es una violación de la Regla 5; es la regla funcionando.
*Contraparte formal:* 7.3, R5.

## 3.6 Regla 6 - Compensación explícita (obligatoria)
Cuando falta un artefacto o validación requerida, la ausencia DEBE compensarse explícitamente.
La Compensación DEBE:
- estar documentada
- referenciar el elemento faltante
- declarar el riesgo aceptado

La compensación es un registro explícito y auditable de riesgo aceptado. No elimina la obligación; marca una desviación consciente y permite evaluar su impacto.

Ejemplo: Se despliega un hotfix sin validación completa, y el equipo registra la validación faltante, el riesgo aceptado y el plan de seguimiento.

Justificación:
Se permiten atajos; no se permiten atajos silenciosos.

**Precisión.**
*Sujeto:* cada instancia de obligación de las demás reglas que aplica y no se cumple. La Regla 6 es una regla sobre los resultados de otras reglas. "Referenciar el elemento faltante" significa referenciar la instancia de obligación incumplida (la regla y el sujeto existente), porque un elemento faltante no puede referenciarse a sí mismo.
*Se satisface cuando:* un registro de compensación referencia la instancia de obligación, declara el riesgo aceptado y es válido en el momento de la evaluación (ver más abajo). El resultado de la instancia referenciada es entonces *compensada*, nunca *satisfecha*. La remediación (producir el registro faltante) convierte la instancia en *satisfecha* para las versiones que cubre y cierra la compensación.
*Validez.* Una compensación es válida cuando es admisible para esa obligación según el conjunto de parámetros, la acepta una parte a la que la política de autoridad permite aceptar ese riesgo y no ha expirado. Una compensación no válida deja la instancia *violada*. No crea por sí misma una segunda violación.

**Interpretación propuesta (OD-5).** Las reglas compensables son R2, R3, R4 y R5. R1 y R7 no son compensables; R6 y R8 no están sujetas a compensación. Los parámetros PUEDEN declarar otras obligaciones como no compensables en un contexto.

**Interpretación propuesta (OD-6).** Una compensación DEBE declarar una condición de revisión: una fecha de expiración o un evento, por ejemplo "hasta que la suite de pruebas de integración pase en verde". PUEDE ser indefinida solo si el conjunto de parámetros permite la aceptación permanente para ese tipo de obligación. Una compensación registrada después de la exposición que cubre (por ejemplo, después de un fallo) se marca como *retroactiva*. Cuenta para las evaluaciones posteriores a su registro, pero no es evidencia de que el riesgo se aceptara antes de la exposición.

**Interpretación propuesta (OD-7).** El conjunto de parámetros DEBE declarar quién puede aceptar qué riesgos, y cada compensación DEBE identificar a la parte que acepta. El método no prescribe roles ni exige independencia; los parámetros pueden exigirla, por ejemplo prohibiendo que el autor de un cambio crítico acepte su riesgo.

*Contraparte formal:* 7.4 y 7.5.

## 3.7 Regla 7 - Conciencia de parámetros (obligatoria)
El método DEBE aplicarse con parámetros contextuales explícitos.
Ejemplos de parámetros:
- criticidad del dominio
- tolerancia al riesgo
- presión regulatoria
- escala del equipo
- vida útil esperada del sistema

Estos parámetros influyen:
- nivel requerido de explicitud
- profundidad de validación
- compensaciones aceptables

Esta regla asegura que las obligaciones se apliquen con contexto, de modo que la evaluación refleje el riesgo y la criticidad reales del trabajo.

Ejemplo: Un sistema en un dominio regulado declara mayor profundidad de validación y límites de compensación más estrictos que un prototipo interno.

Justificación:
La calidad es contextual; el rigor sin contexto es desperdicio.

**Precisión.**
*Sujeto:* la aplicación del método, no los cambios individuales. Hay una instancia de obligación de la Regla 7 por cada alcance evaluado.
*Se satisface cuando:* el conjunto de parámetros es explícito, está versionado y está vinculado a la evaluación.
Los parámetros actúan en dos capas. Los *descriptores de contexto*, como los enumerados arriba, caracterizan la situación. Las *políticas* deciden los predicados que usan las demás reglas. Los parámetros moldean la aplicabilidad, la adecuación y la admisibilidad; no pueden convertir una obligación aplicable e incumplida en una satisfecha.

**Interpretación propuesta (OD-9).** La Regla 7 se satisface solo si el conjunto de parámetros declara una política para cada predicado dependiente de parámetros: unidad de cambio y trivialidad, impacto e irreversibilidad, artefacto que afecta el comportamiento, criticidad, adecuación de la validación, admisibilidad de la compensación y autoridad de aceptación de riesgo. Una política es un criterio; no necesita ser un umbral numérico. Una política ausente hace *indeterminado* todo resultado que dependa de ella.

*Contraparte formal:* 7.2.4 y 7.3, R7.

## 3.8 Regla 8 - Diagnosabilidad del fallo (regla de resultado)
Cuando ocurre un fallo, DEBE ser posible explicarlo en términos de la aplicación del método.
Al menos uno de los siguientes DEBE ser identificable:
- intención ausente
- decisión inválida
- artefacto no validado
- supuesto falso
- compensación inadecuada
- parámetros mal configurados

Esta regla hace del fallo un resultado trazable de decisiones de ingeniería, no una narrativa retrospectiva. Permite analizar qué obligación no se cumplió y por qué.

Ejemplo: Después de una caída, el análisis identifica un artefacto no validado y un registro de compensación ausente como brecha decisiva.

Justificación:
Si el fallo no puede explicarse en términos del método, el método no se aplicó.

**Precisión.**
*Sujeto:* cada fallo observado dentro del alcance evaluado.
La Regla 8 se evalúa a posteriori y depende de un análisis causal del fallo (análisis de incidentes, depuración, investigación de causa raíz) que el método no realiza. El método relaciona los factores causales identificados por ese análisis con el registro de ingeniería. No identifica causas por sí mismo.
Las seis razones enumeradas son de naturaleza distinta. *Intención ausente*, *artefacto no validado* y *compensación inadecuada* son brechas en obligaciones. *Supuesto falso* suele ser una premisa declarada que resultó errónea, lo que es el método funcionando. *Decisión inválida* y *parámetros mal configurados* son juicios hechos en retrospectiva y deben apoyarse en el registro disponible en el momento de la decisión.

**Interpretación propuesta (OD-1).** La Regla 8 obliga a que el registro de ingeniería sea suficiente para clasificar cada factor causal de un fallo que esté dentro del alcance evaluado en una de cinco clases:
1. una brecha a nivel de método (una instancia de obligación *violada*, o una compensación que no era válida);
2. un riesgo aceptado materializado (una compensación válida o un supuesto declarado);
3. una clasificación errónea de parámetros (una política que clasificó el elemento como trivial, no crítico o compensable, con consecuencias fuera de la tolerancia al riesgo declarada);
4. un factor externo o fuera de alcance;
5. no relacionado: el factor está dentro del alcance evaluado pero no puede relacionarse con ningún elemento del registro de ingeniería (por ejemplo, un ajuste de producción cambiado fuera del control de versiones).

La Regla 8 solo se viola por factores de la clase 5. No se viola por factores externos ni por riesgos aceptados que se materializan. Cuando existe una relación pero no puede verificarse porque la evidencia es inaccesible, el resultado es *indeterminada*. Bajo esta interpretación, la justificación anterior se lee: *si un fallo no puede relacionarse con el registro de ingeniería, el registro era insuficiente*. El texto actual dice que el método no se aplicó, lo que el capítulo 6.6 contradice para fallos externos e irreducibles.

*Contraparte formal:* 7.7.

## 3.9 Meta-nota
Estas reglas no describen un proceso.
Definen restricciones y obligaciones que deben cumplirse independientemente del flujo de trabajo.
Eso es lo que las convierte en reglas de un método, no de un proceso.

## 3.10 Conclusión
Estas reglas hacen posible la evaluación al especificar qué debe ser explícito y cómo se registran las brechas. Transforman el fallo en evidencia al hacer observables la intención, decisiones, supuestos, validación o compensación faltantes. Como restringen resultados en lugar del orden de actividad, permanecen independientes de cualquier proceso específico.
