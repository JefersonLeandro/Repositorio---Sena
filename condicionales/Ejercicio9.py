'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar.

El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
si el cliente es menor de 4 años y 18 años debe pagar 5 euros y si es mayor de 18 años , 10 euros


'''

edad = int(input("Escriba su edad : "))
if edad >=1:
    if edad <=18:
        pagar = 5
    else:
        pagar = 10
    if edad < 4 :
        print("tu entrada es gratis")
    else:
        print(f"debes pagar por la entrada : {pagar} euros")
else :
    print("digite una edad valida ")

