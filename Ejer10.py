#Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def CuentaDigitos(n,cantidad):
    cantidad += 1
    if(n // 10 == 0):
        print("La cantidad de digitos que tiene es de --> ", cantidad)
    else:
        return CuentaDigitos(n//10,cantidad)

print(CuentaDigitos(2345,0))