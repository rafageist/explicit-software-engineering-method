# 2. De software a producto de software

El software y los productos de software no son equivalentes. El software consiste en código ejecutable, configuraciones y datos que producen comportamiento. Un producto de software es el resultado de la ingeniería: software cuyo comportamiento, restricciones y propósito pueden explicarse, validarse y justificarse. Este capítulo se centra en la diferencia entre funcionalidad que funciona y resultados de ingeniería responsables.

---

## 2.1 El software es salida; un producto es un resultado

El software puede existir sin intención de ingeniería. Puede funcionar, pasar pruebas o satisfacer necesidades inmediatas y, aun así, permanecer opaco respecto a por qué existe en su forma actual, qué decisiones lo moldearon, de qué supuestos depende, qué trade-offs se aceptaron y cómo se estableció su corrección o idoneidad. Un producto de software, en cambio, es un resultado cuyas propiedades son intencionales y explicables.

Considere un pipeline de datos que ha crecido mediante arreglos urgentes. Produce salidas correctas la mayoría de los días, pero nadie puede explicar por qué existen ciertos umbrales o qué modos de fallo se aceptaron. El sistema funciona, pero su comportamiento no puede justificarse sin reconstruir decisiones pasadas de memoria.

Por contraste, un servicio de cara al cliente puede comportarse dentro de restricciones definidas y, cuando aparece una regresión de latencia, el equipo puede trazar el cambio a una decisión específica y a la condición que pretendía satisfacer. El servicio sigue fallando en condiciones reales, pero el fallo es diagnosticable como resultado de ingeniería.

La distinción no trata de tamaño, pulido, metas de rendimiento o conteo de bugs. Trata de responsabilidad de ingeniería.

---

## 2.2 La ingeniería hace la diferencia

La ingeniería introduce estructura entre problema y solución. Un producto no se define por tener más funciones o menos errores; se define por la visibilidad y la responsabilidad del razonamiento que lo moldeó. Por eso un prototipo puede ser software válido y aun así no calificar como producto: puede demostrar comportamiento sin preservar el razonamiento de ingeniería detrás de él.

Una vez que existe responsabilidad, la diagnosabilidad se vuelve una propiedad del producto en lugar de una consecuencia de quién recuerda la historia.

---

## 2.3 Los productos son diagnosticables; el código por sí solo no

Una propiedad definitoria de un producto de ingeniería es la diagnosabilidad. El éxito en producción no crea responsabilidad de ingeniería de manera retroactiva; solo muestra que el sistema es aceptable en este momento. Cuando ocurren fallos, un producto de ingeniería permite al equipo explicar el fallo en términos del razonamiento que condujo al comportamiento, en lugar de depender de narrativa retrospectiva o del recuerdo individual.

Esta distinción explica por qué la organización por sí sola no puede cerrar la brecha.

---

## 2.4 El proceso no crea productos por sí mismo

Los procesos coordinan actividades. No garantizan que el razonamiento de ingeniería se preserve. Un equipo puede seguir un proceso bien definido y aun así producir software cuyo comportamiento no puede explicarse más allá de defectos superficiales. Esto no es una crítica del proceso; es el reconocimiento de que organización y responsabilidad son preocupaciones distintas.

La diferencia es estructural, por eso requiere un mecanismo explícito.

---

## 2.5 El papel de la explicitud

La explicitud es el mecanismo mediante el cual el software se eleva a producto. Cuando el razonamiento se preserva, los resultados son intencionales, la calidad se vuelve defendible en contexto, los fallos son explicables y el aprendizaje es acumulativo en lugar de anecdótico. Esta es la diferencia estructural entre software que funciona y un producto de ingeniería.

---

## 2.6 Resumen

El software puede existir sin ingeniería; los productos no. Un producto de software se define por el razonamiento explícito, no por las mecánicas de entrega. Los procesos pueden producir software; un método define las obligaciones que permiten que el software califique como producto.

Esta distinción motiva la necesidad de obligaciones explícitas. El siguiente paso es definir cuáles son esas obligaciones, sin prescribir todavía cómo deben organizarse los equipos.
