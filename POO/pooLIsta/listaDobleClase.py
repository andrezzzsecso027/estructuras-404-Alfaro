class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class Lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def adicionar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def mostrarAdelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def mostrarAtras(self):
        actual = self.cola
        while actual:
            print(actual.dato)
            actual = actual.anterior

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                print("El número SÍ existe")
                return
            actual = actual.siguiente
        print("El número NO existe")


listado = Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.mostrarAdelante()
print("-" * 50)
listado.mostrarAtras()
while True:
    dato = input("Escribe el número que deseas buscar (o 'salir'): ")

    if dato.lower() == "salir":
        print("Programa finalizado.")
        break

    dato = int(dato)
    listado.buscar(dato)