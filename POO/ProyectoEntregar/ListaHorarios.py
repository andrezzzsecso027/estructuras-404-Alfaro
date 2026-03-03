
class NodoHorario:
    def __init__(self, hora):
        self.hora = hora
        self.siguiente = None

class ListaHorarios:
    def __init__(self):
        self.cabeza = None
        self.cantidad = 0

    def agregar_horario(self, hora):
        nuevo_nodo = NodoHorario(hora)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.cantidad += 1

    def mostrar_horarios(self):
        if self.cabeza is None:
            print("No hay horarios disponibles")
            return False

        print("\nHorarios Disponibles:")
        print("-" * 40)
        actual = self.cabeza
        numero = 1

        while actual is not None:
            print(f"{numero}. {actual.hora}:00 hrs")
            actual = actual.siguiente
            numero += 1
        print("-" * 40)
        return True

    def seleccionar_horario(self, numero):
        if self.cabeza is None:
            return None
        if numero == 1:
            hora_seleccionada = self.cabeza.hora
            self.cabeza = self.cabeza.siguiente
            self.cantidad -= 1
            return hora_seleccionada

        actual = self.cabeza
        posicion = 1

        while actual.siguiente is not None and posicion < numero - 1:
            actual = actual.siguiente
            posicion += 1

        if actual.siguiente is None:
            return None

        hora_seleccionada = actual.siguiente.hora
        actual.siguiente = actual.siguiente.siguiente
        self.cantidad -= 1
        return hora_seleccionada

    def esta_vacia(self):
        return self.cabeza is None

