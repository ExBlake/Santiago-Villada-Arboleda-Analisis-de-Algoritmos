"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """
    Encuentra la mejor racha probando todos los pares de dias (i, j).

    Para cada dia de inicio i, la suma se acumula al avanzar el dia final j,
    de modo que cada par cuesta O(1) y el total es Θ(n²).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    n = len(valores)
    mejor_inicio = 0
    mejor_fin = 0
    suma_maxima = float("-inf")

    for i in range(n):
        suma = 0

        for j in range(i, n):
            suma += valores[j]

            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima

def suma_cruzada(valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """
    Encuentra el mejor tramo que cruza el punto medio.

    Hace un barrido hacia la izquierda desde medio y otro hacia la derecha
    desde medio + 1, y combina los dos mejores. Cuesta Θ(n) en el rango.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado (inclusive).
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo que incluye al
        menos un elemento de cada mitad.
    """
    suma = 0
    mejor_suma_izquierda = float("-inf")
    mejor_izquierda = medio
    for i in range(medio, inicio - 1, -1):
        suma += valores[i]
        if suma > mejor_suma_izquierda:
            mejor_suma_izquierda = suma
            mejor_izquierda = i

    suma = 0
    mejor_suma_derecha = float("-inf")
    mejor_derecha = medio + 1
    for j in range(medio + 1, fin + 1):
        suma += valores[j]
        if suma > mejor_suma_derecha:
            mejor_suma_derecha = suma
            mejor_derecha = j

    suma_total = mejor_suma_izquierda + mejor_suma_derecha

    return mejor_izquierda, mejor_derecha, suma_total


def subarreglo_maximo(valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """
    Encuentra la mejor racha por divide y venceras.

    Divide el rango en dos mitades, resuelve cada una de forma recursiva,
    calcula el mejor tramo cruzado y devuelve el mejor de los tres casos.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar (inclusive).
        fin: indice final del rango a considerar (inclusive).

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo dentro de
        valores[inicio..fin].
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    inicio_izq, fin_izq, suma_izq = subarreglo_maximo(valores, inicio, medio)
    inicio_der, fin_der, suma_der = subarreglo_maximo(valores, medio + 1, fin)
    inicio_cruz, fin_cruz, suma_cruz = suma_cruzada(
        valores, inicio, medio, fin
    )

    if suma_izq >= suma_cruz and suma_izq >= suma_der:
        return inicio_izq, fin_izq, suma_izq
    if suma_der >= suma_izq and suma_der >= suma_cruz:
        return inicio_der, fin_der, suma_der
    return inicio_cruz, fin_cruz, suma_cruz
    