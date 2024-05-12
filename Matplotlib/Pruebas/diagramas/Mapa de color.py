import matplotlib.pyplot as plt
import numpy as np


#Crear una figura y un eje con Matplotlib, donde 'fig' es la figura completa y 'ax' es el área de trazado
fig, ax = plt.subplots()

# Generar una matriz de 16x16 elementos con valores aleatorios entre 0 y 1
x = np.random.random((16, 16))

# Usar 'imshow' para mostrar la matriz 'x' como una imagen, donde cada valor se mapea a un color
ax.imshow(x)

# Mostrar la figura con la imagen
plt.show()