'''

    Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
    sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
    que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
    contenido del diccionario.

'''

diccionarioInformacion = {}

nombre  = input("Escriba su nombre : ")
diccionarioInformacion["nombre"] = nombre
print(diccionarioInformacion)

edad  = input("Escriba su edad : ")
diccionarioInformacion["edad"] = edad
print(diccionarioInformacion)

sexo  = input("Escriba su sexo : ")
diccionarioInformacion["sexo"] = sexo
print(diccionarioInformacion)

telefono  = input("Escriba su telefono : ")
diccionarioInformacion["telefono"] = telefono
print(diccionarioInformacion)

correo  = input("Escriba su correo electronico : ")
diccionarioInformacion["correoElectronico"] = correo
print(diccionarioInformacion)

print("solucion segun el ejercicio : ")
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
