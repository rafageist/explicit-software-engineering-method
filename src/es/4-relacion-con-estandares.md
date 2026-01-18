# 4. Relación con estándares

El Método Explícito de Ingeniería de Software está diseñado para operar dentro de estándares de ingeniería de software, no para reemplazarlos. Asume que los estándares definen el contexto de trabajo y aclara cómo se establece la responsabilidad de ingeniería dentro de ese contexto.

## 4.1 Compatibilidad con estándares IEEE e ISO
Los estándares de ingeniería de software IEEE / ISO definen marcos de proceso, describiendo actividades, roles y estructuras de ciclo de vida esperadas en la práctica de ingeniería. Establecen el escenario de lo que debe hacerse, pero por lo general no exigen la captura explícita del razonamiento de ingeniería ni aseguran que el fundamento se preserve en una forma analizable.

Este método complementa esos estándares al restringir resultados: exige que el razonamiento de ingeniería sea lo suficientemente explícito para soportar evaluación y diagnóstico. Usados en conjunto, los estándares definen dónde ocurre la ingeniería, mientras que el método define qué debe ser cierto para que esas actividades cuenten como ingeniería responsable.

Es posible seguir un proceso conforme a estándares y aun así producir software que no pueda diagnosticarse tras un fallo porque el razonamiento detrás de elecciones clave nunca se hizo explícito. El mismo proceso también puede producir un producto de ingeniería cuando la intención y las decisiones se capturan de forma que permitan evaluar posteriormente por qué el sistema se comporta como lo hace.

## 4.2 Marcos de proceso vs ejecución del método
El método es ortogonal a los estándares de proceso. Restringe resultados de ingeniería, no flujos de trabajo, y permite que el mismo proceso sea conforme o no conforme dependiendo de si se preserva el razonamiento explícito. Esta separación significa que el método no requiere cambios en fases de ciclo de vida ni en rutinas organizacionales.

Esto no es un conflicto con enfoques ágiles, planificados o híbridos. El método puede adoptarse de manera incremental en cualquiera de ellos, porque evalúa lo que existe en lugar de prescribir cómo debe ordenarse o coordinarse el trabajo.

La compatibilidad con estándares importa porque habilita diagnosabilidad y evaluación en contextos distintos. Los estándares pueden especificar actividades y artefactos, pero no pueden, por sí solos, explicar el fallo como evidencia de ingeniería. El método llena esa brecha sin alterar la estructura de trabajo definida por estándares.

El resultado es una división clara de responsabilidades: los estándares definen dónde ocurre la ingeniería, y el método define qué debe ser cierto para que cuente como ingeniería.
