#Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def VectorAlRevez(lista,i):
    print(lista[i])
    if (i <= 0):
        print("Llegaste al final de la lista")
    else:
        return VectorAlRevez(lista,i-1)

vector = [1,2,3,4,5]

print(vector)
print(VectorAlRevez(vector,len(vector)-1))