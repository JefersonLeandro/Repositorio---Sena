'''

    Hacer un diagrama que muestre el numero de pasos dados durante los primeros 7 dias de la semana
    de una persona sedentaria en comparacion con una persona activa.

'''
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("../../Archivos/datosPasos.csv")
df = pd.DataFrame(datos)

fig, ax = plt.subplots()

df.plot(x = 'Dia', y = 'Activa'    , ax = ax, color = 'red', marker='^')
df.plot(x = 'Dia', y = 'Sedentaria'   , ax = ax, color = 'aquamarine' , marker='o')

ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

#labels
plt.title("Actividad semanal ")
plt.ylabel("Numero de pasos")

plt.show()

print(df)

