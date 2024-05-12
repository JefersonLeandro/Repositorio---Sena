'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
uno ingresos iguales o superiores a 1000 euros mensuales.

Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla
si el usuario tiene que tributar o no
'''

edad = int(input("escriba su edad : "))
ingresos = float(input("escriba sus ingresos : "))

if edad > 16 and ingresos >= 1000 :
    print("Usted puede tributar")

else:
    print("no puede tributar")