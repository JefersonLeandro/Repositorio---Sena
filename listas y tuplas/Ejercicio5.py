'''

Escribir un programa que almacene en una lista los numeros
del 1 al 10 y los muestre por pantalla en orden inversos separados
por comas.

'''

print("solucion 1 ")
lista = [1,2,3,4,5,6,7,8,9,10]
lista.reverse()
for i in range(len(lista)):
    print(lista[i], end=", ")

print("\n")

print("solucion 2 ")
lista2 = [1,2,3,4,5,6,7,8,9,10]
for j in range(10, 0, -1):
    print(lista2[j-1], end=", ")


# soluciones segun el ejercicio
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, 11):
#     print(numbers[-i], end=", ")
#
# print("otra")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers.reverse()
# for number in numbers:
#     print(number, end=", ")