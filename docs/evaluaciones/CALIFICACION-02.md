# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Santiago Villada Arboleda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `4a24a46`

Muy buen trabajo: el código funciona y el informe es claro.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que dividir y vencer empieza a ganar desde n = 50 y explica el costo de las llamadas recursivas en listas pequeñas.
- Compara bien con el máximo de un arreglo: combinar cuesta 1, la recurrencia es `T(n) = 2T(n/2) + 1` y da `Θ(n)`, igual que recorrerla una vez.
- Recomienda dividir y vencer y declara que los tiempos a 1.000.000 son una estimación, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- La estimación parte de 0,28 s y 0,004 s en n = 4000, pero la gráfica publicada muestra cerca de 0,35 s y 0,005 s. Conviene partir siempre de los valores de su propia gráfica.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + n`, explica de dónde sale cada término y la resuelve con el método maestro verificando que el trabajo extra es del orden de `n^log₂2`.
- Justifica que la fuerza bruta es `Θ(n²)` por la cantidad de pares de días.

**Lo que puede mejorar:**
- Falta mencionar el costo del caso base y que el método maestro da exactamente `Θ(n log n)` por el factor `log n` del caso 2; se queda en una frase breve.

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en 30 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos, no llama a la fuerza bruta y ninguna función cambia la lista recibida.
- Tiene tipos y explicaciones (docstrings) en las funciones.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre funciones en `subarreglo.py` y `medicion.py` (PEP 8 pide dos).
- `medicion.py` no tiene la explicación inicial del archivo.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños.
- Calcula el factor al duplicar n (de 2000 a 4000) para los dos algoritmos y lo compara con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Las cifras del informe no coinciden con la gráfica publicada: en el informe la fuerza bruta marca 0,067 s en n = 2000 y 0,28 s en n = 4000, pero en `tiempo_vs_n.png` se lee cerca de 0,09 s y 0,35 s. La tabla del informe tampoco corresponde a esa imagen. Parece que la gráfica y los números salieron de corridas distintas.
- Con solo una medición por tamaño hay ruido; repetir y promediar daría factores más confiables.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta `laboratorios/lab2-divide-y-vencer/` está en un lugar válido y tiene todos los archivos pedidos.
- El informe sigue el orden pedido, la gráfica se ve y cada parte enlaza su código. Hay varios commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción dicen `cd lab2-divide-y-vencer` desde la raíz, pero la carpeta está dentro de `laboratorios/`; el comando no funciona tal como está escrito.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y la medición corre en pocos segundos, verifica que ambas sumas coincidan y genera la gráfica.

## Para el próximo laboratorio
- Revise que los números del informe salgan de la misma corrida que la gráfica publicada.
- Repita cada medición varias veces y use el promedio.
- Deje dos líneas en blanco entre funciones y agregue la explicación inicial (docstring) de cada archivo.
- Revise que los comandos del informe funcionen desde la ruta real de la carpeta.
