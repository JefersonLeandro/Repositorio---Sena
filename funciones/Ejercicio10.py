'''

    Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.



'''


def convertirBinario(numero):

    binario = bin(numero)
    #con format
    # binario = "{0:b}".format(numero)
    return binario




def convertirEntero(binario):

    numero = int(binario , 2)
    return numero


print(convertirBinario(23))
print(convertirEntero("0b10111"))