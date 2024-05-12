'''

    Escribir una función reciba una lista de notas y devuelva
    la lista de calificaciones correspondientes a esas notas.


'''

calificaciones = []
def promediar(notas):

    sumaTotal = sum(notas)
    tamano = len(notas)
    calificacion = sumaTotal / tamano

    calificaciones.append(round(calificacion,2))
    return calificaciones

print(promediar([3.5 , 2.0, 4.0 , 4.5 , 3.1]))
print(promediar([1.0 , 2.0, 5.0 , 3.5 , 2.8]))