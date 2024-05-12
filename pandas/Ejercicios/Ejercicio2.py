'''

    Escribir una función que reciba un diccionario con las notas de los alumno de un curso
    y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

'''
import pandas as pd


def curso(diccionario):

    serie = pd.Series(diccionario)
    datos = {"minima":round(serie.min(), 2) , "maxima":round(serie.max(), 2), "media": round(serie.mean(), 2),"desviacion Estandar":serie.std()}
    serie = pd.Series(datos)
    print(serie)



curso({"jose":2.3, "vartolomeo" :4.5 , "Juan": 3.3, "casimiro":3.5, "sofia":4.7})