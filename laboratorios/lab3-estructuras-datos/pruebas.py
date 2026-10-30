"""Pruebas de estructuras.py: verifican que la lista y la tabla coinciden."""

import random
from estructuras import ListaEnlazada, TablaHash

# Caso 1: serie de ejemplo basada en la situacion.
guias = [1010, 1024, 1017, 1005]
estados = ["en bodega", "en reparto", "en bodega", "entregado"]

lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in zip(guias, estados):
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

# Busqueda exitosa
assert lista.buscar(1024) == "en reparto"
assert tabla.buscar(1024) == "en reparto"
assert lista.buscar(1005) == "entregado"
assert tabla.buscar(1005) == "entregado"

# Busqueda infructuosa (guia mal digitada)
assert lista.buscar(1099) is None
assert tabla.buscar(1099) is None

assert lista.tamano == 4
assert tabla.tamano == 4

# Resultado Caso 1
print("Lista, guia 1024:", lista.buscar(1024))
print("Tabla, guia 1024:", tabla.buscar(1024))
print("Lista, guia 1099:", lista.buscar(1099))
print("Tabla, guia 1099:", tabla.buscar(1099))

# Caso 2: estructuras vacias.
lista = ListaEnlazada()
tabla = TablaHash(7)

assert lista.buscar(10) is None
assert tabla.buscar(10) is None
assert tabla.factor_carga() == 0

# Caso 3: colision forzada, con m = 7 las guias 10, 24 y 17 caen en la
# casilla 3.
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(17) == "en bodega"
assert tabla.buscar(99) is None
assert tabla.casillas[3].tamano == 3
assert tabla.factor_carga() == 3 / 7

# Las demas casillas quedan vacias
for i in range(7):
    if i != 3:
        assert tabla.casillas[i].tamano == 0

# Resultado Caso 3
print("Longitud de la casilla 3:", tabla.casillas[3].tamano)
print("Factor de carga:", tabla.factor_carga())

# Caso 4: colecciones aleatorias, la lista y la tabla deben responder igual.
random.seed(42)
ESTADOS = ["en bodega", "en reparto", "entregado", "devuelto"]
COLECCIONES = 20

for _ in range(COLECCIONES):
    n = random.randint(1, 500)
    m = random.randint(1, 100)

    # Se toman 2n guias distintas de cuatro digitos: las primeras n se
    # insertan y las otras n se usan como guias inexistentes.
    muestra = random.sample(range(1000, 10000), 2 * n)
    existentes = muestra[:n]
    inexistentes = muestra[n:]

    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in existentes:
        estado = random.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia in existentes:
        assert lista.buscar(guia) is not None
        assert lista.buscar(guia) == tabla.buscar(guia)

    for guia in inexistentes:
        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None

    assert lista.tamano == tabla.tamano == n
    assert tabla.factor_carga() == n / m

# Resultado Caso 4
print("Colecciones aleatorias verificadas:", COLECCIONES)

print("Todas las pruebas pasaron.")
