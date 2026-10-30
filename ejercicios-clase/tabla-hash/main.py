import math
import random

class TablaDireccionamientoDirecto:
    """
    Implementa un conjunto dinamico usando un arreglo indexado directamente por la clave
    """
    def __init__(self, m, opcion_funcion_hash): 
        self.m = m
        self.tabla = [None] * m 
        self.familia_universal_hash = FamiliaUniversalHash(139, m)
        self.n = 0
        self.opcion_funcion_hash = opcion_funcion_hash
        
    def insertar (self, key, value):
        """
        Complejidad: 0(1)
        Opcion 1 = Metodo de la division
        Opcion 2 = Metodo de la multiplicacion
        Opcion 3 = Metodo de la familia de funciones hash
        """
        h_key = self.casteo_de_la_llave(key)
        nuevo_nodo = Nodo(key, value)
        nuevo_nodo.siguiente = self.tabla[h_key]
        self.tabla[h_key] = nuevo_nodo
        self.n += 1
        return h_key

    def casteo_de_la_llave(self, key):
        """
        Complejidad: O(1)
        """
        if self.opcion_funcion_hash == 1:
            h_key = self.division_hash(key)
        elif self.opcion_funcion_hash == 2:
            h_key = self.multiplicacion_hash(key)
        else:
            h_key = self.familia_universal_hash.hash(key)
        return h_key

    def buscar(self, key):
        "Complejidad: O(1 + factor de carga)"
        h_key = self.casteo_de_la_llave(key)
        actual = self.tabla[h_key] #Cabeza de la lista en ese slot
        while actual is not None:
            if actual.llave == key:
                return actual.valor
            actual = actual.siguiente
        return None

    def eliminar(self, key):
        "Complejidad: 0(1)"
        h_key = self.casteo_de_la_llave(key)
        actual = self.tabla[h_key]
        anterior = None
        
        while actual is not None:
            if actual.llave == key:
                # Caso 1: El nodo a eliminar es la cabeza de la lista
                if anterior is None:
                    self.tabla[h_key] = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.n -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def display(self):
        """Imprime el estado interno de la tabla para depuración y trazas."""
        print(f"HashTable (m={self.m}, n={self.n}, d={self.obtener_factor_de_carga()})") 
        for i, head in enumerate(self.tabla):
            if head is not None:
                chain = []
                node = head
                while node:
                    chain.append(f" ([{node.llave}: {node.valor}])")
                    node = node.siguiente
                print(f" [{i}] → {' → '.join(chain)}")
            else:
                print(f" [{i}] → NULL")

    def division_hash(self, llave):
        """
        Complejidad: O(1)
        """
        return llave % self.m
    
    def multiplicacion_hash(self, llave, A = (math.sqrt(5) - 1) / 2):
        return int(((llave * A) % 1) * self.m)
    
    def obtener_factor_de_carga(self):
        return self.n / self.m
    
class FamiliaUniversalHash:
    """
    Implementa una familia universal de funciones hash
    """
    def __init__(self, numero_primo, tamanio_tabla):
        self.numero_primo = numero_primo
        self.tamanio_tabla = tamanio_tabla
        self.a = random.randint(1, self.numero_primo - 1)
        self.b = random.randint(0, self.numero_primo - 1)
        
        
    def hash(self, llave):
        return ((self.a * llave + self.b) % self.numero_primo) % self.tamanio_tabla

class Nodo:
    """
    Implementa un nodo para una lista enlazada
    """
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.siguiente = None
        
if __name__ == "__main__":
    # tabla_direccionamiento_directo= TablaDireccionamientoDirecto(100)
    # tabla_direccionamiento_directo.insertar (1234567, "Santiago", 3)
    # tabla_direccionamiento_directo.insertar (3556584, "Ana", 3) 
    # # tabla_direccionamiento_directo.insertar (8, "Luis")
    # # tabla_direccionamiento_directo.insertar (8, "Andres")
    
    # # print(tabla_direccionamiento_directo.tabla)
    # # print(tabla_direccionamiento_directo.buscar(3)) 
    # # print(tabla_direccionamiento_directo.buscar (8))
    
    # # tabla_direccionamiento_directo.eliminar(2)
    # print(tabla_direccionamiento_directo.tabla)
    # # print(tabla_direccionamiento_directo.multiplicacion_hash(1234567))
    # # print(tabla_direccionamiento_directo.multiplicacion_hash(3556584))
    
    tabla_direccionamiento_directo= TablaDireccionamientoDirecto(9,1)
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    values = [
        "Santiago",
        "Ana",
        "Luis",
        "Andres",
        "Karol",
        "Maria",
        "Pedro",
        "Mateo",
        "Camilo"
    ]
    
    for i, k in enumerate(keys):
        splot = tabla_direccionamiento_directo.insertar(k, values[i])
        print(f"Insertando {k}: h({k}) = {splot}")
    
    tabla_direccionamiento_directo.display()