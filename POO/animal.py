class animal:
    def __init__(self, nombre):
       # print("animal, animal, tu mujer dice que soy un animal")
        self.nombre=nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre    
obj=animal("soso")
obj.setNombre(("jijiaj"))    
print(obj.getNombre())