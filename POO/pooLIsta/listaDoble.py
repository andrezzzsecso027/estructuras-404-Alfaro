class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.prev = None
class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertar(self, dato):
        nuevo = NodoDoble(dato)

        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.next = nuevo
            nuevo.prev = self.tail
            self.tail = nuevo
    def mostrar_adelante(self):
        actual = self.head
        while actual is not None:
            print(actual.dato)
            actual = actual.next
    def mostrar_atras(self):
        actual = self.tail
        while actual is not None:
            print(actual.dato)
            actual = actual.prev

lista = ListaDoble()

lista.insertar("Turno A")
lista.insertar("Turno B")
lista.insertar("Turno C")

print("Adelante:")
lista.mostrar_adelante()

print("Atrás:")
lista.mostrar_atras()