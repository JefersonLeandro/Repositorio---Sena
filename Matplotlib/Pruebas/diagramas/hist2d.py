import numpy as np
import matplotlib.pyplot as plt

# Crear figura y eje para el gráfico
fig, ax = plt.subplots()

# Generar 1000 muestras de una distribución normal multivariante
x, y = np.random.multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, 0.4], [0.4, 0.5]], size=1000).T

# Graficar un histograma bidimensional de x e y
ax.hist2d(x, y)

# Mostrar el gráfico
plt.show()
