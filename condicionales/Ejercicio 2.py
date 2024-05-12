'''

Escribir un programa que almacenen la cadena de caracteres contrasena en una variable, pregunte
al usuario por la contrasena e imprima por pantalla si la contrasena introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas

'''

contrasena = "contrasena"

contrasenaUsuario = input("escriba la contraseña: ").lower()

if contrasenaUsuario == contrasena :
    print("las contraseñas coinciden")
else:
    print("las contraseñas son diferentes")
