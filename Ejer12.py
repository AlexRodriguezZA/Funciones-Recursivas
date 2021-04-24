#Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
#números enteros

#24 % 16 ---> [8] --> 16 % 8 --> [0]

def EuclidesMCD(numero1,numero2):
    if numero1>numero2:

        if (numero1 % numero2 == 0):
             print("El MCD es -->  ", numero2)
        else:
            return EuclidesMCD(numero1,numero1%numero2)


print(EuclidesMCD(247,221))
