'''

Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

'''

nombre = input("Escriba su nombre : ")
edad = input("Escriba su edad : ")
direccion = input("Escriba su direccion : ")
telefono = input("Escriba su Telefono: ")

diccionarioInformacion = {"nombre":nombre, "edad":edad, "direccion" : direccion, "telefono" : telefono}


print(f" {diccionarioInformacion["nombre"]} tiene {diccionarioInformacion["edad"]} años, vive en {diccionarioInformacion["direccion"]} y su número de teléfono es {diccionarioInformacion["telefono"]}.")