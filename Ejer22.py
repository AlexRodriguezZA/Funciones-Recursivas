#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
#A. --> sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
#B. --> determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#C. --> Utilizar un vector para representar la mochila.

def UsarLaFuerza(lista,n):
    if (lista[n] == "sable"):
        return print("--> Encontraste el sable en la posición --> ",n,"Fueron necesarios sacar ",n-(n-n)," elementos anteriormente")
    elif (len(lista) == n+1):
        return print("--> Llegaste al final de la lista sin encontrar el sable") #Cuando el sable no está en la mochila
    else:
        return UsarLaFuerza(lista,n+1)

mochilaJedi=["gorro","documento","pistola","carnet","sable"]

print(UsarLaFuerza(mochilaJedi,0))
print("-La mochila contenía -->",mochilaJedi)