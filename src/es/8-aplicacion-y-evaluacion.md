# 8. Aplicación y evaluación del método

Las reglas del capítulo 3 enuncian obligaciones, y el capítulo 7 define cómo se evalúan. Este capítulo establece qué debe declarar un equipo o un evaluador para que la evaluación pueda realizarse, reproducirse y refutarse. Es un protocolo de *declaraciones*, no de actividades. No indica cuándo evaluar, quién evalúa ni en qué orden se producen los registros.

Estado: el contrato de evaluación y el modelo de resultados se proponen para la versión 0.3 y dependen, donde se indica, de las decisiones abiertas OD-6 a OD-11. No añaden obligaciones a las reglas 1-8; hacen evaluables las existentes.

## 8.1 Aplicación, evaluación y proceso

Una *aplicación del método* es la decisión de someter una parte definida del trabajo de ingeniería a la rendición de cuentas que exige el método. Una *evaluación* es un acto concreto de determinar los resultados de las obligaciones de una aplicación frente a una instantánea de la evidencia. Una aplicación puede evaluarse muchas veces; cada evaluación es un resultado separado y versionado.

Ninguna de las dos depende de un proceso. Un equipo que usa Scrum puede evaluar en cada integración; un equipo con un contrato dirigido por plan puede evaluar en cada hito; un auditor puede evaluar una sola vez, años después. El método define lo que la evaluación necesita, no cuándo ocurre.

## 8.2 Alcance evaluado

Un alcance evaluado declara:

1. **Frontera del sistema.** Qué sistema, componentes o servicios se incluyen. Los elementos fuera de la frontera están *fuera de alcance*: no producen instancias de obligación, y los fallos causados allí son *externos* para el diagnóstico (7.7).
2. **Conjunto de cambios.** Qué cambios de ingeniería se evalúan, delimitados por líneas base: por ejemplo "todos los cambios integrados en `main` entre las etiquetas `v4.2.0` y `v4.3.0`", o "las revisiones 18 a 25 del modelo y el código generado a partir de ellas".
3. **Unidad de cambio.** Qué cuenta como un cambio (un commit, una merge request, una revisión de modelo, un despliegue de configuración). La unidad determina los sujetos de la Regla 1.
4. **Fuentes de evidencia.** Dónde se buscan los registros: repositorios, gestores de incidencias, registros de decisiones, repositorios de modelos, sistemas de CI, herramientas de revisión, almacenes documentales. Un registro fuera de las fuentes declaradas no existe para la evaluación.
5. **Declaraciones de completitud.** Para qué relaciones y fuentes la evaluación afirma completitud (7.5.1), por ejemplo "toda ejecución de CI sobre `main` está en el sistema de CI" o "todas las decisiones del componente X están en `docs/adr/`". Donde no se declara completitud, la ausencia produce *indeterminada*, no *violada*.
6. **Frontera de adopción** (opcional). Para sistemas que adoptan el método tras años de operación, una línea base antes de la cual los artefactos son *heredados*. Los artefactos heredados producen instancias de obligación solo cuando un cambio dentro del alcance los modifica o cuando la política de criticidad los clasifica como críticos (capítulo 9, Escenario D).

*Fuera de alcance* y *no aplicable* son cosas distintas. Un elemento fuera de alcance no se evalúa. Una instancia no aplicable sí se evalúa, y el conjunto de parámetros decide que la regla no le aplica. Ambas situaciones deben ser visibles en el informe.

## 8.3 Conjunto de parámetros

Un conjunto de parámetros (7.2.4) es un registro versionado vinculado a la aplicación. Tiene dos capas.

Los **descriptores de contexto** caracterizan la situación: criticidad del dominio, tolerancia al riesgo, presión regulatoria, escala del equipo, vida útil esperada y otros que el equipo considere relevantes. Son entradas de las políticas; las reglas no los leen directamente.

Las **políticas** deciden los predicados que usan las reglas. Bajo OD-9, un conjunto de parámetros debe contener una política para cada uno de los siguientes:

