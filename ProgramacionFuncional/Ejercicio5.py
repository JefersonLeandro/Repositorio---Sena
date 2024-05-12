'''

    Escribir una función que reciba una frase y devuelva un diccionario
    con las palabras que contiene y su longitud.

'''

def desglozar(frase):

    diccionario = {}
    for palabra in frase.split():
        logitud = len(palabra)
        diccionario[palabra] = logitud

    return diccionario



print(desglozar("la vida es llevadera como un bimbam"))