class CampañaMarketing:
    def __init__(self, nombre, mes, descripcion):
        self.nombre = nombre
        self.mes = mes
        self.descripcion = descripcion
        self.ejecutada = False

    def __str__(self):
        estado = " Ejecutada" if self.ejecutada else " Pendiente"
        return f"{self.nombre} ({self.mes}) - {estado}"
