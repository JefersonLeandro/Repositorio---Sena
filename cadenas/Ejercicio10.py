'''
    Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
    separados por comas, y muestre por pantalla cada uno de los productos en una linea distinta.
'''

productos  = input("Escriba los productos separados por coma ") # arroz, carne, pescado , mariscos

print("mis soluciones ")

print("solucion 1  split ")
separados  = productos.split(",")

print("\t" + separados[0])
print("\t" + separados[1])
print("\t" + separados[2])
print("\t" + separados[3])

print("solucion 2 find ")

transantepenultimo  = productos[:productos.find(",")]
antepenultimo  = productos[productos.find(",")+1:]
penultimo  = antepenultimo[antepenultimo.find(",")+1:]
ultimo = penultimo[penultimo.find(",")+1:]

print(f" 1 - {transantepenultimo}")
print(f" 2 - {antepenultimo[:antepenultimo.find(",")]}")
print(f" 3 - {penultimo[:penultimo.find(",")]} ")
print(f" 4 - {ultimo}")

print("soluciones segun el Ejercicio : ")

print("solucion 1")

print(productos.replace(",", "\n"))
print("solucion 2 ")

print(" \n".join(productos.split(",")))