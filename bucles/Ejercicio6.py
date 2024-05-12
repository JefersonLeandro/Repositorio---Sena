'''

    Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo
    rectangulo como el de mas abajo , de altura el numero introducido .
    *
    **
    ***
    ****
    *****

'''

numero = int(input("Escriba un numero entero : "))

print("triangulo rentangulo , 90 grados")
print("for : ")
for i in range(numero):
   print("*"*(i+1))

print("while : ")
j = 1
while j <= numero:
   print("*"*j)
   j+=1

# otra forma segun el ejercicio
n = int(input("\nIntroduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")