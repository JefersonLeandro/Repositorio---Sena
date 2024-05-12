'''
    Escribir un programa que pregunte al usuario su edad y muestre
    por pantalla si es mayor de edad o no
'''


edad = int(input("Escriba su edad : "))

if edad >=18 and edad <=100:
    print("Eres mayor de edad")
elif edad >=1 and edad<18:
    print("Eres menor de edad")
else:
    print("edad Erronea ")
