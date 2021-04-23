# Implementar una función para calcular el producto de dos números enteros dados.
def productoRecursivo(n1,n2):
    if ((n1 == 0) or (n2 == 0)):
        return 0
    else: 
        return n1 + productoRecursivo(n1,n2-1) 

print (productoRecursivo(10,7))


