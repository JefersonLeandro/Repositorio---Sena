'''

    Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno
    y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones
    correspondientes a las notas.


'''


def promediar(diccionario):
    suma = 0
    asignaturas = {}
    for clave , valor in diccionario.items():
        print(valor)
        suma = sum(valor)
        tamano = len(valor)
        promedio = suma / tamano
        asignaturas[clave.upper()] = promedio

    return asignaturas



print(promediar({"matematicas" : [3.4, 4.5 , 2.5 , 1.7] , "naturales" : [3.0, 3.5 , 2.8 , 2.7] , "ingles" : [1.4, 4.5 , 2.0 , 3.6]}))

