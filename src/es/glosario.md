# Glosario

::: glossary

- **Alcance evaluado.** La frontera del sistema, el conjunto de cambios, la unidad de cambio, las fuentes de evidencia y las declaraciones de completitud de una aplicación del método (8.2).
- **Aplicabilidad.** La condición bajo la cual una regla aplica a un sujeto. La decide una política del conjunto de parámetros (7.3).
- **Aplicación del método.** El uso del método sobre un alcance evaluado declarado, con un conjunto de parámetros declarado, de modo que el cumplimiento y la diagnosabilidad puedan evaluarse.
- **Artefacto.** Un producto de trabajo producido, versionado e inspeccionable. Los artefactos que afectan el comportamiento del sistema, según lo decida la política correspondiente, deben ser trazables a una intención o a decisiones (Regla 3). Los registros de ingeniería (intenciones, decisiones, supuestos, validaciones, compensaciones) se tipan por su papel y no se cuentan como artefactos.
- **Autoridad de aceptación de riesgo.** La parte a la que el conjunto de parámetros permite aceptar un tipo dado de riesgo mediante una compensación.
- **Cambio de ingeniería.** Una modificación de artefactos que afectan el comportamiento dentro del alcance evaluado, identificada por una diferencia de versiones. La unidad de cambio la declara la aplicación del método.
- **Compensación.** Una aceptación explícita y auditable de riesgo para una instancia de obligación no cumplida, aceptada por una parte autorizada y sujeta a una condición de revisión. No elimina la obligación subyacente: el resultado es *compensada*, no *satisfecha*.
- **Completitud de la evidencia.** Una declaración de que, para una relación y una parte del alcance, toda instancia verdadera está presente en las fuentes de evidencia. Solo bajo una declaración así la evidencia faltante cuenta como ausencia (7.5.1).
- **Contexto de ingeniería.** El conocimiento, las restricciones y las circunstancias en que ocurre la ingeniería y que explican una solución, sea explícito o tácito (capítulo 10).
- **Contrato de evaluación.** El registro de las entradas de una evaluación (versión del método y del conjunto de reglas, alcance, conjunto de parámetros, referencias a la evidencia, momento de evaluación, juicios) y de sus resultados (8.6).
- **Decisión.** Una elección de ingeniería comprometida entre alternativas, hecha explícita y vinculada a la intención que sirve.
- **Diagnosabilidad.** La capacidad de relacionar los factores causales de un fallo con el registro de ingeniería: como brechas, riesgos aceptados, clasificaciones erróneas de parámetros, factores externos o factores que el registro no puede explicar.
- **Evaluación.** Un acto concreto de determinar los resultados de las instancias de obligación de una aplicación del método frente a una instantánea de la evidencia.
- **Explícito.** Razonamiento de ingeniería capturado como registros trazables en lugar de permanecer no documentado o tácito.
- **Explicitud.** La propiedad del trabajo de ingeniería de estar hecho explícito en una forma trazable, evaluable y diagnosticable.
- **Factor causal.** Una condición que el análisis causal de un fallo identifica como contribuyente a él. Su estado es *establecido* o *provisional*. Solo los factores establecidos cuyo lugar en el sistema se conoce pueden relacionarse con el registro de ingeniería; los demás dejan el diagnóstico indeterminado (7.7).
- **Fallo.** Una desviación observada del comportamiento o las restricciones intencionadas o requeridas que puede analizarse contra el razonamiento de ingeniería explícito.
- **Indeterminada.** El resultado de una instancia de obligación cuando la evidencia disponible no la decide. No es ni una violación ni cumplimiento.
- **Ingeniería de contexto.** La construcción, selección, preservación y entrega deliberadas del contexto relevante a una persona o sistema que lo necesita para actuar. Distinta del método (capítulo 10).
- **Instancia de obligación.** Una regla aplicada a un sujeto, escrita ⟨regla, sujeto⟩. La evaluación asigna un resultado a cada instancia.
- **Intención.** El resultado, la propiedad o la restricción deseada que un cambio o sistema debe satisfacer, con un alcance definido.
- **Método.** Un conjunto prescriptivo de obligaciones y restricciones sobre registros y relaciones de ingeniería, parametrizable y evaluable, e independiente del orden del flujo de trabajo.
- **Ortogonalidad.** Independencia del orden del flujo de trabajo o de la secuencia del ciclo de vida, manteniendo obligaciones de ingeniería fijas.
- **Parámetros contextuales.** El conjunto de parámetros declarado y versionado de una aplicación del método: descriptores de contexto y las políticas que deciden los predicados que usan las reglas.
- **Política.** Un criterio del conjunto de parámetros que decide un predicado dependiente de parámetros, como la trivialidad, el impacto, la criticidad, la adecuación de la validación, la admisibilidad de la compensación o la autoridad de aceptación de riesgo.
- **Procedencia.** Cómo llegó a existir un registro: contemporánea, retrospectiva, reconstruida o inferida (8.4.2).
- **Proceso.** Una secuencia ordenada de actividades o fases usada para organizar el trabajo, que puede incorporar un método pero no define obligaciones de ingeniería por sí mismo.
- **Producto de software.** Software cuyo comportamiento, restricciones y propósito son responsables a través de intención, decisiones, validación y trazabilidad explícitas.
- **Registro de ingeniería.** Las intenciones, decisiones, supuestos, trade-offs, validaciones, compensaciones y vínculos que existen en las fuentes de evidencia declaradas.
- **Regla normativa.** Un enunciado de obligación que define qué debe ser explícito y las consecuencias de la omisión.
- **Resultado.** Uno de *satisfecha*, *violada*, *compensada*, *no aplicable* o *indeterminada*.
- **Software.** Código ejecutable, configuraciones y datos que producen el comportamiento del sistema.
- **Supuesto.** Un enunciado tratado como verdadero para razonar o planificar cuando la evidencia falta o se difiere, y que debe permanecer identificable hasta ser validado o invalidado.
- **Trade-off.** Un equilibrio deliberado entre restricciones o atributos de calidad en competencia, aceptado como parte de una decisión.
- **Trazabilidad.** Vínculos explícitos y navegables entre intenciones, decisiones, supuestos, artefactos y validaciones que permiten inspeccionar y evaluar el razonamiento.
- **Validación.** Evidencia explícita de que un artefacto o decisión satisface su intención declarada bajo el contexto declarado. Incluye lo que la terminología ISO/IEC/IEEE distingue como verificación y validación (4.1).

:::
