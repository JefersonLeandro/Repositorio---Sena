import matplotlib.pyplot as plt
import numpy as np

# Crear una figura y un eje utilizando subplots para una buena gestión del gráfico
fig, ax = plt.subplots()

# Generar 100 puntos linealmente espaciados entre -3.0 y 3.0 para el eje x
x = np.linspace(-3.0, 3.0, 100)
# Generar 100 puntos linealmente espaciados entre -3.0 y 3.0 para el eje y
y = np.linspace(-3.0, 3.0, 100)

# Crear una malla de coordenadas a partir de los vectores x y y
x, y = np.meshgrid(x, y)

# Calcular los valores de z basados en la función matemática elegida
z = np.sqrt(x**2 + 2*y**2)

# Dibujar un gráfico de contorno relleno usando los datos de x, y y z
ax.contourf(x, y, z)

# Mostrar la gráfica en pantalla
plt.show()