#Usar los diferentes graficos del metodo plot, teniendo en cuenta el argumento kind

import pandas as pd
import matplotlib.pyplot as plt


datos = pd.read_csv("../../ficheros/calificaciones.csv")

df = pd.DataFrame(datos)

#Grafico de lineas
df.plot(x='apellido', y='examen1', kind='line')
plt.xticks(rotation=25)
plt.ylabel('examen1')

#Grafico de barras
df.plot(x='apellido', y='examen2', kind='bar')
plt.xticks(rotation=25)
plt.ylabel('examen2')

#Grafico de puntos
df.plot(x='apellido', y='practica', kind='scatter')
plt.xticks(rotation=25)

#todos en uno solo
fig, ax = plt.subplots()

df.plot(x='apellido', y='examen1', color='blue', ax=ax)
df.plot(x='apellido', y='examen2', color='yellow', ax = ax)
df.plot(x='apellido', y='practica', color='brown', ax=ax )
plt.xticks(rotation=25)

plt.grid()
plt.show()

print(df.to_string())