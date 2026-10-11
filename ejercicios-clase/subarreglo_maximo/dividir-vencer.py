import matplotlib.pyplot as plt
import random
import time

def subarreglo_maximo_por_dividir_y_vencer(arreglo: list, inicio: int, fin: int):
    """
    Encuentre el subarreglo de mayor suma en un arreglo original con le paradigma dividir y vencer

    Args:
        arreglo: arreglo a procesaar para extraer el maximo subarreglo
        inicio: índice de inicio del rango a considerar (SE INCLUYE)
        fin: índice de fin del rango a considerar (SE INCLUYE)
        
    Return: 
        Una tupla (mejor_inicio, mejor_fin, suma_maxima, operaciones) 
    """
    if inicio == fin:
        return inicio, fin, arreglo[inicio]
    
    medio = (inicio + fin) // 2
    
    inicio_izquierda, fin_izquierda, suma_izquierda = subarreglo_maximo_por_dividir_y_vencer(arreglo, inicio, medio)
    inicio_derecha, fin_derecha, suma_derecha = subarreglo_maximo_por_dividir_y_vencer(arreglo, medio + 1, fin)
    inicio_cruzado, fin_cruzado, suma_cruzado = suma_cruzada(arreglo, inicio, medio, fin)
    
    if suma_izquierda >= suma_cruzado and suma_izquierda >= suma_derecha:
        return inicio_izquierda, fin_izquierda, suma_izquierda
    if suma_derecha >= suma_izquierda and suma_derecha >= suma_cruzado:
        return inicio_derecha, fin_derecha, suma_derecha
    return inicio_cruzado, fin_cruzado, suma_cruzado

def suma_cruzada(arreglo: list, inicio: int, medio: int, fin: int) -> tuple[int, int, float]:
    """
    Encuentra el subarreglo maximo que cruza el punto medio

    Args:
        arreglo: arreglo a procesar
        inicio: indice inicial del rango considerado
        medio: indice del punto de division
        fin: indice final del rango considerado
        
    Returns:
        Una tupla (mejor_inicio, mejor_fin, suma_maxima)    
    """
    
    suma = 0
    suma_maxima_izquierda = float('-inf')
    mejor_izquierda = medio
    for i in range(medio, inicio - 1, -1):
        suma += arreglo[i]
        if suma > suma_maxima_izquierda:
            suma_maxima_izquierda = suma
            mejor_izquierda = i

    suma = 0
    suma_maxima_derecha = float('-inf')
    mejor_derecha = medio + 1
    for j in range(medio + 1, fin + 1):
        suma += arreglo[j]
        if suma > suma_maxima_derecha:
            suma_maxima_derecha = suma
            mejor_derecha = j

    return mejor_izquierda, mejor_derecha, suma_maxima_izquierda + suma_maxima_derecha

def graficar_tiempo(tamanios: list[int], tiempos_dividir_vencer: list[int], tiempos_fuerza_bruta: list[int]) -> None:
    """
    Grafica tiempos vs n para cada tipo de entrada
    """
    plt.figure()
    plt.plot(tamanios, tiempos_dividir_vencer, label="Dividir y vencer")
    plt.plot(tamanios, tiempos_fuerza_bruta, label="Fuerza bruta")
    plt.title("Subarreglo máximo por dividir y vencer: tiempos vs n")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-4/comparacion.png")

def generar_entradas(n: int) -> list[int]:
    """
    Genera una entrada de tamanio n

    Args:
        n: tamanio de cada una de las tres listas generadas

    Returns:
        Arreglo de numeros negativos y positivos
    """
    entrada = [random.randint(-100, 100) for _ in range(n)]
    entrada.append(500)
    random.shuffle(entrada)
    return entrada

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

if __name__ == "__main__":
    # arreglo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # mejor_inicio, mejor_fin, suma_maxima = subarreglo_maximo_por_dividir_y_vencer(arreglo, 0, len(arreglo) - 1)
    # print(mejor_inicio, mejor_fin, suma_maxima)
    
    tamanios = [10, 50, 100, 200, 400, 800, 1600]
    tiempos_dividir_vencer = []
    tiempos_fuerza_bruta = []
    
    for tamanio in tamanios:
        entrada = generar_entradas(tamanio)
        
        inicio_reloj = time.perf_counter()
        subarreglo_maximo_por_dividir_y_vencer(entrada, 0, tamanio - 1)
        fin_reloj = time.perf_counter()
        tiempos_dividir_vencer.append(fin_reloj - inicio_reloj)
        
        inicio_reloj = time.perf_counter()
        subarreglo_maximo_por_fuerza_bruta(entrada)
        fin_reloj = time.perf_counter()
        tiempos_fuerza_bruta.append(fin_reloj - inicio_reloj)
        
    graficar_tiempo(tamanios, tiempos_dividir_vencer, tiempos_fuerza_bruta)
        
    
    