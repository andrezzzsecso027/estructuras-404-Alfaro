
class PuntoDistribucion:
    def __init__(self, nombre, direccion, demanda_semanal):
        self.nombre = nombre
        self.direccion = direccion
        self.demanda_semanal = demanda_semanal
        self.inventario_actual = 0
        self.ultima_entrega = None

    def __str__(self):
        return f"{self.nombre} ({self.direccion}) - Demanda: {self.demanda_semanal}kg/sem"
