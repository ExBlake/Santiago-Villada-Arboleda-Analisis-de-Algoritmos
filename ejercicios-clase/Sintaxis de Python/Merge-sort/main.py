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

if __name__ == "__main__":
    arreglo = [38, 27, 43, 3, 9, 82, 10]
    print(arreglo)