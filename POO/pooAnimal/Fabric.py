from Felinaaa import felinaaa
class Fabric:
    def __init__(self,nombre):
        self.nombre=nombre
        self.listaPeluches=list()
    def makeToy(self,especie):
        f=felinaaa("gatos",especie)
        self.listaPeluches.append(f)
    def verCatalogo(self):
        return self.listaPeluches