"""Pruebas de subarreglo.py: verifican que ambas soluciones coinciden."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo, suma_cruzada

# Caso 1: serie de ocho dias de la situacion problema.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]

assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

# Resultado Caso 1
print("Fuerza bruta:", subarreglo_fuerza_bruta(serie))
print("Divide y venceras:", subarreglo_maximo(serie, 0, len(serie) - 1))

# Caso 2: una serie de un solo elemento.
serie = [7]

assert subarreglo_fuerza_bruta(serie)[2] == 7
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 7

# Resultado Caso 2
print("Fuerza bruta:", subarreglo_fuerza_bruta(serie))
print("Divide y venceras:", subarreglo_maximo(serie, 0, len(serie) - 1))

# Caso 3: todos los valores son negativos.
serie = [-8, -3, -6, -2, -9]

assert subarreglo_fuerza_bruta(serie)[2] == -2
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -2

# Resultado Caso 3
print("Fuerza bruta:", subarreglo_fuerza_bruta(serie))
print("Divide y venceras:", subarreglo_maximo(serie, 0, len(serie) - 1))

# Caso 4: todos los valores son positivos.
serie = [2, 4, 1, 3]

assert subarreglo_fuerza_bruta(serie)[2] == 10
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 10

# Resultado Caso 4
print("Fuerza bruta:", subarreglo_fuerza_bruta(serie))
print("Divide y venceras:", subarreglo_maximo(serie, 0, len(serie) - 1))

# Caso 5: la mejor racha cruza el punto medio.
serie = [4, -1, 5, 2, -1, 3]

assert subarreglo_fuerza_bruta(serie)[2] == 12
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 12

# Resultado Caso 5
print("Fuerza bruta:", subarreglo_fuerza_bruta(serie))
print("Divide y venceras:", subarreglo_maximo(serie, 0, len(serie) - 1))

# Caso 6: verificar que las funciones no modifiquen la lista.
serie = [3, -2, 5, -1]
copia = serie.copy()

subarreglo_fuerza_bruta(serie)
subarreglo_maximo(serie, 0, len(serie) - 1)

assert serie == copia

print("Lista original:", copia)
print("Lista despues de ejecutar las funciones:", serie)

# Caso 7: comparar ambos algoritmos en 30 listas aleatorias.
random.seed(42)

for _ in range(30):
    tamanio = random.randint(1, 30)
    serie = [
        random.randint(-100, 100)
        for _ in range(tamanio)
    ]

    resultado_fuerza_bruta = subarreglo_fuerza_bruta(serie)
    resultado_dividir_vencer = subarreglo_maximo(
        serie, 0, len(serie) - 1
    )

    assert resultado_fuerza_bruta[2] == resultado_dividir_vencer[2]

    print("Fuerza bruta:", resultado_fuerza_bruta[2])
    print("Divide y venceras:", resultado_dividir_vencer[2])

print("Todas las pruebas se ejecutaron correctamente.")