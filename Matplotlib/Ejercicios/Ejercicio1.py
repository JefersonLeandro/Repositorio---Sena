'''

    Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por
    pantalla un diagrama de líneas con la evolución de las ventas.

    conclusiones
    -preguntar las el rango de años
    -preguntar las ventas


'''
import matplotlib.pyplot as plt

print("VENTAS")
añoInicio = int(input("Escriba el año de inicio : "))
añoFinal = int(input("Escriba el año final :  "))

ventas = []
años = []
for año in range(añoInicio, añoFinal + 1):
    ventaxAño = float(input(f"Escriba las ventas del año {año} : "))
    ventas.append(ventaxAño)
    años.append(año)

fig, ax = plt.subplots()

plt.title("Ventas anuales")
plt.ylabel("Totales")
plt.xlabel("años")
ax.plot( años, ventas , color= 'aquamarine')
plt.show()


print(ventas)