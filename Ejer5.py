#Desarrollar una función que permita convertir un número romano en un número decimal.

def RomanosDecimal(romano,i):
    NumerosRomanos = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
    numeroEntero = 0
    if (i==len(romano) ):
        return numeroEntero 
    else:
        return numeroEntero + NumerosRomanos[romano[i]] + RomanosDecimal(romano,i+1)



print(RomanosDecimal('xvx',0))

