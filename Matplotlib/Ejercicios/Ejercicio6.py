'''

    Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos de una empresa
    por meses y devuelva un diagrama de líneas con dos líneas, una para los ingresos y otra para los gastos.

    El diagrama debe tener una leyenda identificando la línea de los ingresos y la de los gastos, un título
    con el nombre “Evolución de ingresos y gastos” y el eje y debe empezar en 0.

'''
import pandas as pd
import matplotlib.pyplot as plt

def mostrar(df):

    #asinacion
    fig, ax = plt.subplots()
    ax.plot(df['Meses'],  df['Ingresos'], label='Ingresos')#linea de ingresos
    ax.plot(df['Meses'],  df['Gastos'], label='Gastos')#linea de gastos

    ax.set_ylim(0)  # Esto establece los límites visuales del eje y comenzando en cero y hasta donde quiera

    #etiquetas
    plt.xlabel("Meses")
    plt.ylabel("Evolucion")
    plt.title("Evolución de ingresos y gastos")

    plt.legend()#toma por defecto los mensajes dispuestos en cada linea

    #visualizacion
    plt.xticks(rotation=25)#rotar el texto 25 grados, mejor visualizacion
    plt.show()


datos = pd.read_csv("../Archivos/IngresosyGastos.csv")
df = pd.DataFrame(datos)
print(df)

mostrar(df)