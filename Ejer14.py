#Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
#se puede convertir el número a cadena.

def SumaDigitos(n,suma):
    suma = n%10 + suma 
    if (n // 10 == 0):
        print("la suma de los digitos del numero es --> ",suma)
    else:
        return SumaDigitos(n//10,suma)

print(SumaDigitos(88,0))  
          
