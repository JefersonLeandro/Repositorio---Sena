'''

    Escribir un programa que pregunte al usuario los numeros ganadores de la loteria
    primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
    mayor.


'''

listaN = []
for i in range(6):
    n = int(input(f"numero {i+1} de la loteria  : "))
    listaN.append(n)

listaN.sort()
print(listaN)