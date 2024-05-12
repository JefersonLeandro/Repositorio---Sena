import pandas as pd

leer = pd.read_csv("../archivos/acondicionamiento-fisico.csv")

# remplazarCero = leer.fillna(0) # remplaza los datos vacios por cero
# remplazarCadena = leer.fillna("dato vacio") # remplaza los datos vacios por "dato vacio"
# leer.fillna(0 , inplace=True) # lo hace pero modificando los datos en momoria

# print(leer)
# print("---------------")
# De forma especifica

# leer["Date"] = leer["Date"].fillna("0000/00/00")
#
# leer.fillna({"Calories" : 123}, inplace=True) # replazar por un valor por default
# print(leer)

# print("---------------")
#remplezando valores por valores aritmeticos como la media , mediana moda

media = leer["Calories"].mean()
mediana = leer["Calories"].median()
moda = leer["Calories"].mode()[0]
leer.fillna({"Calories" : moda} , inplace=True)
print(leer)
