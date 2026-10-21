# Índice

- [Prólogo - Contexto y motivación](prologo.md)

- [0. El problema](el-problema.md)
  - 0.1 Situación
  - 0.2 Declaración del problema
  - 0.3 Hipótesis
  - 0.4 Objetivo
  - 0.5 Alcance y no objetivos

- [1. Por qué esto es un método](1-por-que-un-metodo.md)
  - 1.1 Metodología vs método vs proceso
  - 1.2 Por qué "método" encaja
  - 1.3 Dependencia sin rigidez
  - 1.4 Separación de responsabilidades
  - 1.5 El método como función evaluativa

- [2. De software a producto de software](2-de-software-a-producto.md)
  - 2.1 El software es salida; un producto es un resultado
  - 2.2 La ingeniería hace la diferencia
  - 2.3 Los productos son diagnosticables; el código por sí solo no
  - 2.4 El proceso no crea productos por sí mismo
  - 2.5 El papel de la explicitud
  - 2.6 Resumen

- [3. Reglas normativas centrales (borrador)](3-reglas-normativas.md)
  - 3.0 Cómo leer estas reglas
    - 3.0.1 Palabras clave normativas
    - 3.0.2 Términos usados por todas las reglas
    - 3.0.3 Resultados
    - 3.0.4 Estatus del texto
  - 3.1 Regla 1 - Declaración de intención (obligatoria)
  - 3.2 Regla 2 - Explicitación de decisiones (obligatoria)
  - 3.3 Regla 3 - Trazabilidad de artefactos (obligatoria)
  - 3.4 Regla 4 - Requisito de validación (contextual)
  - 3.5 Regla 5 - Declaración de supuestos (obligatoria)
  - 3.6 Regla 6 - Compensación explícita (obligatoria)
  - 3.7 Regla 7 - Conciencia de parámetros (obligatoria)
  - 3.8 Regla 8 - Diagnosabilidad del fallo (regla de resultado)
  - 3.9 Meta-nota
  - 3.10 Conclusión

- [4. Relación con estándares](4-relacion-con-estandares.md)
  - 4.1 Lo que abordan estándares identificables
  - 4.2 Lo que el método agrega, y lo que no
  - 4.3 Marcos de proceso vs ejecución del método

- [5. Ortogonalidad respecto a marcos de proceso](5-ortogonalidad.md)
  - 5.1 Espacios de problema distintos
  - 5.2 Dependencias lógicas vs prescripción del proceso
  - 5.3 Coexistencia con la estructura del proceso
  - 5.4 Lo que significa y no significa la ortogonalidad
  - 5.5 Resumen

- [6. El fallo como resultado del método](6-fallo-como-resultado-del-metodo.md)
  - 6.1 Libertad de organización, no libertad de opacidad
  - 6.2 El fallo no es una sorpresa
  - 6.3 El fallo como evidencia, no como narrativa
  - 6.4 Responsabilidad a nivel de método
  - 6.5 Por qué el fallo mejora la ingeniería
  - 6.6 Límites de la diagnosabilidad
  - 6.7 Resumen

- [7. Esbozo de formalización - Método Explícito de Ingeniería de Software](7-formalizacion.md)
  - 7.0 Estatus de los enunciados
  - 7.1 Universo de discurso
    - 7.1.1 Conjuntos de entidades
    - 7.1.2 Predicados (tipado)
    - 7.1.3 Atributos de los registros
  - 7.2 Relaciones núcleo (modelo de grafo)
    - 7.2.1 Relaciones fundamentales
    - 7.2.2 Trazabilidad (derivada)
    - 7.2.3 Instancias de obligación
    - 7.2.4 Los parámetros como interpretaciones
  - 7.3 Las reglas como aplicabilidad y requisito
    - 7.3.1 Regla 1 - Declaración de intención
    - 7.3.2 Regla 2 - Explicitación de decisiones
    - 7.3.3 Regla 3 - Trazabilidad de artefactos
    - 7.3.4 Regla 4 - Requisito de validación
    - 7.3.5 Regla 5 - Declaración de supuestos
    - 7.3.6 Regla 6 - Compensación explícita
    - 7.3.7 Regla 7 - Conciencia de parámetros
    - 7.3.8 Regla 8 - Diagnosabilidad del fallo
    - 7.3.9 Matriz regla-predicado y cambios respecto a 0.2.1
  - 7.4 Capa deóntica (obligaciones, permisos, consecuencias)
    - 7.4.1 DEBE como obligación condicional
    - 7.4.2 La compensación como obligación contraria al deber
    - 7.4.3 Recomendaciones
  - 7.5 Evaluación con evidencia incompleta
    - 7.5.1 Instantánea y completitud
    - 7.5.2 Evaluación trivalente
    - 7.5.3 Validez de las compensaciones
    - 7.5.4 Función de resultado
    - 7.5.5 Veredicto agregado
  - 7.6 Tiempo, versiones y reproducibilidad
  - 7.7 Diagnosabilidad
  - 7.8 Expresividad: qué cubre la lógica de primer orden
  - 7.9 Notas prácticas (no normativas)

- [8. Aplicación y evaluación del método](8-aplicacion-y-evaluacion.md)
  - 8.1 Aplicación, evaluación y proceso
  - 8.2 Alcance evaluado
  - 8.3 Conjunto de parámetros
  - 8.4 Evidencia y procedencia
    - 8.4.1 Contenido mínimo de un registro
    - 8.4.2 Procedencia
    - 8.4.3 Accesibilidad
    - 8.4.4 Navegabilidad
    - 8.4.5 La evidencia faltante no es evidencia de ausencia
  - 8.5 Ciclo de vida de la compensación
  - 8.6 Contrato de evaluación
  - 8.7 Informe de resultados
  - 8.8 Puntos de evaluación
  - 8.9 Independencia de las herramientas

- [9. Ejemplos desarrollados](9-ejemplos-desarrollados.md)
  - 9.1 Escenario A - Cambio desde el código
  - 9.2 Escenario B - Desarrollo desde modelos
  - 9.3 Escenario C - Cambio de emergencia en producción
  - 9.4 Escenario D - Software heredado
  - 9.5 Escenario E - Investigación de un fallo
  - 9.6 Resumen de los escenarios

- [10. Contexto de ingeniería, ingeniería de contexto y el método](10-contexto-de-ingenieria.md)
  - 10.1 Tres cosas distintas
  - 10.2 Dónde se encuentran
  - 10.3 Independencia de las plataformas
  - 10.4 Por qué la distinción importa para el método

- [Referencias](referencias.md)
  - Lógica, semántica y lenguaje normativo
  - Trazabilidad, decisiones y procedencia
  - Análisis de fallos
  - Estándares
  - Trabajo relacionado del autor

- [Glosario](glosario.md)
