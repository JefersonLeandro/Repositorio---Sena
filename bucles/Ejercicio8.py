'''
    Escribir un programa que pida al usuario un numero entero y muestre
    por pantalla un triangulo rectangulo como el de mas abajo.

    1
    3 1
    5 3 1
    7 5 3 1
    9 7 5 3 1


'''

# mi forma
numero = int(input("Escriba un numero entero : "))

cadena = ""
for i in range(numero):
    impar = (i + 1) % 2 != 0
    if impar:
        cadena +=f"{i + 1}  "
        print(cadena[::-1])


# otra forma de hacerlo segun el ejercicio
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
