'''

    Escribir una función que simule una calculadora científica que permita calcular el seno,
    coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el
    valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al
    valor introducido y el resultado de aplicar la función a esos enteros.

'''
import math
def calculadora():
    print("CALCULADORA CIENTFICA\n")
    print("-Seno \n-Coseno \n-Tangente \n-Exponencial \n-'Logaritmo' neperiano \n-Salir  ")
    print("---------------")
    function = input("opcion : ").lower()
    diccionario = {}
    print(function)
    cont = 0
    while(function != "salir"):
        valor = int(input("valor : ").lower())
        print("---------------")
        if function in globals():
            resultado = globals()[function](valor) #obtener la funcion por el nombre dentro de un diccionario global donde se almacenan todas
            print(f"resultado : {resultado:.3f}")
            cont +=1
            diccionario[cont] = {'valor' : valor , 'resultado': resultado }
            print("---------------")
            print("tabla : ")
            for clave , contenido  in diccionario.items():
                print(clave,"--",contenido['valor'],"--",contenido['resultado'])

            print("---------------")

        else:
            print("-----------------------")
            print("Función no válida. Inténtalo de nuevo.")
            print("-----------------------")

        print("CALCULADORA CIENTFICA\n")
        print("-Seno \n-Coseno \n-Tangente \n-Exponencial \n- 'Logaritmo' neperiano \n-Salir  ")
        print("-----------------------")
        function = input("opcion : ").lower()


def seno(valor):
    seno = math.sin(math.radians(valor))
    return seno

def coseno(valor):
    coseno = math.cos(math.radians(valor))
    return coseno

def tangente(valor):
    tangente = math.tan(math.radians(valor))
    return tangente

def exponencial(valor):
    exponencial = math.exp(valor)
    return exponencial

def logaritmo(valor): #se entiende como neperiano o natural.
    desicion = input("desea especificar la base (si/no) : ").lower()

    logaritmo = 0
    if desicion == "si":
        base = float(input("Escriba la base : "))
        logaritmo  = math.log(valor, base)
    else:
        logaritmo  = math.log(valor)

    return logaritmo


calculadora()