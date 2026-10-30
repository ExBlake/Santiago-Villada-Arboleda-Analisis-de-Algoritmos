class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.derecho = None
        self.izquierdo = None
        self.padre = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = Nodo(8)
        self.raiz.izquierdo = Nodo(3)
        self.raiz.izquierdo.padre = self.raiz
        self.raiz.derecho = Nodo(10)
        self.raiz.derecho.padre = self.raiz
        self.raiz.izquierdo.izquierdo = Nodo(1)
        self.raiz.izquierdo.izquierdo.padre = self.raiz.izquierdo
        self.raiz.izquierdo.derecho = Nodo(6)
        self.raiz.izquierdo.derecho.padre = self.raiz.izquierdo
        self.raiz.derecho.derecho = Nodo(14)
        self.raiz.derecho.derecho.padre = self.raiz.derecho
        # self.inorder(self.raiz)
        # self.nodo_encontrado = self.buscar(6)
        # self.minimo_dato = self.minimo(self.raiz).dato
        self.insertar(9)
        print()

    def inorder(self, nodo):
        if nodo is None:
            return
        # Caso recursivo
        self.inorder(nodo.izquierdo)
        print(nodo.dato)
        self.inorder(nodo.derecho)

    def buscar(self, dato):
        nodo_actual = self.raiz
        while nodo_actual is not None and nodo_actual.dato != dato:
            if dato < nodo_actual.dato:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        return nodo_actual

    def minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        padre_actual = None
        nodo_actual = self.raiz

        while nodo_actual is not None:
            padre_actual = nodo_actual
            if dato < nodo_actual.dato:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        nuevo_nodo.padre = padre_actual

        if padre_actual is None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.dato < padre_actual.dato:
            padre_actual.izquierdo = nuevo_nodo
        else:
            padre_actual.derecho = nuevo_nodo

        # self.inorder(self.raiz)

    def transplantar(self, u, v):
        """
        Reemplaza el subarbol con raiz u por el subarbol con raiz v
        """
        if u.padre is None:
            self.raiz = v
        elif u == u.padre.izquierdo:
            u.padre.izquierdo = v
        elif u == u.padre.derecho:
            u.padre.derecho = v

        if v is not None:
            v.padre = u.padre

    def eliminar(self, dato):
        "Complejidad: O(h)"
        nodo_a_eliminar = self.buscar(dato)
        # Caso 1: Si no se encuentra el elemento que se quiere eliminar
        if nodo_a_eliminar is None:
            return
        # Caso 2: Si el elemento que se quiere eliminar solo tiene un nodo hijo a la izquierda
        if nodo_a_eliminar.izquierdo is None:
            self.transplantar(nodo_a_eliminar, nodo_a_eliminar.derecho)
        # Caso 3: Si el elemento que se quiere eliminar solo tiene un nodo hijo a la derecha
        elif nodo_a_eliminar.derecho is None:
            self.transplantar(nodo_a_eliminar, nodo_a_eliminar.izquierdo)
        # Caso 4: Si el elemento a eliminar tiene dos hijos
        else:
            nodo_minimo_derecho = self.minimo(nodo_a_eliminar.derecho)
            # En caso de que el nodo a eliminar tenga mas de un subnivel
            if nodo_minimo_derecho.padre != nodo_a_eliminar:
                self.transplantar(nodo_minimo_derecho, nodo_minimo_derecho.derecho)
                nodo_minimo_derecho.derecho = nodo_a_eliminar.derecho
                nodo_minimo_derecho.derecho.padre = nodo_minimo_derecho
            self.transplantar(nodo_a_eliminar, nodo_minimo_derecho)
            nodo_minimo_derecho.izquierdo = nodo_a_eliminar.izquierdo
            nodo_minimo_derecho.izquierdo.padre = nodo_minimo_derecho
        self.inorder(self.raiz)

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
