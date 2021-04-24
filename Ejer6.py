#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def CaracteresInvertido(lista,i):
    print(lista[i])
    if (i <= (len(lista) - len(lista))):
        print("Fin de la lista")
    else:
        return CaracteresInvertido(lista,i-1)

caracteres = ["e","f","v","t"]

print(caracteres)

print(CaracteresInvertido(caracteres,len(caracteres)-1))

        