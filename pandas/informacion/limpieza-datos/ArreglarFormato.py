import pandas as pd

# existen dos formas para arreglar un formato equivocado
# 1.convertir el formato de la columna a un formato en especifico


df = pd.read_csv("../archivos/acondicionamiento-fisico.csv")
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# 2. eliminar la fila
df.dropna(subset=['Date'] , inplace=True)

# algunas veces las columnas tienen mal los datos por eejemplo el promedio de la session de una persona se puede ver que
# en la columna duracion en la fila 7 esta 450 este valor puede ser verdadero pero al observar el resto de datos se sabe que la
# session de esta persona fue de 45 toodo esto para data frame pequeños ya que en los grandes se utilizan loops


# df.loc[7, "Duration"] = 45 # pequenas

# para grandes data frames y poder controlar los limites de los datos segun el metodo que se aplique
#usando loc
# for i in df.index:
#
#     if df.loc[i, "Duration"] > 120:
#         df.loc[i, "Duration"] = 120


# #usando drop
for j in df.index:
    if df.loc[j, "Duration"] > 120 :
        df.drop(j, inplace=True)







print(df.to_string())
