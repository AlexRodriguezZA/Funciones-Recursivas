#Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
#de dos número entero.

#MCD de [247 y 221] --> 13 --> MCM 247*221//13 == [4199]

def EuclidesMCM(numero1,numero2,multiplicacion):

    if numero1>numero2:
        if (numero1 % numero2 == 0):
            print("El MCM es -->  ", multiplicacion//numero2)
        else:
            return EuclidesMCM(numero1,numero1%numero2,multiplicacion)

n1 = 247
n2 = 221
print(EuclidesMCM(n1,n2,n1*n2))



