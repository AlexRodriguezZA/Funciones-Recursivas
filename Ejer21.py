#Dada una lista de valores ordenadas, desarrollar un algoritmo que modifique el método de búsqueda binaria para que funcione 
# de forma recursiva.

array = [1,2,3,4,5,6,7,8,9,10]

def binariaRecursiva(lista,NumeroBuscado):
    inicio = 0
    final = len(lista)-1
    medio = (inicio+final)//2
    if (NumeroBuscado == lista[medio]):
        return print("El numero está en el array, en la posicion N°", medio)

print(binariaRecursiva(array,5))
    
 