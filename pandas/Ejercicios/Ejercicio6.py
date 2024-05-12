'''

   El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con
   las siguientes columnas:

   nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa),
   Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada),
   volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

   Construir una función que construya un DataFrame a partir del un fichero con
   el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.


'''

import pandas as pd

def mostrar(nombreColumnas):

    datos = pd.read_csv("../informacion/archivos/cotizacion.csv")

    df = pd.DataFrame(datos)

    columnas = df[nombreColumnas]

    estadisticas = {}

    for i in range(len(nombreColumnas)):

        estadisticas[nombreColumnas[i]] = {
            'maximo': columnas[nombreColumnas[i]].max(),
            'minimo': columnas[nombreColumnas[i]].min(),
            'media': round(columnas[nombreColumnas[i]].mean(), 2)}

    nuevoDataFrame = pd.DataFrame(estadisticas)

    return nuevoDataFrame

print(mostrar(['Final',"Efectivo", "Volumen"]))
