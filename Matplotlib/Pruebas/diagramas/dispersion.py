import matplotlib.pyplot as plt

#crear la figura y los ejes
fig, ax = plt.subplots()

#dibujar los puntos
ax.scatter(x = [1,2,3] , y = [3,2,1])

#Guardar el grafico en formato png
plt.savefig('diagrama.dispersion.png')

#Mostrar el grafico
plt.show()