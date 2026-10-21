# 4. Relación con estándares

El Método Explícito de Ingeniería de Software está diseñado para operar dentro de estándares de ingeniería de software, no para reemplazarlos. Asume que los estándares definen el contexto de trabajo y aclara cómo se establece la responsabilidad de ingeniería dentro de ese contexto.

Versiones anteriores de este capítulo describían los estándares IEEE e ISO en conjunto como marcos de proceso que "por lo general no exigen la captura explícita del razonamiento de ingeniería". Eso no es exacto para varios de ellos. Este capítulo identifica los estándares concernidos y enuncia la relación con cada uno.

## 4.1 Lo que abordan estándares identificables

| Estándar | Qué aborda | Relación con el método |
|---|---|---|
| ISO/IEC/IEEE 12207 (software) e ISO/IEC/IEEE 15288 (sistemas), procesos de ciclo de vida | Definiciones de procesos, entre ellos gestión de decisiones, gestión de riesgos, gestión de la configuración, gestión de la información, verificación y validación | Estos estándares definen procesos cuyos resultados incluyen decisiones, fundamentos y riesgos registrados. El método no define procesos. Define obligaciones sobre los registros que esos procesos producen y los evalúa sea cual sea el proceso que los produjo. |
| ISO/IEC/IEEE 42010 | Descripción de arquitectura, incluidos el fundamento y las decisiones de arquitectura | Una descripción de arquitectura conforme es una fuente de registros de decisión e intención para las reglas 2 y 3 en el nivel arquitectónico. El método cubre además decisiones por debajo de ese nivel y su vínculo con cambios individuales. |
| ISO/IEC/IEEE 29148 | Ingeniería de requisitos, incluidos atributos y trazabilidad de requisitos | Los requisitos son una forma común de intención (regla 1) y la trazabilidad de requisitos es una parte de la regla 3 [Gotel and Finkelstein 1994]. El método agrega intenciones para cambios individuales, compensación de vínculos faltantes y evaluación con evidencia incompleta. |
| IEEE 1012 | Verificación y validación, con niveles de integridad que escalan las tareas de V&V según la criticidad | Los niveles de integridad son una política de criticidad y adecuación lista para usar en la regla 4. El método generaliza la idea a todo predicado que depende de parámetros y agrega la compensación explícita cuando falta la V&V requerida. |
| ISO/IEC/IEEE 16085 | Gestión de riesgos en el ciclo de vida | Una compensación es una aceptación de riesgo registrada. La práctica de gestión de riesgos puede aportar la política de autoridad y las declaraciones de riesgo que exige la regla 6. |
| ISO/IEC/IEEE 15289 | Contenido de los elementos de información del ciclo de vida | Aporta estructuras de contenido que pueden servir como registros (8.4.1). El método exige cierto contenido y ciertos vínculos, no un documento particular. |
| ISO/IEC 25010 | Modelo de calidad del producto | Aporta vocabulario para los atributos de calidad nombrados en intenciones y trade-offs. |
| ISO/IEC/IEEE 24765 | Vocabulario de ingeniería de sistemas y software | Referencia terminológica. Donde los términos del método difieren, la diferencia es deliberada (ver abajo). |

Estas relaciones se basan en el alcance publicado y las descripciones de procesos de cada estándar. Una correspondencia cláusula por cláusula con las ediciones vigentes es trabajo futuro, y debe hacerse contra los textos normativos, no a partir de este resumen.

**Una nota sobre terminología.** En el uso ISO/IEC/IEEE, la *verificación* confirma que se cumplen requisitos especificados, y la *validación* confirma que se cumplen los requisitos para un uso previsto específico. El método usa *validación* para cualquier evidencia explícita de que un artefacto o una decisión satisface su intención declarada bajo el contexto declarado (glosario). Por tanto, cubre lo que los estándares llaman verificación además de validación. Quien aplique el método dentro de un proceso basado en estándares puede registrar cuál de las dos es cada registro de validación.

## 4.2 Lo que el método agrega, y lo que no

Los estándares definen dónde ocurre la ingeniería y, en varios casos, qué registros debe producir. El método agrega tres cosas que los estándares anteriores no ofrecen como tales:

1. **Evaluación independiente del proceso que produjo los registros.** Un registro producido bajo 12207, bajo Scrum o por un desarrollador individual se evalúa con las mismas reglas (capítulo 5).
2. **Semántica explícita para la desviación y la incertidumbre.** Son los resultados *compensada* e *indeterminada*, la exigencia de que la compensación no borre obligaciones y la regla de que la evidencia ausente no prueba la ausencia (capítulo 7.5).
3. **Una relación definida entre el fallo y el registro de ingeniería.** Es la clasificación de factores del capítulo 7.7.

El método no es un esquema de evaluación de la conformidad. Aplicarlo no demuestra conformidad con ningún estándar, y la conformidad con un estándar no implica que se cumplan las obligaciones del método. Es posible seguir un proceso conforme a estándares y aun así producir software que no pueda diagnosticarse tras un fallo porque el razonamiento detrás de elecciones clave nunca se hizo explícito. El mismo proceso también puede producir un producto de ingeniería cuando la intención y las decisiones se capturan de forma que permitan evaluar posteriormente por qué el sistema se comporta como lo hace.

## 4.3 Marcos de proceso vs ejecución del método
El método es ortogonal a los estándares de proceso. Restringe resultados de ingeniería, no flujos de trabajo, y permite que el mismo proceso sea conforme o no conforme dependiendo de si se preserva el razonamiento explícito. Esta separación significa que el método no requiere cambios en fases de ciclo de vida ni en rutinas organizacionales.

Esto no es un conflicto con enfoques ágiles, planificados o híbridos. El método puede adoptarse de manera incremental en cualquiera de ellos, porque evalúa lo que existe en lugar de prescribir cómo debe ordenarse o coordinarse el trabajo.

La compatibilidad con estándares importa porque habilita diagnosabilidad y evaluación en contextos distintos. Los estándares pueden especificar actividades y artefactos, pero no pueden, por sí solos, explicar el fallo como evidencia de ingeniería. El método llena esa brecha sin alterar la estructura de trabajo definida por estándares.

El resultado es una división clara de responsabilidades: los estándares definen dónde ocurre la ingeniería y, a menudo, qué debe registrar; el método define qué debe ser cierto del registro para que el trabajo cuente como ingeniería responsable, y cómo se evalúa.
