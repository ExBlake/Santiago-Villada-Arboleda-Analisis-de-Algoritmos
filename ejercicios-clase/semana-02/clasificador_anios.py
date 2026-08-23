"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    # % residuo de la division
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        try:
            mensaje = input("Ingrese años separados por comas: ")
            partes_anio = mensaje.split(",")
            anios = []
            
            for p in partes_anio:
                anios.append(int(p))
                
            return anios
        except Exception:
            print("Error: ingrese solo números enteros.")
 
def main() -> None:
    """Punto de entrada del script."""
    lista_anios = leer_anios()
    
    # Comprensión de listas
    bisiestos = []
    # for anio in lista_anios:
    #     if es_bisiesto(anio):
    #         bisiestos.append(anio)
    bisiestos = [anio for anio in lista_anios if es_bisiesto(anio)]    
    print("Años ingresados:", lista_anios)
    print("Años bisiestos:", bisiestos)
    print("Cantidad de bisiestos:", len(bisiestos))
 
 
if __name__ == "__main__":
    main()