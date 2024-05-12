'''

    Escribir un programa que muestre por pantalla la tabla
    de multiplicar del 1 al 10.


'''
print("for : ")
for i in range(10):
    producto = (i+1) * (i+1)
    print(f"{i+1} x {i+1} : {producto} ")

print("while: ")
j = 1
while j != 11:
    resultado = j * j
    print(f" {j} x {j} : {resultado}")
    j += 1


print("Otros ejercicios de practico  ")

numero = int(input("Escriba un numero : "))

for i in range(10):
    resultado = numero * (i+1)
    print(f" {numero} x {i+1} = {resultado}")


print("Finalmente todas las tablas de multiplicar \n son : ")

for i in range(10):
    for j in range(10):
        resultado = (j+1) * (i+1)
        print(f" {i+1} x {j+1} = {resultado} ")
    print("\n")