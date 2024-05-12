'''

 Escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre por pantalla
 el nombre completo del usuario tres veces , una con todas las letras minusculas , otra con todas letras mayusculas
 y otra solo con la primera letra del nombre y de los apellidos en mayuscula. el Usuario puede introducir su nombre combinando
 mayusculas y minusculas como quiera

'''


nombre = input("Escriba su nombre completo : ")
nombreMinuscula = nombre.lower()
nombreMayuscula = nombre.upper()
nombreTitulo = nombre.title()
print("1 minuscula -lower : " + f"  {nombreMinuscula} ")
print("2 mayuscula -upper: " + f"  {nombreMayuscula} ")
print("3 Titulo - title: " + f"  {nombreTitulo} ")
