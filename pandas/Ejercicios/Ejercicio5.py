'''

    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

'''

import pandas as pd

def balance(diccionario, meses):


    df = pd.DataFrame(diccionario)


    # Establecer la columna 'Mes' como índice
    df = df.set_index('Mes')

    # Seleccionar solo los meses especificados
    dfMeses = df.loc[meses]

    # resultado de la resta de los gatos y las ventas solamente de esos meses
    dfMeses['Balance'] = dfMeses['Ventas'] - dfMeses['Gastos']

    # se acede ala columna balance y se suman su valores dando un unico resultado
    return dfMeses.Balance.sum()

    # print(df[df.Mes.isin(meses)]) mas facil de usar para filtrar los datos


print(balance( {"Mes" : [ "Enero","Febrero" , "Marzo", "Abril"],
              "Ventas" : [30500, 35600, 28300, 33900],
              "Gastos" : [22000, 23400, 18100, 20700]
              }, ['Abril','Febrero','Enero' ]))