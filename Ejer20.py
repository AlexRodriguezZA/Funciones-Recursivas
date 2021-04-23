#Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
#manera recursiva, y permita determinar si un valor dado está o no en dicha lista.

vector = [1,2,3,4]

def BusquedaSecuencial(lista,numeroBuscado,i):
    if (i<=len(lista)-1):
        if ((numeroBuscado==lista[i])):
            print("El número si esta la lista")
        else:
            return BusquedaSecuencial(lista,numeroBuscado,i+1)
    else:
        print("El numero no está en la lista")

print(BusquedaSecuencial(vector,3,0))
