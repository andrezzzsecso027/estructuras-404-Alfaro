class LineaProduccion:
    def __init__(self, nombre, tipo_producto, capacidad_hora):
        self.nombre = nombre
        self.tipo_producto = tipo_producto
        self.capacidad_hora = capacidad_hora
        self.ocupada = False
        self.total_producido = 0

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"{self.nombre} - {self.tipo_producto} - {self.capacidad_hora}kg/h - {estado}"