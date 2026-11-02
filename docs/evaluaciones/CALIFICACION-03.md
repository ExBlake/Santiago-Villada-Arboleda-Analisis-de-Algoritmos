# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Santiago Villada Arboleda · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `d0b3334`

Excelente trabajo: entregó un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **100 / 100** |
| **Nota (0–5)** | **5.00** |

## 1. Corrección conceptual (20 / 20)
**Lo que hizo bien:**
- Explicó bien la colisión con el ejemplo de las guías 10, 24 y 17 con m = 7, y comparó encadenamiento y direccionamiento abierto con ventajas y costos.
- Justificó por qué la tabla no sirve para rangos y estimó la altura del árbol degenerado (cerca de 400.000) frente al equilibrado (cerca de 19).
- Recomendó tabla hash más árbol equilibrado y declaró la estimación a 5.000.000 de envíos como estimación, apoyada en su medición.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justificó por qué buscar una guía inexistente en la lista recorre los n nodos, y por qué la tabla cuesta el "1" de calcular la casilla más el α de recorrer su lista.
- Nombró el supuesto de hashing uniforme simple y explicó que, si todo cae en una casilla, la tabla se vuelve una lista.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: la lista inserta al inicio y busca con un `while`; la tabla reutiliza la lista en cada casilla y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren búsquedas exitosas e infructuosas, la colisión forzada con m = 7, el factor de carga 3/7 y 20 colecciones aleatorias. Todas pasan.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre ellas.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda. La primera cubre 7 valores de n con las dos curvas en los mismos ejes; la segunda cubre 8 valores de α entre 0,25 y 10.
- Calculó el factor de crecimiento de la lista (≈ 2,01 al duplicar n) y de la tabla (≈ 1,10), y los contrastó con lo esperado.
- Describió que el tiempo sube casi en línea recta con α, coherente con `Θ(1 + α)`.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` está en `laboratorios/` (ubicación válida) con todos los archivos del entregable.
- El `README.md` sigue el orden pedido, tiene su nombre, instrucciones para reproducir, enlaces al código en cada parte y las gráficas incrustadas con ruta relativa que funciona.
- Hizo 5 commits descriptivos sobre el laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan y `medicion.py` corre completo y genera las dos gráficas. Los tiempos que obtuve varían respecto a los suyos, pero la forma de las curvas es la misma.
