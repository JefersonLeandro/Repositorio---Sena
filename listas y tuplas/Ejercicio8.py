'''

    Escribir un programa que pida al usuario una palabra y muestre
    por pantalla si es un palíndromo.

    palindromo
   - Palabra o frase que se lee igual de derecha a izquierda, que de izquierda a derecha.

'''

palabra = input("Escriba una palabra : ")

if palabra == palabra[::-1]:
    print(f" {palabra , palabra[::-1]} es un palindromo")
else:
    print(f" {palabra} , {palabra[::-1]} no es un palidromo ")

print("solucion 2 : ")
letras = []

for letra in palabra:
    letras.append(letra)

cont = 0
tamano = len(palabra)-1
for i in range(len(palabra)):
    if letras[i] == letras[tamano]:
         cont+= 1
         tamano-=1


if cont == len(palabra):
    print(f" {palabra} es un palindromo")
else:
    print(f" {palabra} no es un palindromo")



