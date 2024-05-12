'''
praticando el bucle for

    parametros del range (inicio , limite, diferencia)
    inicio 1
    limite  hasta 27 sin incluirlo , si se se quiere incluir sumar + 1
    difirencia 5

    el cuenta la diferencia un numero adelante osea en este caso el empieza a cotar desde 1
    for i in range(0, numero , 5):   ->  0,5,10,15,20,25
         print(i)

'''

# entre un limite a otro
# for i in range(13, 23):
#     print(i+1)


# n = int(input("\nIntroduce un número entero positivo: "))
# for i in range(1, n+1, 2):
#     print(i, end=", ")

# n = int(input("\nIntroduce un número entero positivo: "))
# for i in range(n, -1, -1):
#     print(i, end=", ")


# numero = int(input("Escriba un numero : "))
#
# for i in range(0, numero , 5):
#     print(i)

frase = input("Escriba una frase : ")


for i in frase:
    print(i)