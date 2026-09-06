# def insertion_sort(arreglo: list, puntos_de_control:set[int]) -> list:
#     """
#     Ordena una lista de menor a mayor utilizando el metodo de insercion

#     Args:
#         arreglo: lusta de elementos
#         puntos_de_control: conjunto de índices donde se deben registrar los puntos de control

#     Returns:
#         La lista ordenada.
#     """
#     for i in range(1, len(arreglo)):
#         if i in puntos_de_control:
#             arreglo[:i] == sorted(arreglo[:i])
#         clave = arreglo[i] # representa el elemento que va a insertar
#         j = i - 1
#         while j >= 0 and arreglo[j] > clave:
#             arreglo[j + 1] = arreglo[j]
#             j -= 1
#         arreglo[j + 1] = clave
#     return arreglo 

# if __name__ == "__main__":
#     arreglo = [5,2,4,6,1,3]
#     n = len(arreglo)
#     puntos = {2, n // 2, n-1}
#     arreglo_ordenado = insertion_sort(arreglo, puntos)
#     print(arreglo_ordenado)
    
import random
import matplotlib.pyplot as plt


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

def generar_entradas(n: int) -> dict[str, list[int]]:
    """
    Genera 3 entradas de tamaño n: ordenada, invertida y aleatoria

    Args:
        n: tamaño de cada una de las 3 listas generadas

    Returns:
        Diccionario con las claves "ordenada", "invertida" y "aleatoria"
    """
    ordenada = list(range(n))
    invertida = list(range(n, 0, -1))

    aleatoria = ordenada.copy()
    random.shuffle(aleatoria)
    return {"ordenada": ordenada, "invertida": invertida, "aleatoria": aleatoria}

def medir_comparaciones(tamanios: list[int]) -> dict[str, list[int]]:
    """
    Mide comparaciones de insertion sort para cada tipo de entrada

    Args:
        tamanios: lista con los tamaños de las entradas a medir

    Returns:
        Diccionario con una clave por tipo de entrada y como valor, la lista de comparaciones medidas para cada tamaño n
    """
    resultados = {"ordenada": [], "invertida": [], "aleatoria": []}
    
    for n in tamanios:
        entradas = generar_entradas(n)
        for tipo, arreglo in entradas.items():
            _, comparaciones, _ = insertion_sort(arreglo)
            resultados[tipo].append((comparaciones))
            
    return resultados        

def graficar_operaciones(tamanios: list[int], resultados: dict[str, list[int]]) -> None:
    """
    Grafica comparaciones vs n para cada tipo de entrada
    """
    plt.figure()
    for tipo, valores in resultados.items():
        plt.plot(tamanios, valores, label=tipo)
    plt.title("Comparaciones de Insertion Sort")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-2/comparaciones_insertion_sort.png")

if __name__ == "__main__":
    tamanios = [10,50,100,200,400,800]
    resultados = medir_comparaciones(tamanios)
    graficar_operaciones(tamanios, resultados)
    
    # arreglo = [5,2,4,6,1,3]
    # arreglo_ordenado = insertion_sort(arreglo)
    # print(arreglo_ordenado)    