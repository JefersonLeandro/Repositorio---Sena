'''

    Escribir una función que reciba una muestra de números
    en una lista y devuelva otra lista con sus cuadrados.

'''

def cuadrados(lista):
    listaElevada = []
    for n in lista:
        valor = n*n
        listaElevada.append(valor)
    return listaElevada

print(cuadrados([1,2,3,4]))
print(cuadrados([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


