'''

    Escribir una función que reciba un diccionario con las notas de los alumnos de un curso
    y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.


'''

import pandas as pd


def curso(diccionario):

    aprobados = {}
    for nombre , nota in diccionario.items():
        if nota >= 3.5:
            aprobados[nombre] = nota

    serie = pd.Series(aprobados)
    notas = serie.sort_values(ascending=False)
    print(notas)




curso({"jose":2.3, "vartolomeo" :4.5 , "Juan": 3.3, "casimiro":3.5, "sofia":4.7})