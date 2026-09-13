import matplotlib.pyplot as plt
from pathlib import Path
from time import perf_counter
from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso
)

# Carpeta de graficas, anclada a la ubicacion de este archivo (no al
# directorio desde el que se ejecute el script). Se crea si no existe.
GRAFICAS_DIR = Path(__file__).resolve().parent / "graficas"
GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)

def medir(tamanios: list[int]) -> dict[str, dict[str, list]]:
    """
    Mide tiempo y comparaciones de insertion sort para cada escenario.

    Args:
        tamanios: lista con los tamaños de las entradas a medir.

    Returns:
        Diccionario con los tiempos y comparaciones de cada escenario.
    """

    resultados = {
        "aleatorio": {
            "tiempos": [],
            "comparaciones": []
        },
        "casi_ordenado": {
            "tiempos": [],
            "comparaciones": []
        },
        "inverso": {
            "tiempos": [],
            "comparaciones": []
        }
    }

    for n in tamanios:
        entradas = {
            "aleatorio": generar_aleatorio(n, 42),
            "casi_ordenado": generar_casi_ordenado(n, 42),
            "inverso": generar_inverso(n)
        }

        for tipo, arreglo in entradas.items():
            inicio = perf_counter()
            _, comparaciones = insertion_sort(arreglo)
            fin = perf_counter()
            tiempo = fin - inicio
            resultados[tipo]["tiempos"].append(tiempo)
            resultados[tipo]["comparaciones"].append(comparaciones)
    return resultados

def graficar_comparaciones(tamanios: list[int], resultados: dict[str, dict[str, list]]) -> None:
    """
    Grafica comparaciones vs n para cada escenario.
    """

    plt.figure()
    for tipo, datos in resultados.items():
        plt.plot(tamanios, datos["comparaciones"], label=tipo)

    plt.title("Comparaciones de Insertion Sort")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig(GRAFICAS_DIR / "parte3_comparaciones.png")
    plt.close()


def graficar_tiempo(tamanios: list[int], resultados: dict[str, dict[str, list]]) -> None:
    """
    Grafica tiempo vs n para cada escenario.
    """

    plt.figure()
    for tipo, datos in resultados.items():
        plt.plot(tamanios, datos["tiempos"], label=tipo)
    plt.title("Tiempo de ejecución de Insertion Sort")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(GRAFICAS_DIR / "parte3_tiempo.png")
    plt.close()

if __name__ == "__main__":
    import os
    print(os.getcwd())
    tamanios = [100, 200, 400, 800, 1600, 3200, 6400]
    resultados = medir(tamanios)
    graficar_comparaciones(tamanios,resultados)
    graficar_tiempo(tamanios,resultados)