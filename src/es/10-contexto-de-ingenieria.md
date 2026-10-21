# 10. Contexto de ingeniería, ingeniería de contexto y el método

Este capítulo no es normativo. Sitúa el método en relación con dos ideas vecinas: el contexto de la ingeniería y la ingeniería de contextos. Ambas se discuten en el ensayo *El contexto de la ingeniería y la ingeniería de contextos* [Rodríguez Ramírez 2026]. El objetivo es mantener separadas las tres ideas, porque confundirlas haría que el método dependiera de una forma particular de almacenar o entregar el conocimiento.

## 10.1 Tres cosas distintas

1. El **contexto de ingeniería** es el conocimiento, las restricciones y las circunstancias en que ocurre la ingeniería y que explican una solución: requisitos, modelos, decisiones, alternativas descartadas, supuestos, pruebas, defectos, conversaciones y las relaciones entre todos ellos. Existe lo registre alguien o no. Una parte es explícita, otra es tácita y otra se ha perdido.
2. La **ingeniería de contexto** es la construcción, selección, preservación y entrega deliberadas del contexto relevante a alguien o algo que lo necesita para actuar: un ingeniero que se incorpora a un equipo, un revisor o un agente basado en un modelo de lenguaje al que se le pide modificar código. Es una actividad con sus propias decisiones de diseño: granularidad, identidad, relaciones, recuperación y actualidad.
3. **El método** define obligaciones que hacen explícita, trazable y evaluable una parte del contexto de ingeniería: intención, decisiones, supuestos, trade-offs, validaciones y desviaciones aceptadas, con un nivel de explicitud fijado por parámetros declarados.

El método no describe el contexto de ingeniería; exige que una parte definida de él exista como registro. No realiza ingeniería de contexto; le es indiferente cómo se almacenan, recuperan o entregan los registros.

## 10.2 Dónde se encuentran

- **El registro de ingeniería es una proyección del contexto de ingeniería.** La instantánea $\Sigma$ del capítulo 7 es la parte del contexto de ingeniería que es explícita, dentro del alcance y las fuentes declarados, en una línea base. Lo que permanece tácito queda fuera de $\Sigma$ y, para la evaluación, no existe.
- **El método fija un mínimo, no un máximo.** Un equipo puede conservar mucho más contexto del que el método exige. El método solo exige que, dentro del alcance, puedan evaluarse las obligaciones del capítulo 3.
- **La ingeniería de contexto puede consumir el registro.** Antes de que un agente o una persona modifique un artefacto, un paso de ingeniería de contexto puede recuperar las intenciones, decisiones, supuestos y validaciones a los que el artefacto se traza. El método hace que estos registros existan y estén vinculados. No define cómo se seleccionan ni cómo se presentan.
- **La ingeniería de contexto puede producir candidatos a registro, no registros.** Las herramientas y los modelos pueden proponer vínculos, reconstruir justificaciones o resumir el historial. Según el modelo de procedencia (8.4.2), ese resultado es *inferido* hasta que una persona responsable lo confirma. Una relación inferida por un modelo no adquiere la autoridad de una decisión aprobada ni de una prueba realmente ejecutada.
- **La evaluación necesita identidad y versiones estables.** El contrato de evaluación (8.6) exige referencias inmutables a la evidencia. Cualquier almacén de contexto que se use como fuente de evidencia debe proporcionarlas, sea cual sea su tecnología: archivos en un repositorio, una base de datos o un grafo de conocimiento.

## 10.3 Independencia de las plataformas

Como el método se define sobre registros y relaciones, y no sobre un modelo de almacenamiento, puede aplicarse con archivos Markdown y un repositorio, un gestor de incidencias, un repositorio de modelos, una base de datos de grafos o una plataforma dedicada. No debe adquirir conceptos que existan solo en una de ellas.

Divengine Studio puede implementar un evaluador opcional del método sobre su propio modelo de contexto de ingeniería. Ese evaluador sería una implementación entre otras posibles. Tendría que respetar los límites del capítulo 8.9: un contrato de evaluación expuesto, entradas inmutables, vínculos inferidos separados de los registrados y la revisión manual todavía posible. El método no se convertiría en un método de Studio, y su vocabulario no pasaría a ser obligatorio para todos los proyectos que Studio gestione.

## 10.4 Por qué la distinción importa para el método

Los agentes basados en modelos de lenguaje hacen más visible la ausencia de razonamiento de ingeniería explícito. Un agente puede leer código y proponer un cambio localmente razonable sin saber que ese código implementa una restricción, que una alternativa se descartó por razones de seguridad o que un comportamiento extraño es deliberado. Hacer explícito ese razonamiento es lo que el método siempre ha exigido. Lo que cambian los agentes es el número de lectores y el costo de que el razonamiento no esté ahí.

También añaden un riesgo nuevo: que el razonamiento inferido se confunda con el razonamiento registrado. Las distinciones de procedencia del capítulo 8 son la respuesta del método a ese riesgo. Valen igual si la inferencia proviene de un modelo, de un analizador estático o de un ingeniero bienintencionado que reconstruye el pasado.
