#Script Anterior sin refactorizar

# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))

from typing import List


def calcular_promedio(numeros: List[float]) -> float:
    """Calcula el promedio aritmético de una lista de números.

    Args:
        numeros: Lista de enteros o flotantes a promediar.

    Returns:
        El promedio aritmético como número flotante.
    """
    suma_total = 0.0
    for i in numeros:
        suma_total += i
    return suma_total / len(numeros)


def main() -> None:
    lista_numeros = [1, 2, 3, 4, 5] # Lista de prueba
    promedio = calcular_promedio(lista_numeros)
    print(promedio)


if __name__ == "__main__":
    main()