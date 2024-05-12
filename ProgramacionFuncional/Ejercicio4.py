'''

    Escribir una función que reciba otra función booleana y una lista,
    y devuelva otra lista con los elementos de la lista que devuelvan
    True al aplicarles la función booleana.

'''


def recibir(funcionBooleana, lista):

    nuevaLista = []
    for numero in lista:
        resultado = funcionBooleana(numero)
        print("resultado", resultado)
        if resultado:
            nuevaLista.append(numero)

    return nuevaLista


def es_capicua(numero):

    numeroStr = str(numero)
    verificacion = False

    print("--", numeroStr[::-1])

    if numeroStr == numeroStr[::-1]:
        verificacion = True

    return verificacion



print(recibir(es_capicua,[121, 123, 111, 00]))