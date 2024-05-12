'''


    Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar
    de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por
    pantalla informando de ello.

'''

def mostrarlinea():

    nTabla = input("numero entre 1 y 10 : ")
    nLinea = int(input("numero de linea : "))

    try:
        with open(f"resultados/tablas/tabla-{nTabla}.txt" , "r") as fichero:

            lineas = fichero.readlines()
            print(lineas[nLinea - 1 ])

    except FileNotFoundError:
        print(f"la tabla {nTabla} de multiplicar no existe")

mostrarlinea()





#hay un metodo especial para leer una linea especifica readLines()