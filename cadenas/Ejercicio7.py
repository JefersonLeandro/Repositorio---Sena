'''

    Escribir un programa que pregunte el correo electronico del usuario en la consola y muestre por pantalla
    otro correo electronico con el mismo nombre (la parte delante de la arroba @ pero con dominio ceu.es

'''

correo = input("Escriba un correo ")
dominio = "@ceu.es"

print(correo[:correo.find("@")]+dominio)

