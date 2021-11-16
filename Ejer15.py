#Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
#Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
#el número a calcular su raíz.

def raizcuadrada(n1, n2):
    if((n1 * n1) <= n2):
        return n1
    else:
        return raizcuadrada(n1-1, n2)


def raiz(n):
    if n == 0:
        return n
    else:
        return raizcuadrada(n, n)

print(raiz(2))