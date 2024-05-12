'''
    Escribir una función que reciba una serie de Pandas con las notas de los alumnos de un curso
    y devuelva un diagrama de cajas con las notas.

    El diagrama debe tener el título “Distribución de notas”.

'''
import matplotlib.pyplot as plt
import pandas as pd

data = [3.4,4.5,3.4,2.5,3.0,2.3,4.5,3.9,4.0,3.0,2,1,3.5,3.7,4.0,2.9]
serie  = pd.Series(data)

def graficar(serie):
    fig, ax  = plt.subplots()
    ax.boxplot(serie)
    plt.title("Distribucion de notas")
    plt.show()

graficar(serie)


