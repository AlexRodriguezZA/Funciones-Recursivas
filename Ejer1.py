#Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def Fibon(numero):
    if (numero == 1 or numero == 0):
        return numero
    else:
        return Fibon(numero-1) + Fibon(numero-2)
print(Fibon(3))
