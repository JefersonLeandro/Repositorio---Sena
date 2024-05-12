'''

    Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.


    El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente,
    añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.]

    El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente
    y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.


'''




def agregar():

    respuesta = " "
    while  respuesta != "n" :
        nombre = input("Escriba el nombre de la persona : ").title()
        telefono = input("Escriba su numero telefonico : ")

        with open("listin.txt", "a") as fichero:
            fichero.write(nombre + "," + telefono + "\n")
        respuesta = input("'s'  -> para continuar o 'n' -> para salir. ")


def consultar():

    nombre = input("Escriba el nombre del cliente a consultar : ").title()
    with open("listin.txt", "r") as fichero:

        contenido = fichero.read()
        lista = contenido.split("\n")

        bandera = True
        for cadena in lista:
             items = cadena.split(",")
             if len(items) == 2 and nombre == items[0]:
                    print("---persona encontrada------")
                    print(f"nombre - {nombre}  telefono -  {items[1]}")
                    print("---------------------------")
                    bandera = False

        if bandera:
            print(f"el nombre {nombre} no coincide con nuestros registros")

def eliminar():

    nombre = input("Escriba el nombre del cliente a eliminar : ").title()

    nuevoContenido = []
    with open("listin.txt", "r") as fichero:
        contenido = fichero.read()

        lista = contenido.split("\n")

        bandera = False
        for cadena in lista:
            items = cadena.split(",")
            if len(items) == 2 and nombre != items[0]:
                nuevoContenido.append(cadena)

            elif nombre == items[0]:

                print("---persona eliminada------")
                print(f"nombre - {nombre}  telefono -  {items[1]}")
                print("---------------------------")
                bandera = True

        if bandera:
            with open("listin.txt", "w") as fichero:

                for cadena in nuevoContenido:

                    fichero.write(cadena+"\n")
        else:

            print("nombre no encontrado")




print("------------------")
print("Menu Telefonico")
print("------------------")

print(" 1.Agregar  \n 2.Consultar  \n 3.Eliminar \n 4.Salir")
accion = input("digite la operacion : ")

print(accion)



while accion != "4":

    if accion.isdigit():
        accion = int(accion)
        if accion >= 1 and accion <= 4 :
                if accion == 1:
                   agregar()
                elif accion == 2:
                    consultar()
                elif accion == 3:
                    eliminar()

    else:
         print("Accion erronea, digitela nuevamente. ")
    print("------------------")
    print("Menu Telefonico")
    print("------------------")

    print(" 1.Agregar  \n 2.Consultar  \n 3.Eliminar \n 4.Salir")
    accion = input("digite la operacion : ")









