'''
Escribir un programa que pida al usuario dos numeros y muestre por pantalla su division.
si el divisor es cero el programa debe mostrar un error.
'''

dividiendo =float(input(" dividiendo : "))
divisor =float(input(" divisor : "))

if divisor > 0 or divisor < 0  :
    division = dividiendo / divisor
    print(f"El resultado de su division es : {division} ")
else:
    print("ERROR")
    print("no se puede dividir en cero")
