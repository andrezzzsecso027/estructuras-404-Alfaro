class Nodo:
    def __init__(self, dato):
        self.dato = dato      # Información del nodo
        self.next = None      # Referencia al siguiente nodo

class ListaSimple:
    def __init__(self):
        self.head = None  # Primer nodo de la lista

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo

    def mostrar(self):
        actual = self.head
        while actual is not None:
            print(actual.dato)
            actual = actual.next

lista = ListaSimple()

lista.insertar("Turno 1")
lista.insertar("Turno 2")
lista.insertar("Turno 3")

lista.mostrar()
