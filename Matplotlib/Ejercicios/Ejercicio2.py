'''
    Escribir una función que reciba una diccionario con las notas de las asignaturas
    de un curso y una cadena con el nombre de un color y devuelva un diagrama de barras
    de las notas en el color dado.

'''

import matplotlib.pyplot as plt
import pandas as pd

def notas(diccionario, cadena):

    fig , ax = plt.subplots()

    df = pd.DataFrame(diccionario)
    promedios = df.mean()

    ax.bar(diccionario.keys(), promedios, color=cadena)
    plt.title("Curso")
    plt.xlabel("asignaturas")
    plt.ylabel("notas")
    plt.show()



print(notas({'matematicas':[3.4,4.5,3.4,2.5], 'Ingles':[3.0,2.3,4.5,3.9], 'Economia':[4.0,3.0,2,1],
      'Quimica':[3.5, 3.7, 4.0, 2.9]}, 'black'))