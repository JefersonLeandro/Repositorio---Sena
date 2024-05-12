'''

    Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt
    con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre
    por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

'''


def leertablaMultiplicar():
    numero = input("Escriba un numero entre 1 y 10 : ")

    try:
        with open(f"resultados/tablas/tabla-{numero}.txt" , "r") as fichero:
            contenido = fichero.read()
            print(contenido)

    except FileNotFoundError:
        print("tabla de multiplicar no encontrada")

leertablaMultiplicar()