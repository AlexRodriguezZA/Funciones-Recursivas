#Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
#matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
#y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
#avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.
matriz = [[1, 1, 1, 1, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 10]]


def SalirLaberinto(laberinto,x,y):
    if (x>=0 and x<=len(laberinto)-1) and (y>=0 and y<=len(laberinto[0])-1):
        if (laberinto[x][y] == 10):
            print("saliste del laberinto")
        elif (laberinto[x][y] == 1):
            laberinto[x][y] = 2
            SalirLaberinto(laberinto,x,y+1)
            SalirLaberinto(laberinto,x,y-1)
            SalirLaberinto(laberinto,x-1,y)
            SalirLaberinto(laberinto,x+1,y)
            laberinto = 1

print(SalirLaberinto(matriz,0,0))

