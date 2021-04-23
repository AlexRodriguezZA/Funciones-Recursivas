#Implementar una función que calcule la suma de todos los números enteros comprendidos 
# entre cero y un número entero positivo dado.
def sumaNumeros(n):
    if (n==0):   #Caso base
        return n
    else:
        return n + sumaNumeros(n-1) #llamada recursiva

print(sumaNumeros(5))