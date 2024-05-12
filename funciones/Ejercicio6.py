'''

    Escribir una función que reciba una muestra de números en una lista y devuelva su media.


'''
def media (muestra):

    suma= 0
    for numero in muestra:
        suma += numero

    media = suma/len(muestra)
    return media

print(media([2,3,3,5,7,10]))
print(media([1, 2, 3, 4, 5]))