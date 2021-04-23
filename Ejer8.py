#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
#4/2 = 2 --> 2/2 = {1} ---->100
#% --> {0}    % --> {0}------^^
#       ----------------------^   
def DecimalBinario(numero):
    if (numero == 1):
        return 1
    elif (numero == 0):
        return 0
    else:
        return str(DecimalBinario(numero//2)) + str(numero%2)
        
print(DecimalBinario(5))
