'''
    Escribir un programa que muestre el eco de todoo lo que el usuario
    introduzca hasta que el usuario escriba "salir" que terminara.



'''

caracteres = input("Escriba algo (letras , simbolos , numeros o palabras ) : ")
# mi solucion
print("Escriba 'salir' para salir  " )
stop = " "
tamano = len(caracteres)
while stop != "salir":
    for i in range(tamano):
        print(f"   {caracteres[:(i+1)] }    ")

    stop = input("Desea (Continuar o salir) : ")




# solucion segun el ejercicio
print("solucion 2 ")
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)