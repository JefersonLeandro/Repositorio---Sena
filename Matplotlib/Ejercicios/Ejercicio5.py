'''

    Escribir una función que reciba una serie de Pandas con el número de ventas de un producto
    por años y una cadena con el tipo de gráfico a generar (lineas, barras, sectores, areas)
    y devuelva un diagrama del tipo indicado con la evolución de las ventas por años y con
    el título “Evolución del número de ventas”.

'''
import pandas as pd
import matplotlib.pyplot as plt

def graficar(serie,grafico):

    grafico = grafico.lower()
    fig, ax = plt.subplots()

    if grafico == 'lineas':
        ax.plot(serie)
    elif grafico == 'barras':
        ax.bar(serie.keys(), serie)
    elif grafico == 'sectores':
        ax.pie(serie, labels= serie.keys(), autopct = '%1.1f%%')
    elif grafico == 'areas':
        ax.fill_between(serie.keys(), serie.values)
    else:
        print("opcion erronea")

    plt.title("Evolución del número de ventas")
    plt.show()

# barras de chocalate vendidas al año
datos = {2021: 1000, 2022: 800, 2023: 1300, 2024: 918}
serie = pd.Series(datos)
graficar(serie, 'Sectores')\

# para que sirve el metodo kind ?