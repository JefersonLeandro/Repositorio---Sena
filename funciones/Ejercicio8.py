'''
    Escribir una función que reciba una muestra de números en una lista
    y devuelva un diccionario con su media, varianza y desviación típica.

    media - promedio
    varianza - dispersion de los resultados o la muestra
    desviacion tipica - variacion de un punto a otro
'''
import math
def mvd(lista):

    #media
    suma = sum(lista)
    tamano = len(lista)
    media = suma/tamano

    # varianza
    resultantes = []
    for x in lista:
        aux = (x - media)**2
        resultantes.append(aux)

    varianza = (sum(resultantes))/(tamano-1) # se hace con -1 ya que es conjunto de resultados como muestra si fuera una poblacion seria solo el tamano
    desviacionTipica = math.sqrt(varianza)

    diccionario = {"media" : media , "varianza" : round(varianza,3) , "desviacionTipica" : round(desviacionTipica,3)}


    return diccionario

print(mvd([1, 2, 3, 4, 5]))
print(mvd([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))




