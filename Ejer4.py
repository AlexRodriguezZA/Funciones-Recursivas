#Implementar una función para calcular la potencia dado dos números enteros, el primero re-
#presenta la base y segundo el exponente.
def potenciaRecursiva(base,exponente):
    if (base == 0):
        return 0
    elif (exponente == 0):
        return 1
    else:
        return base * potenciaRecursiva(base,exponente-1)

print (potenciaRecursiva(0,3))