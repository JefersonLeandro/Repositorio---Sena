'''

    Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
    la tabla de multiplicar de ese número, done n es el número introducido.


'''

def tablaMultiplicar():

    numero = int(input("digite numero entre 1 y 10 entero : "))

    with open(f"resultados/tablas/tabla-{numero}.txt", "w") as fichero:
        for i in range(1,11):
            resultado = numero * i
            fichero.write(f" {numero} x {i} = {resultado} \n")


    print("tabla guardada", numero)

tablaMultiplicar()