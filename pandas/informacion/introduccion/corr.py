import pandas as pd

df = pd.read_csv("../archivos/caracteristicas-numericas.csv")


print(df.corr())