| Política | Decide | Ejemplo |
|---|---|---|
| Unidad de cambio y trivialidad | $\mathsf{NonTrivial}$ | "Una merge request es trivial si solo cambia comentarios, formato o datos de prueba." |
| Impacto e irreversibilidad | $\mathsf{Impactful}$, $\mathsf{Irreversible}$, $\mathsf{Balances}$ | "De impacto: afecta una API pública, un formato de datos persistido, un control de seguridad o una dependencia. Irreversible: migraciones de datos sin reversión." |
| Artefactos que afectan el comportamiento | $\mathsf{AffectsBehavior}$ | "Código fuente, configuración, esquemas, código de infraestructura y modelos usados para generación." |
| Criticidad | $\mathsf{Critical}$ | "Crítico: todo lo que esté bajo `payments/` o `auth/`, y cualquier cambio en un cálculo regulado." |
| Adecuación de la validación | $\mathsf{Adequate}$ | "Artefactos críticos: pruebas automatizadas en la interfaz afectada más una revisión hecha por alguien distinto del autor." |
| Admisibilidad de la compensación | $\mathsf{Admissible}$, $\mathsf{PermitsPermanent}$ | "La validación de cálculos de dosis no es compensable. No se permite la aceptación permanente para artefactos críticos." |
| Autoridad de aceptación de riesgo | $\mathsf{MayAccept}$ | "Riesgos sobre artefactos críticos: el responsable del servicio o, durante un incidente declarado, el comandante del incidente. Nunca el autor del cambio por sí solo." |

Una política es un criterio, no necesariamente un umbral, y puede requerir juicio. Cuando lo requiere, el juicio se registra como una valoración con su autor (7.6). Las políticas pueden ser estrictas o permisivas. El método no decide cuán estricto debe ser un contexto; exige que la exigencia se declare, de modo que pueda evaluarse y cuestionarse.

Modificar un conjunto de parámetros produce una nueva versión. Las evaluaciones indican qué versión usaron. Un conjunto de parámetros modificado para que una evaluación pasada resulte favorable queda a la vista como tal, porque la versión anterior y la evaluación anterior permanecen.

## 8.4 Evidencia y procedencia

### 8.4.1 Contenido mínimo de un registro

Cada registro usado como evidencia tiene un identificador, un tipo (intención, decisión, supuesto, trade-off, validación, compensación, valoración), un contenido o una referencia a él, la versión o el resumen criptográfico de aquello a lo que se refiere, un agente responsable, el momento en que se registró, su procedencia y su fuente. El método no prescribe un formato: la descripción de una pull request, un registro de decisión de arquitectura, un ticket, un elemento de un modelo o una fila de una base de datos pueden ser registros si contienen esta información.

### 8.4.2 Procedencia

*Interpretación propuesta (OD-8).* Los registros tienen uno de cuatro tipos de procedencia. La distinción es compatible con modelos generales de procedencia como W3C PROV [Moreau and Missier 2013], que el método no exige.

| Procedencia | Significado | Satisface obligaciones |
|---|---|---|
| contemporánea | registrada mientras se hacía el trabajo | sí |
| retrospectiva | registrada después por una persona responsable del trabajo, a partir de su propio conocimiento | sí |
| reconstruida | justificación histórica recuperada a partir de evidencia (historial, tickets, entrevistas) y confirmada por una persona responsable | sí, prospectivamente; nunca se presenta como la justificación original |
| inferida | propuesta por análisis o herramientas (incluidos modelos de lenguaje) y no confirmada | no; a lo sumo convierte *violada* en *indeterminada* |

El método no fabrica historia ni permite que las herramientas lo hagan. Un vínculo inferido puede ser una buena hipótesis, pero hasta que una persona responsable lo confirme no tiene la autoridad de una decisión registrada. La diferencia entre *retrospectiva* y *reconstruida* importa. La primera es el relato del propio autor; la segunda es una interpretación de rastros, y puede ser errónea.

### 8.4.3 Accesibilidad

Un registro referenciado que el evaluador no puede leer (permisos, almacenamiento eliminado, un sistema externo) es *inaccesible*. Las fórmulas que dependen de su contenido se evalúan como *desconocidas* (7.5.2). La inaccesibilidad se informa junto con la referencia, para que alguien con acceso pueda resolverla. Los evaluadores NO DEBEN suponer que la evidencia inaccesible habría sido favorable o desfavorable.

### 8.4.4 Navegabilidad

