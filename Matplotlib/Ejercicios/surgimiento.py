'''

     Graficar los años de creacion en un diagrama de barras
     de los siguientes lenguajes

     lenguajes :

     Html : 1991, CSS : 1994,  Python : 1991, Java : 1995 , JavaScript : 1995,
     Php : 1994 , C# : 2000 , C++ : 1985 , y Sql : 1970


'''
import matplotlib.pyplot as plt

#figura y el los ejes
fig, ax = plt.subplots()

# Datos
x = ['HTML', 'CSS', 'Python', 'Java', 'PHP','JavaScript' , 'C#', 'C++', 'SQL']
y = [1991, 1994, 1991, 1995, 1994, 1995 , 2000, 1985, 1979]


# Crear gráfico de barras
ax.bar(x, y, color='black')

# Ajustando los límites del eje y para asegurar que todos los datos se muestren completamente
ax.set_ylim([1970, 2005])  # rango de años


#celdas
ax.grid(axis = 'y' , color = 'gray', linestyle='dashed')

plt.title("Surgimiento de lenguajes ")
plt.ylabel("Años")
plt.xlabel("Lenguajes")

# Mostrar gráfico
plt.show()
