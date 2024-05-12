'''
    El fichero bancos.csv contiene las cotizaciones de los principales bancos de España
    con : Empresa (nombre de la empresa), Apertura (precio de la acción a la apertura de bolsa),
    Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada),
    Cierre (precio de la acción al cierre de bolsa), Volumen (volumen al cierre de bolsa).

    Construir una función reciba el fichero bancos.csv y cree un diagrama de líneas con las series temporales
    de las cotizaciones de cierre de cada banco.

    ------
    -Sacar la informacion de la columna cierre
    - Eje y  : numeros
    - Eje x  : Bancos


'''
import matplotlib.pyplot as plt
import pandas as pd


def graficar(fichero):

    df = pd.DataFrame(fichero)
    informacion = df[['Empresa', 'Cierre']].set_index('Empresa')
    print(informacion)

    informacion.plot(kind='line')# se especifica que el grafico sera de lineas

    #Mensajes
    plt.title("Cierre de bolsa")
    plt.ylabel("Cierre")


    #visualizacion
    plt.xticks(rotation=20)  # rotar el texto 25 grados, mejor visualizacion
    plt.grid()
    plt.show()
    print(cierres)



fichero = pd.read_csv("../Archivos/bancos.csv")
graficar(fichero)
