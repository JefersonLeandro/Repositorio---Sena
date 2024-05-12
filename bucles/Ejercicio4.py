'''
    Escribir un programa que pida al usuario un numero entero
    positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero
    separados por comas.

'''
numero = int(input("Escriba un numero entero positivo : "))
numero2 = numero
# while
print("numeros en decendencia : ")
print("while : ")


while numero != -1 :
    print(numero, end=",")
    numero -= 1

print("\nfor: ")

x = numero2
for i in range(numero2+1):
   print(x,end=",")
   x -=1
# otra forma de hacerlo segun el ejercicio
n = int(input("\nIntroduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")