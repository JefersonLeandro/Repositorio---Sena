import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../archivos/caracteristicas-numericas.csv")

df['Duration'].plot(kind="hist")

plt.show()