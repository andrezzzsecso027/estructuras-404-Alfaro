class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

a=nodo(100)
b=nodo(1000)
c=nodo(1)
d=nodo(10)
a.siguiente=b
b.siguiente=c
c.siguiente=d
d.siguiente=None

actual=a
while actual:
    print(actual.dato)
    actual=actual.siguiente