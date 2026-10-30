"""Medicion de tiempos de busqueda: lista enlazada contra tabla hash.

Experimento A: mide el tiempo medio de buscar guias que no existen en
la lista y en la tabla (con alfa cercano a 2) para varios valores de n.
Experimento B: con n fijo, mide el tiempo medio de busqueda en la tabla
para varios factores de carga.

Las guias se generan con semilla fija para poder repetir la medicion.
Solo se cronometran las busquedas, con time.perf_counter(). Imprime las
tablas de tiempos y genera graficas/lista_vs_tabla.png y
graficas/tiempo_vs_alfa.png con los datos de esa misma corrida.
"""

import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

BUSQUEDAS = 200
REPETICIONES = 30
MUESTRA_VERIFICACION = 100
ESTADOS = ["en bodega", "en reparto", "entregado", "devuelto"]


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias(n: int, semilla: int = 42) -> tuple[list[int], list[str]]:
    """Genera n guias distintas de diez digitos, cada una con un estado.

    Args:
        n: cantidad de guias que se van a generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una tupla con la lista de guias y la lista de sus estados.
    """
    azar = random.Random(semilla)
    # sample no repite valores, asi las guias quedan distintas
    guias = azar.sample(range(10**9, 10**10), n)
    estados = [azar.choice(ESTADOS) for _ in range(n)]
    return guias, estados


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo probando divisores hasta su raiz.

    Args:
        numero: entero que se quiere revisar.

    Returns:
        True si el numero es primo, False si no.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(numero: float) -> int:
    """Busca el primer primo mayor o igual a un numero.

    Args:
        numero: valor desde el que se empieza a buscar.

    Returns:
        El primo mas pequeno que es mayor o igual a `numero`.
    """
    candidato = max(2, round(numero))
    while not es_primo(candidato):
        candidato += 1
    return candidato


def construir_lista(guias: list[int], estados: list[str]) -> ListaEnlazada:
    """Crea una lista enlazada con las guias dadas.

    Args:
        guias: numeros de guia que se van a insertar.
        estados: estado de cada guia, en el mismo orden.

    Returns:
        La lista con todas las guias insertadas.
    """
    lista = ListaEnlazada()
    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)
    return lista


def construir_tabla(
    guias: list[int], estados: list[str], m: int
) -> TablaHash:
    """Crea una tabla hash de m casillas con las guias dadas.

    Args:
        guias: numeros de guia que se van a insertar.
        estados: estado de cada guia, en el mismo orden.
        m: numero de casillas de la tabla.

    Returns:
        La tabla con todas las guias insertadas.
    """
    tabla = TablaHash(m)
    for guia, estado in zip(guias, estados):
        tabla.insertar(guia, estado)
    return tabla


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash, guias_buscar: list[int]
) -> float:
    """Mide el tiempo medio por busqueda en una estructura.

    Cada ronda busca todas las guias de `guias_buscar`. Se hacen varias
    rondas y se promedian, porque una sola busqueda en la tabla dura tan
    poco que el ruido del computador pesa mucho.

    Args:
        estructura: lista enlazada o tabla hash donde se busca.
        guias_buscar: guias que se van a buscar.

    Returns:
        El tiempo medio de una busqueda, en segundos.
    """
    mediciones = []
    for _ in range(REPETICIONES):
        inicio_reloj = time.perf_counter()
        for guia in guias_buscar:
            estructura.buscar(guia)
        fin_reloj = time.perf_counter()
        mediciones.append((fin_reloj - inicio_reloj) / len(guias_buscar))
    return sum(mediciones) / REPETICIONES


def verificar_estructuras(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
    estados: list[str],
    inexistentes: list[int],
) -> None:
    """Revisa que la lista y la tabla respondan lo mismo.

    Toma una muestra de guias existentes y revisa que ambas devuelvan el
    estado correcto. Tambien revisa que las guias inexistentes den None.

    Args:
        lista: lista enlazada con las guias.
        tabla: tabla hash con las mismas guias.
        guias: guias insertadas en ambas estructuras.
        estados: estado de cada guia, en el mismo orden.
        inexistentes: guias que no estan en las estructuras.
    """
    azar = random.Random(1)
    cantidad = min(MUESTRA_VERIFICACION, len(guias))
    for i in azar.sample(range(len(guias)), cantidad):
        assert lista.buscar(guias[i]) == estados[i]
        assert tabla.buscar(guias[i]) == estados[i]
    for guia in inexistentes:
        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None


