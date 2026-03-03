from Persona import Persona


class Usuario(Persona):
    def __init__(self, nombre, cedula, hora_turno, tramite="General"):
        super().__init__(nombre, cedula)
        self.hora_turno = hora_turno
        self.tramite = tramite
        self.atendido = False

    def __str__(self):
        estado = "Atendido" if self.atendido else "Pendiente"
        return f"{super().__str__()} | Turno: {self.hora_turno}:00 hrs | Trámite: {self.tramite} | {estado}"