import pandas as pd
#muestra las primeras filas de un archivo

df = pd.read_csv("../archivos/data.csv")


print(df.head())# 5 primeras filas
print(df.head(10))# especifico las 10 primeras filas
