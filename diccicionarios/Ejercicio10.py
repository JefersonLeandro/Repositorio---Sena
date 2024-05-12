'''

    Escribir un programa que permita gestionar la base de resultados de clientes de una empresa.

    Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
    y el valor será otro diccionario con los resultados del cliente (nombre, dirección, teléfono,
    correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente.

    El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
    (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes
    preferentes, (6) Terminar.

    En función de la opción elegida el programa tendrá que hacer lo siguiente:

    1.Preguntar los resultados del cliente, crear un diccionario con los resultados y añadirlo a la base de resultados.
    2.Preguntar por el NIF del cliente y eliminar sus resultados de la base de resultados.
    3.Preguntar por el NIF del cliente y mostrar sus resultados.
    4.Mostrar `lista` de todos los clientes de la base resultados con su NIF y nombre.
    5.Mostrar la lista de clientes preferentes de la base de resultados con su NIF y nombre.
    6.Terminar el programa.


'''
respuesta = 0
bdDatos = {}
while respuesta != 6:
    print("---Base de resultados - clientes-- ")
    print("--MENU--\n 1. Añadir cliente \n 2. Eliminar cliente \n 3. Mostrar cliente \n 4. Listar todos los clientes \n 5. Listar clientes preferentes \n 6. Terminar")
    respuesta = int(input("Opcion : "))

    if respuesta == 1:
        nombre = input("Escriba su nombre : ")
        documento = int(input("Escriba su numero de documento -NIF : "))
        direccion = input("direccion de residencia : ")
        telefono = input("Telefono : ")
        correo = input("correo : ")
        preferente =  input("Usted es preferente (si/no) : ").lower() == "si"
        bdDatos[documento] = {"nombre" : nombre, "documento" : documento, "direccion" : direccion, "telefono" :  telefono,
                              "correo" : correo, "preferente" : preferente}
        print("--- cliente añadido con exito ---")

    elif respuesta == 2:
        print("* Persona a eliminar ")
        documento = int(input("Escriba el numero de documento : "))
        if documento in bdDatos :
            bdDatos.pop(documento, 0)
            print("--cliente eliminado con exito---")
            print(bdDatos)
        else :
            print("--El cliente solicitado no se encuentra registrado--")

    elif respuesta == 3:
        print("* Persona a mostrar ")
        documento = int(input("Escriba el numero de documento : "))

        if documento in bdDatos:
            print("<resultados>")
            for clave , valor in bdDatos[documento].items():
                print(f" { clave } : {valor}")
        else:
            print("--El cliente solicitado no se encuentra registrado--")

    elif respuesta == 4:
        print("* Personas con nombre y documento")
        if bdDatos is not None :
            print("resultados : ")
            for clave, valor in bdDatos.items():
                print("---------------------")
                print("nombre :", valor["nombre"])
                print("documento :", clave)
                print("----------------------")
        else:
            print(" base de resultados vacia ")
    elif respuesta == 5:
        print("* Personas Preferentes con nombre y documento")
        if bdDatos is not None:
            print("resultados : ")
            cont = 0
            for clave, valor in bdDatos.items():
                if valor["preferente"] == True:
                    print("---------------------")
                    print("nombre :", valor["nombre"])
                    print("documento :", clave)
                    print("----------------------")
                    cont+=1
                elif cont == 0:
                    print("no hay clientes preferentes")
        else:
            print(" base de resultados vacia")

    elif respuesta != 6:
        print("respuesta invalida")
