import pandas as pd
import Matplotlib.pyplot as plt

#diagrama dispersion con puntos
df = pd.read_csv("../../archivos/caracteristicas-numericas.csv")

df.plot( kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()