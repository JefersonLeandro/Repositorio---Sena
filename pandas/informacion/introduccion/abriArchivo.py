
import pandas as pd


print("numero de datos por default")

leer = pd.read_csv("../archivos/data.csv")
print(leer)

print("todos los datos cambiando el tamano por default\n")

pd.options.display.max_rows = 9999

print(leer)






