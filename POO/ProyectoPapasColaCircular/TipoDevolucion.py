class TipoDevolucion:
    def __init__(self, tipo, proceso_resolucion):
        self.tipo = tipo
        self.proceso = proceso_resolucion
        self.cantidad_registrada = 0

    def __str__(self):
        return f"{self.tipo} - Casos: {self.cantidad_registrada}"
