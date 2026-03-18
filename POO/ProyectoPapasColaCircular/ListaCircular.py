class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cantidad = 0

    def agregar(self, dato):

        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

        self.cantidad += 1

    def mostrar(self):

        if self.cabeza is None:
            print(" La lista está vacía")
            return []

        elementos = []
        actual = self.cabeza
        cont = 0

        while cont < self.cantidad:
            elementos.append(actual.dato)
            actual = actual.siguiente
            cont += 1

        return elementos

    def obtener_actual(self):

        if self.cabeza:
            return self.cabeza.dato
        return None

    def rotar(self):

        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def esta_vacia(self):
        return self.cabeza is None