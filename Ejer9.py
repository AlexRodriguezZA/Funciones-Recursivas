def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)
    

print(logaritmo(3,4))