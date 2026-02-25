def cuentaRegresiva(numero):
    print(numero)
    if numero>0:
        numero-=1
        cuentaRegresiva(numero)
    else:
        return 0    
cuentaRegresiva(abs(int(input("ingrese un numero positivo: "))))
def calcularFactorial(numero):
    if numero>0:
        numero=numero*calcularFactorial(numero-1)
        print(numero)    
    else:
        print("bruto ignorante")    

calcularFactorial(int(input("escriba un numero")))