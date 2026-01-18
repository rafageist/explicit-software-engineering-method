# 6. El fallo como resultado del método

Los sistemas complejos fallan. Esto no es una anomalía; es una constante. El método no pretende eliminar el fallo. Pretende hacer que el fallo sea diagnosticable como evidencia de ingeniería y no como un artefacto narrativo.

El problema no es que ocurran fallos. El problema es que a menudo no pueden explicarse objetivamente, incluso después del hecho. Lo que distingue a la ingeniería del ensayo y error es la capacidad de explicar el fallo con evidencia trazable. El método trata el fallo como un resultado evaluable del razonamiento de ingeniería, no como una excepción inesperada.

---

## 6.1 Libertad de organización, no libertad de opacidad

Los equipos y organizaciones son libres de organizar su trabajo como consideren. El método no interfiere con modelos de coordinación, cadencia de planificación, herramientas ni estructura interna. Lo que restringe no es cómo se organiza el trabajo, sino qué debe ser explícito para que el resultado califique como ingeniería. Se preserva la libertad de organización; no la opacidad.

---

## 6.2 El fallo no es una sorpresa

La mayoría de los fallos de software son previsibles en retrospectiva. Después de un fallo, los equipos suelen reconstruir que el problema no se entendía del todo, que los supuestos resultaron falsos, que se tomaron decisiones bajo presión, que la validación fue insuficiente o que se aceptaron trade-offs en silencio. El problema no es que esas cosas ocurrieran; el problema es que no fueron explícitas.

Aquí importa la distinción entre "qué ocurrió" y "por qué esto fue posible". Lo primero puede reconstruirse con logs y cronologías. Lo segundo requiere artefactos de razonamiento explícito que expliquen por qué se permitió que existiera un estado del sistema.

---

## 6.3 El fallo como evidencia, no como narrativa

Sin artefactos explícitos, el fallo se explica mediante narrativa: memoria, opinión y racionalización retrospectiva. Los postmortems suelen convertirse en historias sobre lo que pasó en lugar de explicaciones de por qué fue posible. Con el método aplicado, el fallo puede explicarse mediante evidencia como intención ausente, decisiones no documentadas, supuestos inválidos, validación ausente, brechas sin compensación o parámetros mal configurados. Este cambio transforma el fallo de un relato a un diagnóstico técnico basado en trazabilidad y obligaciones explícitas.

En un caso, una caída de servicio se explica como "tráfico inesperado". La cronología es clara, pero la explicación es débil. Bajo el método, el diagnóstico apunta a una intención ausente sobre capacidad, una decisión de escalado no documentada, un supuesto inválido sobre la forma de la carga y la ausencia de validación o compensación por omitir pruebas de capacidad.

En otro caso, un defecto en etapa final se atribuye a "cambios apresurados". La narrativa asigna la presión como causa, pero no la base de ingeniería. Bajo el método, el diagnóstico muestra que un cambio crítico salió sin validación registrada, que nunca se documentó una compensación para esa brecha y que el parámetro de tolerancia al riesgo estaba mal configurado para la vida útil esperada del sistema.

---

## 6.4 Responsabilidad a nivel de método

Cuando un sistema falla, la responsabilidad puede evaluarse al nivel del método: si se declaró y comprendió la intención, si las decisiones fueron explícitas y justificadas, si los supuestos se identificaron y se siguieron, si la validación correspondió al riesgo, si las compensaciones fueron explícitas y si los parámetros contextuales fueron realistas. Si estas preguntas no pueden responderse, el método no se aplicó plenamente. El fallo, en ese caso, no es misterioso; es esperable.

Esto no implica negligencia. Indica dónde el registro de ingeniería estuvo incompleto y dónde las obligaciones no se cumplieron o se aceptaron sin compensación explícita. El método hace visible esa brecha para poder evaluarla y corregirla.

---

## 6.5 Por qué el fallo mejora la ingeniería

Porque el fallo se vuelve explicable, se vuelve reutilizable. Los equipos pueden aprender entre proyectos, mejorar la toma de decisiones, ajustar niveles de explicitud, refinar compensaciones y evolucionar su uso del método. El fallo deja de ser un punto final y se convierte en entrada que fortalece la responsabilidad de ingeniería con el tiempo.

---

## 6.6 Resumen

El fallo es inevitable; la opacidad es opcional. El método no dicta cómo trabajan los equipos, pero sí qué debe ser explícito para que el trabajo sea ingeniería. Cuando ocurre un fallo, debe ser explicable en términos del método; la madurez de ingeniería crece a partir de fallos diagnosticados, no de fallos evitados.

El método no previene todos los fallos, y algunos fallos permanecen irreductibles o externos. Su alcance es la evaluación del razonamiento de ingeniería, no la eliminación de resultados adversos. En ese sentido, el fallo se convierte en una señal medible del estado de ingeniería, y el siguiente paso es formalizar cómo puede realizarse esa evaluación.
