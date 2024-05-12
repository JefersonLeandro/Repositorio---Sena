import pandas as pd

# numero y porcentaje de hombres y mujeres en el barco.
datos = pd.read_csv("../archivos/titanic.csv")

df = pd.DataFrame(datos)

numero = df['Sex'].value_counts()
porcentaje = df['Sex'].value_counts(normalize=True)*100

print("numero \n",numero)
print("porcentaje\n",porcentaje)