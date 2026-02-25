class zoo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.listasGatos=[]
    def addFelino(self,gato):
        self.listasGatos.append(gato)    
    def verGatos(self):
        return self.listaGatos    