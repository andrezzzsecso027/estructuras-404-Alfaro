class Proveedor:
    def __init__(self, nombre, ubicacion, capacidad_kg):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_kg = capacidad_kg
        self.disponible = True
        self.total_suministrado = 0

    def __str__(self):
        estado = " Disponible" if self.disponible else " No disponible"
        return f"{self.nombre} ({self.ubicacion}) - Cap: {self.capacidad_kg}kg - {estado}"
    