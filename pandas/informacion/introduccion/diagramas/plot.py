import pandas as pd
import matplotlib.pyplot as plt

# Método para crear diagramas en combinación con otras librerías, en este caso Matplotlib
df = pd.read_csv("../../archivos/caracteristicas-numericas.csv")

df.plot()

# Muestra la figura antes de guardarla
plt.show()


