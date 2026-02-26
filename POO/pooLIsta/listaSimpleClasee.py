class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista:
    def __init__(self):
        self.primero = None

    def adicionar(self, dato):
        nuevo = Nodo(dato)
        if self.primero == None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def eliminar(self):
        if self.primero is None:
            print("La lista está vacía")
            return

        dato = int(input("Ingrese el número a eliminar: "))


        # Caso 2: el dato está en el primer nodo
        if self.primero.dato == dato:
            self.primero = self.primero.siguiente
            print("Dato eliminado")
            return

        # Caso 3: el dato está en un nodo intermedio o final
        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                print("Dato eliminado")
                return
            actual = actual.siguiente

        print("El dato no se encontró en la lista")


listado = Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.mostrar()
listado.eliminar()
print("Lista modificada:")
listado.mostrar()