def guardar_grafica(nombre: str) -> None:
    """Guarda la grafica actual en la carpeta graficas.

    Args:
        nombre: nombre del archivo png.
    """
    carpeta = os.path.dirname(os.path.abspath(__file__))
    carpeta_graficas = os.path.join(carpeta, "graficas")
    os.makedirs(carpeta_graficas, exist_ok=True)
    plt.savefig(os.path.join(carpeta_graficas, nombre))
    plt.close()


def graficar_lista_vs_tabla(
    tamanios: list[int],
    tiempos_lista: list[float],
    tiempos_tabla: list[float],
) -> None:
    """Grafica el tiempo medio por busqueda de ambas estructuras contra n.

    Args:
        tamanios: valores de n medidos.
        tiempos_lista: tiempos medios de la lista, en segundos.
        tiempos_tabla: tiempos medios de la tabla, en segundos.
    """
    # Se pasa a microsegundos para que los numeros del eje se lean mejor
    lista_us = [t * 1e6 for t in tiempos_lista]
    tabla_us = [t * 1e6 for t in tiempos_tabla]

    plt.figure()
    plt.plot(tamanios, lista_us, marker="o", label="Lista enlazada")
    plt.plot(tamanios, tabla_us, marker="o",
             label="Tabla hash (α ≈ 2)")
    plt.title("Búsqueda de guías inexistentes: lista vs tabla hash")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.legend()
    plt.grid(True)
    guardar_grafica("lista_vs_tabla.png")


def graficar_tiempo_vs_alfa(
    alfas: list[float], tiempos: list[float], n: int
) -> None:
    """Grafica el tiempo medio por busqueda en la tabla contra alfa.

    Args:
        alfas: factores de carga medidos.
        tiempos: tiempos medios de la tabla, en segundos.
        n: numero de guias que tenia la tabla.
    """
    tiempos_us = [t * 1e6 for t in tiempos]

    plt.figure()
    plt.plot(alfas, tiempos_us, marker="o",
             label=f"Tabla hash (n = {n})")
    plt.title("Efecto del factor de carga en la búsqueda")
    plt.xlabel("Factor de carga (α = n / m, guías por casilla)")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.legend()
    plt.grid(True)
    guardar_grafica("tiempo_vs_alfa.png")


def experimento_a() -> None:
    """Mide lista contra tabla para varios n e imprime los resultados."""
    tamanios = [100, 500, 1000, 5000, 10000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    print("Experimento A: lista enlazada contra tabla hash")
    print(f"{BUSQUEDAS} busquedas de guias inexistentes por cada n")
    print("     n |      m |    α | Lista (µs) | Tabla (µs)")

    for n in tamanios:
        guias, estados = generar_guias(n)
        inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
        m = primo_cercano(n / 2)

        # Las dos estructuras se construyen con las mismas guias
        lista = construir_lista(guias, estados)
        tabla = construir_tabla(guias, estados, m)
        verificar_estructuras(lista, tabla, guias, estados, inexistentes)

        tiempos_lista.append(medir_busquedas(lista, inexistentes))
        tiempos_tabla.append(medir_busquedas(tabla, inexistentes))

        print(
            f"{n:6} | {m:6} | {tabla.factor_carga():4.2f} | "
            f"{tiempos_lista[-1] * 1e6:10.3f} | "
            f"{tiempos_tabla[-1] * 1e6:10.3f}"
        )

    print("La lista y la tabla devolvieron lo mismo en todos los n")
    graficar_lista_vs_tabla(tamanios, tiempos_lista, tiempos_tabla)


def experimento_b() -> None:
    """Mide la tabla con n fijo y varios alfa e imprime los resultados."""
    n = 20000
    alfas_buscados = [0.25, 0.5, 1, 2, 4, 6, 8, 10]
    alfas = []
    tiempos = []

    guias, estados = generar_guias(n)
    inexistentes = generar_guias_inexistentes(set(guias), BUSQUEDAS)
    lista = construir_lista(guias, estados)

    print(f"\nExperimento B: efecto del factor de carga (n = {n})")
    print("     m |     α | Tabla (µs)")

    for alfa in alfas_buscados:
        # Si alfa = n / m, entonces m = n / alfa (y se busca un primo)
        m = primo_cercano(n / alfa)
        tabla = construir_tabla(guias, estados, m)
        verificar_estructuras(lista, tabla, guias, estados, inexistentes)

        # Se usa el alfa real, porque m primo no da el alfa exacto
        alfas.append(tabla.factor_carga())
        tiempos.append(medir_busquedas(tabla, inexistentes))

        print(f"{m:6} | {alfas[-1]:5.2f} | {tiempos[-1] * 1e6:10.3f}")

    graficar_tiempo_vs_alfa(alfas, tiempos, n)


if __name__ == "__main__":
    experimento_a()
    experimento_b()
