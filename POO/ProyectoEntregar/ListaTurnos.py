class NodoTurno:
    def __init__(self, usuario):
        self.usuario = usuario
        self.siguiente = None
        self.anterior = None

class ListaTurnos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def agregar_turno(self, usuario):

        nuevo_nodo = NodoTurno(usuario)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

        self.cantidad += 1
        print(f"Turno agendado para {usuario.nombre} a las {usuario.hora_turno}:00 hrs")

    def mostrar_turnos_resumido(self):

        if self.cabeza is None:
            print(" No hay turnos agendados")
            return

        print("\n LISTA DE TURNOS:")
        print("-" * 50)

        actual = self.cabeza
        numero = 1

        while actual is not None:
            estado = "✅" if actual.usuario.atendido else "⏳"
            print(f"{numero}. {estado} {actual.usuario.hora_turno}:00 hrs - {actual.usuario.nombre}")
            actual = actual.siguiente
            numero += 1
        print("-" * 50)

    def obtener_primer_pendiente(self):

        actual = self.cabeza

        while actual is not None:
            if not actual.usuario.atendido:
                return actual
            actual = actual.siguiente

        return None

    def esta_vacia(self):
        return self.cabeza is None
