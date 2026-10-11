import random
import time
import os

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def generar_entradas(n: int) -> list[int]:
    """
    Genera una entrada de tamaño n con numeros entre -100 y 100.

    Args:
        n: tamaño de la lista que se va a generar.

    Returns:
        Una lista de numeros enteros positivos y negativos.
    """

    entrada = [random.randint(-100, 100) for _ in range(n)]
    return entrada


def graficar_tiempo(
    tamanios: list[int],
    tiempos_dividir_vencer: list[float],
    tiempos_fuerza_bruta: list[float],
) -> None:
    """
    Grafica los tiempos de ejecucion de ambos algoritmos.
    
    Args:
        tamanios: tamaños de entrada medidos.
        tiempos_dividir_vencer: tiempos de divide y venceras, en segundos.
        tiempos_fuerza_bruta: tiempos de la fuerza bruta, en segundos.

    """
    plt.figure()
    plt.plot(tamanios, tiempos_dividir_vencer, marker="o",
             label="Dividir y vencer")
    plt.plot(tamanios, tiempos_fuerza_bruta, marker="o",
             label="Fuerza bruta")
    plt.title("Subarreglo máximo: tiempos vs n")
    plt.xlabel("Tamaño de la entrada (n, número de días)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    
    carpeta = os.path.dirname(os.path.abspath(__file__))
    carpeta_graficas = os.path.join(carpeta, "graficas")
    os.makedirs(carpeta_graficas, exist_ok=True)
    plt.savefig(os.path.join(carpeta_graficas, "tiempo_vs_n.png"))
    plt.close()

if __name__ == "__main__":

    random.seed(42)

    tamanios = [10, 50, 100, 500, 1000, 2000, 4000]
    tiempos_dividir_vencer = []
    tiempos_fuerza_bruta = []

    for tamanio in tamanios:
        entrada = generar_entradas(tamanio)

        # Medir el tiempo de divide y venceras.
        inicio_reloj = time.perf_counter()
        resultado_dividir_vencer = subarreglo_maximo(
            entrada, 0, len(entrada) - 1
        )
        fin_reloj = time.perf_counter()
        tiempos_dividir_vencer.append(fin_reloj - inicio_reloj)

        # Medir el tiempo de fuerza bruta.
        inicio_reloj = time.perf_counter()
        resultado_fuerza_bruta = subarreglo_fuerza_bruta(entrada)
        fin_reloj = time.perf_counter()
        tiempos_fuerza_bruta.append(fin_reloj - inicio_reloj)

        assert resultado_dividir_vencer[2] == resultado_fuerza_bruta[2]

        print("Tamaño de entrada:", tamanio)
        print("Suma máxima:", resultado_dividir_vencer[2])
        print("Tiempo dividir y vencer: ", tiempos_dividir_vencer[-1], " segundos")
        print("Tiempo fuerza bruta: ", tiempos_fuerza_bruta[-1], " segundos")
        print("Las sumas de ambos algoritmos coinciden")


    print("\nResumen de tiempos:")
    print("Tamaño | Dividir y vencer (s) | Fuerza bruta (s)")
    for i in range(len(tamanios)):
        print(
            f"{tamanios[i]:6} | "
            f"{tiempos_dividir_vencer[i]:20.6f} | "
            f"{tiempos_fuerza_bruta[i]:16.6f}"
        )
    graficar_tiempo(tamanios, tiempos_dividir_vencer, tiempos_fuerza_bruta)
