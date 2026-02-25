from animal import animal

class felinaaa(animal):
    def __init__(self, nombre,especie):
        super().__init__(nombre)
        self.especie=especie
    def getEspecie(self):
        return self.especie
    def setEspecie(self,especie):
        self.especie=especie
        