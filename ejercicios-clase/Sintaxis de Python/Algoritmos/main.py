import math
import matplotlib.pyplot as plt

def trabajo_aproximado_del_algoritmo_a(n: int) -> float:
    """
    Estima el trabajo del Algoritmo A para un tamaño n de datis
    
    Args:
        n: Tamaño de la entrada
        
    Returns:
        Trabajo aproximado del algoritmo (el numero de operaciones que realiza el algoritmo)
    """
    
    return n ** 2 

def trabajo_aproximado_del_algoritmo_b(n: int) -> float:
    """
    Estima el trabajo del Algoritmo B para un tamaño n de datis
    
    Args:
        n: Tamaño de la entrada
        
    Returns:
        Trabajo aproximado del algoritmo (el numero de operaciones que realiza el algoritmo)
    """
    
    return n * math.log2(n)

def graficar_y_comparar_algoritmos(tamanios: list[int], ruta_salida: str) -> None:
    """
    Grafica el trabajo aproximado de A y B para una lista de tamaños
    
    Args:
        tamanios: Tamaños de entrada a evaluar en orden creciente
        ruta_salida: Ruta del archivo donde se guardará la gráfica
    """
    
    trabajo_a = [trabajo_aproximado_del_algoritmo_a(n) for n in tamanios]
    trabajo_b = [trabajo_aproximado_del_algoritmo_b(n) for n in tamanios]
    trabajo_a_hardware_rapido = [valor / 2 for valor in trabajo_a]
    
    plt.figure(figsize=(8,5))
    plt.plot(tamanios, trabajo_a, label ="Algoritmo A (n**2)")
    plt.plot(tamanios, trabajo_b, label ="Algoritmo B (n log n)")
    plt.plot(tamanios, trabajo_a_hardware_rapido, label ="Algoritmo A en Hardware 2x mas rápido)")
    plt.title("Algoritmos A vs Algoritmo B")
    plt.xlabel("Tamaño de la entrada (n)")
    plt.ylabel("Trabajo aproximado")
    plt.legend(["Algoritmo A", "Algoritmo B"])
    plt.grid()
    plt.savefig(ruta_salida)
    
if __name__ == "__main__":
    tamanios = [10, 100, 500, 1000, 5000, 10000, 30000]
    graficar_y_comparar_algoritmos(tamanios, "graficas/clase-1/algoritmo_a_vs_b.png")