import pandas as pd


datos = pd.read_csv('../archivos/titanic.csv')
df = pd.DataFrame(datos)
#mostrar el numero de sobrevivientes de muejeres y hombres por cada clase

grupos = df.groupby(['Pclass','Sex'])
sobrevivientes = grupos['Survived'].sum()

print(sobrevivientes)