Un vínculo es navegable en ambas direcciones (Regla 3) cuando puede resolverse desde cada extremo usando las fuentes declaradas. Un mensaje de commit que cita un ticket es navegable desde el commit. Es navegable desde el ticket si el repositorio es una fuente declarada y puede buscarse en él el identificador del ticket, o si el ticket enlaza de vuelta. Un vínculo que solo existe en la memoria de una persona, o en una fuente ajena a la evaluación, no es navegable.

### 8.4.5 La evidencia faltante no es evidencia de ausencia

Cuando el alcance es incompleto, la falta de evidencia no prueba que el trabajo no se hiciera. La evaluación decide entre *violada* e *indeterminada* únicamente mediante sus declaraciones de completitud. Declarar completitud es una responsabilidad: una declaración que luego resulta falsa invalida los resultados que dependían de ella (Proposición 7.3).

## 8.5 Ciclo de vida de la compensación

Una compensación registra una desviación de la que alguien rinde cuentas. Su vida tiene los siguientes estados:

| Estado | Significado |
|---|---|
| registrada | la compensación existe con su contenido requerido |
| aceptada | un agente autorizado por la política de autoridad ha aceptado el riesgo declarado |
| activa | aceptada y no vencida; la instancia referenciada está *compensada* |
| remediada | se hizo el trabajo faltante; la instancia pasa a *satisfecha* para las versiones que cubre la remediación, y la compensación se cierra |
| vencida | se alcanzó la condición de revisión mientras el sujeto seguía en operación, sin remediación ni renovación; la instancia deja de estar *compensada* y pasa a *violada* (o *indeterminada*, si el requisito no puede decidirse) |
| renovada | una nueva compensación, con una nueva aceptación, sustituye a la vencida |
| retirada | la desviación se revirtió (por ejemplo, el cambio se deshizo) |

**Contenido requerido.** Referencia a la instancia de obligación (regla y versión del sujeto). Declaración del riesgo aceptado (qué puede salir mal, con qué probabilidad y con qué consecuencia, en la medida en que se conozca). Agente que acepta y momento de la aceptación. Condición de revisión: una fecha o un evento *(propuesta, OD-6)*. Plan de remediación (DEBERÍA).

**Historial.** Las compensaciones nunca se editan en el lugar ni se eliminan. Una compensación renovada o corregida sustituye a la anterior, y ambas permanecen en el registro. Este historial es lo que permite que una evaluación o un diagnóstico posteriores establezcan qué riesgo se aceptó, quién lo aceptó y cuándo.

**Compensaciones retroactivas.** Una compensación registrada después de la exposición que cubre se marca como retroactiva *(propuesta, OD-6)*. Cuenta desde el momento en que se registra. No puede demostrar que un fallo anterior a ese momento materializó un riesgo aceptado.

## 8.6 Contrato de evaluación

Una evaluación solo es reproducible si sus entradas están fijadas (Definición 7.16). El *contrato de evaluación* es el registro de esas entradas y de los resultados.

| Campo | Contenido |
|---|---|
| Versión del método y del conjunto de reglas | p. ej. ESEM 0.3.0, conjunto de reglas con las decisiones abiertas resueltas o las interpretaciones propuestas aplicadas (enumeradas) |
| Alcance evaluado | frontera del sistema, conjunto de cambios por líneas base, unidad de cambio, frontera de adopción |
| Conjunto de parámetros | identificador y versión |
| Fuentes de evidencia | cada fuente con referencias inmutables (hashes de commit, identificadores de revisión, resúmenes criptográficos de contenido) |
| Declaraciones de completitud | por relación y fuente |
| Momento de evaluación | el instante $t$ usado para la validez de las compensaciones |
| Juicios | valoraciones usadas, con autor y fecha |
| Instancias de obligación | regla, sujeto, aplicabilidad |
| Resultados | por instancia, con explicación diagnóstica y referencias a la evidencia |
| Caminos de trazabilidad | para las instancias de la Regla 3, el camino encontrado o el punto donde se interrumpe |
| Compensaciones | instancias referenciadas, validez, estado, retroactividad |
| Notas | recomendaciones no seguidas, evidencia inaccesible |
| Veredicto y perfil | veredicto agregado y recuentos por resultado (8.7) |
| Evaluador | quién realizó la evaluación, y con qué herramientas, si las hubo |

Una serialización ilustrativa (no normativa; cualquier formato con el mismo contenido es válido):

