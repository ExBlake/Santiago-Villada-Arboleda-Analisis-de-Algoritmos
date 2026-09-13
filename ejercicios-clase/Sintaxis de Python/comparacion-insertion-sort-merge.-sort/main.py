import math
import random
import matplotlib.pyplot as plt

from time import perf_counter
 
def insertion_sort(arreglo: list) -> tuple[list, int, int]:
    """
    Ordena una lista de menor a mayor utilizando el metodo de insercion

    Args:
        arreglo: lusta de elementos

    Returns:
        Tupla (arreglo, comparaciones, desplazamientos)
    """
    comparaciones = 0
    desplazamientos = 0
    n = len(arreglo)
    for i in range(1, n):
        clave = arreglo[i] # representa el elemento que va a insertar
        j = i - 1
        
        while j >= 0:
            comparaciones += 1
            if arreglo[j] <= clave:
                break
            arreglo[j + 1] = arreglo[j]
            desplazamientos += 1
            j -= 1
        arreglo[j + 1] = clave
        
    return arreglo, comparaciones, desplazamientos

def merge_sort(arreglo: list[int]) -> list[int]:
    """
    Ordena una lista de menor a mayor utilizando el metodo de merge sort

    Args:
        arreglo: lista de elementos a ordenar

    Returns:
        La lista ordenada.
    """
    # Caso Base
    if len(arreglo) <= 1:
        return arreglo

    # Caso recursivo
    mitad = len(arreglo) // 2
    izquierda = merge_sort(arreglo[:mitad])
    derecha = merge_sort(arreglo[mitad:])

    return merge(izquierda, derecha)

def merge(izquierda: list[int], derecha: list[int]) -> list[int]:
    """
    Combina dos listas ordenadas en una sola lista ordenada

    Args:
        izquierda: lista ordenada de menor a mayor del subarreglo a la izquierda
        derecha: lista ordenada de menor a mayor del subarreglo a la derecha

    Returns:
        Una liosta ordenada con todos los elementos de izq y derecha
    """
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def medir (algoritmo, tamanio: int, repeticion: int = 3) -> float:
    """
    Cronometra un algotirmo de ordenamiento


    Args:
        algoritmo: funcion que recibe una lista desordenada y devuelve ordenada
        tamanio: cantidad de elementos de la entrada
        repeticion: cuantas veces medir el algoritmo

    Returns:
        Tiempo de observado en segundos
    """
    
    tiempo = []
    for _ in range(repeticion): 
        datos = [random.randint(0, 10000) for _ in range(tamanio)]
        inicio = perf_counter()
        algoritmo(datos)
        fin = perf_counter()
        tiempo_total = fin - inicio
        tiempo.append(tiempo_total)
    return min(tiempo)

def graficar_operaciones(tamanios: list[int], resultados_insertion: list[float], resultados_merge: list[float]) -> None:
    """
    Grafica tiempo vs n para cada tipo de entrada
    """
    plt.figure()
    plt.plot(tamanios, resultados_insertion, label="Insertion Sort")
    plt.plot(tamanios, resultados_merge, label="Merge Sort")
    plt.title("Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempoi de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-3/merge-vs-insertion.png")


if __name__ == "__main__":
    tamanios = list(range(10, 1200, 100))
    tiempos_insertion_sort = []
    tiempos_merge_sort = []
    for n in tamanios:
        tiempo_insertion = medir(insertion_sort, n)
        tiempos_insertion_sort.append(tiempo_insertion)
        
    for n in tamanios:
        tiempo_merge = medir(merge_sort, n)
        tiempos_merge_sort.append(tiempo_merge)  
    
    graficar_operaciones(tamanios, tiempos_insertion_sort, tiempos_merge_sort)  