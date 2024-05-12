import pandas as pd

# metodo duplicated() devuelve un valor boleano

df = pd.read_csv("../archivos/acondicionamiento-fisico.csv")

print(df.duplicated())

# para eliminar los duplicados
df.drop_duplicates(inplace=True)
