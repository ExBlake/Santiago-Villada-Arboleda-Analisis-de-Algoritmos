import matplotlib.pyplot as plt
import random

def subarreglo_maximo_por_fuerza_bruta(arreglo: list):
    """
    Encuentre el subarreglo de mayor suma en un arreglo original calculando todas las posibles combinaciones

    Args:
        arreglo: arreglo a procesaar para extraer el maximo subarreglo
        
    Return: 
        Una tupla (mejor_inicio, mejor_fin, suma_maxima, operaciones) 
    """
    
    n = len(arreglo)
    mejor_inicio, mejor_fin = 0,0
    suma_maxima = float('-inf')
    operaciones = 0
    
    for i in range(n):
        operaciones += 1
        for j in range(i, n):
            operaciones += 1
            suma = 0
            for k in range(i, j + 1):
                operaciones += 1
                suma += arreglo[k]

            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima, operaciones

def graficar_operaciones(tamanios: list[int], resultados: list[int]) -> None:
    """
    Grafica comparaciones vs n para cada tipo de entrada
    """
    plt.figure()
    plt.plot(tamanios, resultados)
    plt.title("Subarreglo máximo por fuerza bruta: operaciones vs n")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-4/fuerza-bruta-maximo-subarreglo.png")
    
def generar_entradas(n: int) -> list[int]:
    """
    Genera una entrada de tamanio n

    Args:
        n: tamanio de cada una de las tres listas generadas

    Returns:
        Arreglo de numeros negativos y positivos
    """
    entrada = [random.randint(-100, 100) for _ in range(n)]
    random.shuffle(entrada)
    return entrada

if __name__ == "__main__":
    # arreglo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # mejor_inicio, mejor_fin, suma_maxima, operaciones = subarreglo_maximo_por_fuerza_bruta(arreglo)
    # print(mejor_inicio, mejor_fin, suma_maxima, operaciones)
    
    tamanios = [10, 50, 100, 200, 400, 800]
    cantidad_operaciones = []
    for tamanio in tamanios:
        _, _, _, operaciones = subarreglo_maximo_por_fuerza_bruta(generar_entradas(tamanio))
        cantidad_operaciones.append(operaciones)
        print(tamanio, cantidad_operaciones)
    graficar_operaciones(tamanios, cantidad_operaciones)