# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Santiago Villada Arboleda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `dfd2892`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 11 / 20 |
| Documentación y organización del informe | 3 / 10 |
| **Total** | **71 / 100** |
| **Nota (0–5)** | **3.55** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que cumpla la ventana de 4 horas, y nombra esa ventana como la restricción que se incumple.
- Explica que duplicar la velocidad del servidor no cambia cómo crece el trabajo cuando aumentan los datos.
- Da un segundo ejemplo propio (imágenes de facturas) con cantidad de datos y restricción de tiempo.
- En la Parte 2 relaciona el tiempo con la energía acumulada día tras día e identifica dos perjuicios (paciente y operador) diciendo quién asume el costo.

**Lo que puede mejorar:**
- En el ejemplo propio faltó explicar por qué ese algoritmo no escalaba (qué crecía y cómo), no solo que era lento.
- La tensión ética se queda en "debe ser preciso"; falta decir que el orden decide a quién se llama primero y qué obligación adicional trae eso.
- La parte ambiental no da ninguna cifra ni estimación, aunque fuera aproximada.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué entradas de tamaño fijo se toma cada uno, y justifica usar el peor caso por la ventana estricta.
- Deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro verificando la condición del caso 2.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- En el análisis línea a línea de insertion sort muchas líneas quedan como "depende de los datos"; falta sumar los costos de forma explícita para llegar a la cota.
- La explicación del caso promedio de insertion sort es descriptiva; falta justificar por qué es cuadrático.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `list.sort()`.
- Los tres generadores producen lotes del tamaño pedido, sin repetidos y con semilla.
- Las funciones de los dos algoritmos y de los generadores tienen type hints y docstring.

**Lo que puede mejorar:**
- Hay varias faltas de PEP 8: líneas con espacios, falta de líneas en blanco entre funciones, archivos sin salto de línea final, líneas largas en `parte4_complejidad.py`.
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` tienen docstring incompleto (sin `Args`/`Returns` en las gráficas) y `medir` no tipa el parámetro `algoritmo`.
- El sentido de orden (ascendente) no se declara, aunque Tamiza pide de mayor a menor.

## 4. Calidad del análisis de las gráficas (11 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y se ven correctamente en el informe.
- Identifica con apoyo en las curvas que el escenario C es el peor caso, B el mejor y A el intermedio, y lo contrasta con su predicción.
- En 4.2 concluye que merge sort conviene y lo relaciona con las complejidades de 4.1.

**Lo que puede mejorar:**
- Falta por completo el concepto técnico de 4.3: no hay recomendación final, ni respuesta a la compra del servidor con un dato medido, ni extrapolación a 1.200.000 registros declarada como estimación, ni otra consideración (memoria, estabilidad).
- La gráfica de la Parte 4 usa tamaños distintos a los de la Parte 3 (llega solo a 3000), y no explica qué pasa con los tamaños pequeños con datos concretos.
- Las conclusiones no citan valores medidos (por ejemplo, el tiempo de cada algoritmo para un tamaño concreto).

## 5. Documentación y organización del informe (3 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está en una ubicación válida y tiene todos los archivos y las tres gráficas pedidas.
- Las gráficas se incrustan con ruta relativa que sí funciona.
- Los mensajes de commit son descriptivos.

**Lo que puede mejorar:**
- El informe no trae su nombre completo ni las instrucciones para reproducir el experimento.
- Ninguna parte práctica enlaza su código (`parte3_casos.py`, `parte4_complejidad.py`, `algoritmos.py`, `datos.py`).
- Solo hay 3 commits sobre el laboratorio y se piden al menos cinco.
- La imagen de la Parte 4 tiene una descripción que habla de otra gráfica.
- Hay copias de las gráficas del laboratorio en `graficas/` de la raíz del repositorio, distintas de las de la carpeta del laboratorio; el informe usa las de la carpeta correcta, pero conviene no duplicarlas.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, los algoritmos ordenan correctamente en los tres escenarios y se generan las gráficas.

## Para el próximo laboratorio
- Complete todas las secciones que pide el laboratorio (aquí faltó el concepto técnico de 4.3) antes de entregar.
- Agregue su nombre, las instrucciones de reproducción y los enlaces al código en el informe.
- Respalde cada conclusión con un dato medido citando la gráfica y el tamaño de entrada.
- Corra `pycodestyle` y complete los docstrings y type hints de todas las funciones.
- Haga commits más pequeños y frecuentes (mínimo cinco) y evite duplicar archivos en el repositorio.
