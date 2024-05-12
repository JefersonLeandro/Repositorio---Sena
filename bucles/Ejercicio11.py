'''

Escribir un programa que pida al usuario una palabra y luego
muestre por pantalla una a una las letras de la palabra introdroducida
empenzando por la ultima


'''
palabra = input("Escriba una palabra : ")
tamano = len(palabra)
print("while : ")

while tamano != 0:
    print(palabra[tamano-1])
    tamano-=1

print("for : ")

tamano = len(palabra)
for i in range(tamano):
    print(palabra[tamano-1])
    tamano-=1

# otra forma de hacerlo segun el ejercicio
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])