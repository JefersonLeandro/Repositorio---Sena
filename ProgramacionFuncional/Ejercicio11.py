'''


    Escribir una función que reciba una muestra de números y devuelva los valores atípicos,

    es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3.

    Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por
    la desviación típica de la muestra.


'''

import math
from statistics import stdev
def valoresAtipicos(muestra):

    tamano = len(muestra)
    mediaAritmetica = sum(muestra)/tamano

  # desviacionEstandar =  math.sqrt(sum(list(map( lambda muestra : (muestra-mediaAritmetica)**2 ,muestra)))/tamano) tambien sirve sino que el metodo stdev es mas preciso
    desviacionEstandar = stdev(muestra)

    puntuacionesTipicas = list(map( lambda muestra : (muestra-mediaAritmetica) / desviacionEstandar ,muestra))

    datosAtipicos = []
    for valor1 , valor2 in zip(muestra , puntuacionesTipicas): # el metodo zip es para recibir dos listas
            if valor2 > 3 or valor2 < -3:
                datosAtipicos.append(valor1)

    return f"DATOS  : {datosAtipicos}"


print(valoresAtipicos([1,2,3,4,5]))
print(valoresAtipicos([6,2,3,1]))
print(valoresAtipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
print(valoresAtipicos([88 , 120 , 300 , 500 , 1]))

'''

metodos para sacar la media y desviacion estandar de manera perezosa pero funcional se ahorra bastante codigo 
mean()  -> mediaAritmetica
stdev() -> desviacionEstandar 

'''