
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("../Archivos/top100cities_weather_data.csv")
df = pd.DataFrame(datos)
df = df[['City', 'Temperature (Celsius)']]
ciudades = df['City']
print("Temperaturas - Ciudades")
print("Elige 5 cuidades a las viajarias : ")
print(ciudades.to_string())
cont = 0
selecciones = []

while cont != 5:
    n = int(input(f"Escribe el numero de la cuidad {cont+1}  : "))
    if n in df.index:
        selecciones.append(n)
        print(f"La ciudad '{df['City'][n]}' se agrego correctamente.")
        cont+=1
    else:
        print("cuidad no encontrada")

filas = df.iloc[selecciones]
print(filas)
filas.plot(x='City', y='Temperature (Celsius)')
plt.show()





