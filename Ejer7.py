#Desarrollar un algoritmo que permita calcular la siguiente serie: h(n) = 1 + 1/2 + 1/3 + 1/4 + 1/5 ... (1/n)

def sumaFracionaria(n):
    if (n == 1):
        return 1
    else:
        return 1/n + (1 // n + sumaFracionaria(n-1))   

print(sumaFracionaria(5))