'''

Escribir un programa que pregunte por una muestra de números, separados por comas,
los guarde en una lista y muestre por pantalla su media y desviación típica.


'''


import  math

muestra = input("Escriba la muestra de numeros separados por comas : ")
listaNumeros = []
suma = 0

for i in muestra.split(","):
    listaNumeros.append(float(i))

suma = sum(listaNumeros)
tamano = len(listaNumeros)
media = suma / tamano
desviacionTipica = 0

for numero in listaNumeros:
    desviacionTipica += (numero-media)**2


desvicionTipicaFinal =  math.sqrt(desviacionTipica/tamano)
print(f"la media es : {media}")
print(f"la desviacion tipica es : {desvicionTipicaFinal:.2f}")

