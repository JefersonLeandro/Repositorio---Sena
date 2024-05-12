'''

    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal , y
    despues muestre por pantalla la misma frase pero con la vocal introducida en mayuscula

'''

frase = input("Escriba una frase : ")
vocal = input("Escriba una vocal : ")

print(frase.replace(vocal,vocal.upper() ))