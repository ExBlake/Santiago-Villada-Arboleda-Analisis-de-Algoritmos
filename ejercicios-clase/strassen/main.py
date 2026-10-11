import random
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
Matriz = list[list[float]]

def multiplicar_metodo_clasico (a: Matriz, b: Matriz):
    """
    Multiplica dos matrices cuadradas con la formula de Cij
    Args:
        a: Matriz nxn
        b: Matriz nxn
    Returns:
        El producto matricial de a x b y el numero de multiplicaciones que realiza el algoritmo
"""
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    multiplicaciones = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
                multiplicaciones += 1
    return c, multiplicaciones

def sumar(a: Matriz, b: Matriz):
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def restar(a: Matriz, b: Matriz):
    n = len(a)
    c = [[0,0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c


def generar_matriz (n: int):
    """
    Genera una matriz de nxn con valores aleatorios
    
    Args: 
        n: tamanio de la matriz a generar
        
    Returns:
        Una matriz de nxn
    """
    
    matriz_generada = [[random.randint(-5,5) for _ in range(n)] for _ in range(n)]
    return matriz_generada


def deducir_complejidad (tamanios: list[int]):
    """
    Corre la funcion multiplicar_metodo_clasico sobre tamanios crecientes y muestra la cantidad de operaciones realizadas
    Args:
        tamanios: tamanios de matriz a probar
    """
    for n in tamanios:
        _, multiplicaciones = multiplicar_metodo_clasico(generar_matriz(n), generar_matriz(n))
        print(n, multiplicaciones)
        
def strassen_2x2(a: Matriz, b: Matriz):
    """
    Multiplica dos matrices 2x2 con las 7 multiplicaciones de Strassen
    Args:
        a: Matriz cuadrada de 2x2
        b: Matriz cuadrada de 2x2
    Returns:
        El producto matricial de axb, la cantidad de multiplicaciones
    """
    
    a11 = a[0][0]
    a12 = a[0][1]
    a21 = a[1][0]
    a22 = a[1][1]
    
    b11 = b[0][0]
    b12 = b[0][1]
    b21 = b[1][0]
    b22 = b[1][1]
    
    m1 = (a11 + a22) * (b11 + b22)
    m2 = (a21 + a22) * b11  
    m3 = a11 * (b12 - b22)
    m4 = a22 * (b21 - b11)
    m5 = (a11 + a12) * b22
    m6 = (a21 - a11) * (b11 + b12)
    m7 = (a12 - a22) * (b21 + b22)
    
    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6
    
    return [[c11, c12], [c21, c22]], 7


def dividir_en_bloques(a: Matriz) -> tuple [Matriz, Matriz, Matriz, Matriz]: 
    """Parte una matriz n x n (n par) en sus 4 submatrices n/2 x n/2."""
    n = len(a)
    medio = n // 2
    a11 = [fila[:medio] for fila in a[:medio]]
    a12 = [fila[medio:] for fila in a[:medio]]
    a21 = [fila[:medio] for fila in a[medio:]]
    a22 = [fila[medio:] for fila in a[medio:]]
    return a11, a12, a21, a22

def unir_bloques (c11: Matriz, c12: Matriz, c21: Matriz, c22: Matriz) -> Matriz: 
    """Reconstruye una matriz n x n a partir de sus 4 submatrices n/2 x n/2.""" 
    superior = [fila_izq + fila_der for fila_izq, fila_der in zip(c11, c12)] 
    inferior = [fila_izq + fila_der for fila_izq, fila_der in zip (c21, c22)] 
    return superior + inferior

def strassen_dividir_vencer(a: Matriz, b: Matriz):
    """
    Multiplica dos matrices cuadradas con el Algoritmo de Strassen y cuenta ñas multiplicaciones escalares realizadas
    
    Limitaciones: 
       Solo funciona si n es una potencia de 2 (2, 4, 8, 16, ...)
       
    Args:
        a: Matriz nxn, con n potencia de 2
        b: Matriz nxn, con n potencia de 2
        
    Returns: 
        Una tupla (producto, multiplicaciones) con la matriz resultante y el total de multiplicaciones escalares usadas
    """
    n = len(a)
    #Caso Base
    if n <= 2:
        return strassen_2x2(a, b)
    
    a11, a12, a21, a22 = dividir_en_bloques(a)
    b11, b12, b21, b22 = dividir_en_bloques(b)
    
    m1, c1 = strassen_dividir_vencer(sumar(a11, a22), sumar(b11, b22))
    m2, c2 = strassen_dividir_vencer(sumar(a21, a22), b11)
    m3, c3 = strassen_dividir_vencer(a11, restar(b12, b22))
    m4, c4 = strassen_dividir_vencer(a22, restar(b21, b11))
    m5, c5 = strassen_dividir_vencer(sumar(a11, a12), b22)
    m6, c6 = strassen_dividir_vencer(restar(a21, a11), sumar(b11, b12))
    m7, c7 = strassen_dividir_vencer(restar(a12, a22), sumar(b21, b22))
    
    c11 = sumar(restar(sumar(m1, m4), m5), m7)
    c12 = sumar(m3, m5)
    c21 = sumar(m2, m4)
    c22 = sumar(restar(sumar(m1, m3), m2), m6)
    
    multiplicaciones = c1 + c2 + c3 + c4 + c5 + c6 + c7
    
    return unir_bloques(c11, c12, c21, c22), multiplicaciones


def graficar_multiplicaciones(tamanios: list[int], resultados_clasico: list[int], resultados_strassen: list[int]) -> None: 
    """
    Grafica cantidad de multiplicaciones vs n para cada algoritmo de
    multiplicacion de matrices.
    """
    plt.figure()
    plt.plot(tamanios, resultados_clasico, label="Multiplicacion clasica")
    plt.plot(tamanios, resultados_strassen, label="Strassen")
    plt.title("Multiplicacion clasica vs Strassen")
    plt.xlabel("Tamano de la matriz (n)")
    plt.ylabel("Cantidad de multiplicaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-5/clasico-vs-strassen.png")
    plt.show()

if __name__ == "__main__":
    # a = generar_matriz(4)
    # b = generar_matriz(4)

    # print("Multiplicacion con el metodo clasico")
    # multiplicacion_clasica, _ = multiplicar_metodo_clasico (a, b)
    # print(multiplicacion_clasica)
    
    # # deducir_complejidad([2, 4, 8, 16, 32])
    # # print(sumar(a, b))
    # print("Multiplicacion con el metodo de Strassen")
    # print(strassen_dividir_vencer(a, b))
    
    # assert multiplicacion_clasica == strassen_dividir_vencer(a, b)
    
    
    # Tamanios potencias de 2 para que Strassen no necesite relleno. 
    tamanios = [2, 4, 8, 16, 32, 64, 128, 256]
    tiempo_clasica = [] 
    tiempo_strassen = []
    tiempo_numpy = []
    
    
    for n in tamanios:
        a = generar_matriz(n) 
        b = generar_matriz(n)
        
        inicio = perf_counter() 
        resultado_clasico, _ = multiplicar_metodo_clasico(a,b) 
        fin = perf_counter() 
        tiempo_total = fin - inicio 
        tiempo_clasica.append(tiempo_total)
        
        inicio = perf_counter()
        resultado_strassen, _ = strassen_dividir_vencer(a,b)
        fin = perf_counter()
        tiempo_total = fin - inicio
        tiempo_strassen.append(tiempo_total)
        
        A = np.array([[1, 2], [3, 4]]) 
        B = np.array([[5, 6], [7, 8]]) 
        inicio = perf_counter()
        c = A @ B
        fin = perf_counter()
        tiempo_total = fin- inicio 
        tiempo_numpy.append(tiempo_total)
            
    print("Clasica")
    print(resultado_clasico)
    print("Strassen")
    print(resultado_strassen)
    print("Numpy")
    print(c)    
            
    plt.figure()
    plt.plot(tamanios, tiempo_clasica, label="Multiplicacion clasica")
    plt.plot(tamanios, tiempo_strassen, label="Strassen")
    plt.plot(tamanios, tiempo_numpy, label="Numpy")
    plt.title("Multiplicacion clasica vs Strassen vs Numpy")
    plt.xlabel("Tamano de la matriz (n)")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/clase-5/clasico-vs-strassen-vs-numpy.png")
    plt.show()    
