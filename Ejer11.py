#Desarrollar un algoritmo que invierta un número entero.

def InvertirNumero(n,numeroInvertido):
    numeroInvertido = str(numeroInvertido) + str(n%10) 
    if (n // 10 == 0):
        print("El numero invertido es --> ", numeroInvertido)
    else:
        return InvertirNumero(n//10,numeroInvertido)

print(InvertirNumero(678,""))

def invertir_numero(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)

print(invertir_numero(34))
