import matplotlib.pyplot as plt
from pathlib import Path
from time import perf_counter
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

# Para que se guarden las graficas en la carpeta "graficas" dentro del directorio actual
GRAFICAS_DIR = Path(__file__).resolve().parent / "graficas"
GRAFICAS_DIR.mkdir(parents=True, exist_ok=True)

def medir(algoritmo, datos: list[int], repeticion: int = 3) -> float:
    """
    Cronometra un algoritmo de ordenamiento.

    Args:
        algoritmo: funcion que recibe una lista y la ordena.
        datos: lista de datos que se utilizara para medir.
        repeticion: cantidad de veces que se mide el algoritmo.

    Returns:
        Tiempo minimo observado en segundos.
    """

    tiempos = []

    for _ in range(repeticion):
        inicio = perf_counter()
        algoritmo(datos)
        fin = perf_counter()

        tiempo_total = fin - inicio
        tiempos.append(tiempo_total)

    return min(tiempos)


def graficar_tiempo(tamanios: list[int],tiempos_insertion: list[float],tiempos_merge: list[float]) -> None:
    """
    Grafica el tiempo de ejecucion de Insertion Sort y Merge Sort.
    """

    plt.figure()
    plt.plot(tamanios,tiempos_insertion,label="Insertion Sort")
    plt.plot(tamanios,tiempos_merge,label="Merge Sort")
    plt.title("Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(GRAFICAS_DIR / "parte4_tiempo.png")
    plt.close()

if __name__ == "__main__":
    tamanios = [100, 200, 400, 800, 1600, 2000, 3000]
    tiempos_insertion_sort = []
    tiempos_merge_sort = []
    for n in tamanios:
        datos = generar_aleatorio(n, 42)
        tiempo_insertion = medir(insertion_sort, datos)
        tiempos_insertion_sort.append(tiempo_insertion)
        tiempo_merge = medir(merge_sort, datos)
        tiempos_merge_sort.append(tiempo_merge)
    graficar_tiempo(tamanios,tiempos_insertion_sort,tiempos_merge_sort)
    print("Insertion Sort:", tiempos_insertion_sort)
    print("Merge Sort:", tiempos_merge_sort)