'''


    Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario
    con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.

'''


def promediar(diccionario):

    asignaturas = {}
    for clave , valor in diccionario.items():
        print(valor)
        suma = sum(valor)
        tamano = len(valor)
        promedio = suma / tamano
        if promedio >= 3.5:
            asignaturas[clave.upper()] = promedio

    return  asignaturas



print("asignaturas aprobadas")
print(promediar({"matematicas" : [3.4, 5.0 , 4.0, 2.5] , "naturales" : [5.0, 4.7 , 2.8 , 2.7] , "ingles" : [1.4, 4.5 , 2.0 , 3.6]}))

