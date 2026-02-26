def cuentaRegresiva(numero):
    print(numero)
    if numero>0:
        numero-=1
        cuentaRegresiva(numero)
    else:
        return 0    
cuentaRegresiva(abs(int(input("ingrese un numero positivo: "))))
def sumar(a,b):
    return sumar(a+b)
print(sumar(3,4))