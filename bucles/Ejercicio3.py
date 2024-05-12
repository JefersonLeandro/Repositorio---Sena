'''

    Escriba un programa que pida al usuario un numero entero positivo y muestre por
    pantalla todos los numeros impares desde 1 hasta ese numero separados por comas

esto es aparte
    puede tener un limite el range range(1, n+1, 2):

'''

numero =  int(input("Escriba un numero entero positivo : "))

# for
print(f"\tLos numeros impares  hasta {numero} son : ")
print("- Con un for  ")

for i in range(numero):
    i+=1
    comprobar = i % 2 != 0 # true o false

    if comprobar:
        print(i, end=",")

print("\n-Con un while  ")

stop = 1
while stop <= numero:
    verificar  = stop % 2 != 0 # true o false

    if verificar:
        print(stop, end= ",")

    stop+=1

# otra forma de hacerlo segun el ejercicio
n = int(input("\nIntroduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")