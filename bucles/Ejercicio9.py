'''
    Escrbrir un programa que almacene la cadena de caracteres 'contrasena' en una variable
    pregunte al usuario por la contrasena hasta que introduzca la contrasena correcta

'''


contrasena = "contrasena"
passwordUsuario = input("Escriba la contrasena : ")

print("while: ")
while passwordUsuario!= contrasena:
    print("\t-Contrasena incorrecta- ")
    passwordUsuario = input("Escriba la contrasena : ")
print("\t-Catrasena correcta- Bienvenido al limbo   ")