```yaml
evaluation:
  method: ESEM 0.3.0
  ruleset: {version: 0.3.0, interpretations: [OD-1/B, OD-2/B, OD-5/B, OD-6/A1+B1]}
  scope:
    boundary: [orders-api, payment-adapter]
    change_set: {repo: git@example.org:shop/orders.git, from: v4.2.0, to: v4.3.0}
    change_unit: merge-request
  parameters: {id: PS-shop, version: 7}
  sources:
    - {id: repo, ref: 9f2c1e0}
    - {id: tracker, ref: "export 2026-10-20T09:00Z sha256:3b1d..."}
    - {id: ci, ref: "runs on main, 2026-09-01..2026-10-20"}
  completeness:
    - {relation: validates, source: ci, part: "main branch"}
  time: 2026-10-21T10:00Z
  judgments: [{id: J-12, author: m.ortiz, on: D-31, about: Impactful}]
  outcomes:
    - {instance: [R4, payment-adapter@a41b2c], outcome: compensated, by: C-9,
       explanation: "no adequate validation of a41b2c; C-9 valid until 2026-10-24"}
    - {instance: [R3, orders-api/retry.yaml@9f2c1e0], outcome: satisfied,
       path: [retry.yaml, D-31, I-14]}
  verdict: compliant-with-compensations
  profile: {satisfied: 41, compensated: 1, violated: 0, not_applicable: 12, indeterminate: 0}
```

**Versiones del método y evaluaciones anteriores** *(propuesta, OD-11)*. Una evaluación está ligada a la versión de su conjunto de reglas y nunca cambia por una versión posterior del método. Reevaluar bajo una nueva versión produce un nuevo contrato, y toda comparación debe indicar ambas versiones. Las versiones del método siguen `MAJOR.MINOR.PATCH`. Un cambio MAJOR puede convertir resultados anteriores *satisfecha* o *no aplicable* en *violada*. Un cambio MINOR solo puede resolver resultados *indeterminada* o añadir material no normativo. Un PATCH es editorial. Por debajo de 1.0, las versiones MINOR pueden contener cambios normativos, que el registro de cambios debe enumerar.

## 8.7 Informe de resultados

Cada instancia de obligación se informa con su resultado y con una explicación que nombra lo que lo decidió: la aplicabilidad (qué política, qué juicio), el requisito (qué registros, o qué ausencia bajo qué declaración de completitud) y la compensación (qué registro, y por qué es válida o inválida). Un resultado sin explicación no puede refutarse, y una evaluación que no puede refutarse no rinde cuentas.

El veredicto agregado (Definición 7.15) se informa junto con el perfil completo de resultados. Un resumen que oculta instancias compensadas o indeterminadas tras la palabra "conforme" tergiversa la evaluación.

Una evaluación NO DEBE afirmar:

- que el sistema es correcto, seguro o apto para su propósito. El método evalúa el registro de ingeniería, no el comportamiento del producto;
- que un trabajo no se hizo, cuando solo falta evidencia de él bajo la completitud declarada;
- la completitud del diagnóstico de fallos (7.7, *Límites*);
- objetividad más allá de sus entradas declaradas. Donde las políticas requirieron juicio, los juicios forman parte del resultado.

## 8.8 Puntos de evaluación

El método no prescribe puntos de evaluación. Las opciones habituales son: antes de integrar un cambio, antes de una entrega, periódicamente para auditoría y después de un fallo. Evaluar temprano detecta registros faltantes mientras las personas que pueden escribirlos aún recuerdan. Evaluar tarde mide lo que realmente sobrevivió. Un equipo puede combinar ambas cosas. En todos los casos la evaluación usa el contrato anterior, de modo que los resultados obtenidos en distintos puntos son comparables.

## 8.9 Independencia de las herramientas

Una evaluación puede realizarse a mano, con una hoja de cálculo, con consultas sobre repositorios o con un evaluador dedicado. El método no depende de ninguna de estas opciones. Una herramienta que implemente el método debe:

- exponer el contrato de evaluación y la explicación de cada resultado;
- mantener inmutables, para una evaluación dada, la versión del método, el conjunto de parámetros y las referencias a la evidencia;
- mantener los vínculos inferidos separados de los registrados;
- dejar posible la revisión manual.

Divengine Studio puede ofrecer un evaluador opcional para este método. El método se define con independencia de él y de cualquier otra plataforma, y su vocabulario no depende de cómo una herramienta almacene el contexto (capítulo 10).
