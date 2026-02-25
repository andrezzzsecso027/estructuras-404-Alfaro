from animal import animal
from Felinaaa import felinaaa
from ZOO import zoo
from Fabric import Fabric
#ob=Animal("Pantera")
#ob1=Animal("Gato")
#ob1.setNombre("Lince")
#print(ob1.getNombre())
gato1=felinaaa("Felino","Leon")
gato2=felinaaa("Felino","Tigre")
z1=zoo("udec")
z1.addFelino(gato1)
z1.addFelino(gato2)
#print(z1.verGatos())
for ob in z1.verGatos():
    print(ob.getEspecie())

del z1
print(type(gato1))

zz=Fabric("minitoy")
zz.makeToy("puma")
zz.makeToy("lince")
zz.makeToy("jaguar")

for peluche in zz.verCatalogo():
    print(peluche.getEspecie())

