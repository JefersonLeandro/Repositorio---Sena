'''

Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el numero de veces que aporece la letra en la frase

'''

frase = input("Escriba una frase : ")
letra = input("Escriba una letra : ")

limite = len(frase)
print("for : ")
nVeces = 0
for i in range(limite):
    caracter = frase[i]
    if caracter == letra:
        nVeces +=1

print(f" la frase contiene la letra {letra ,  nVeces} veces  ")

print("while: ")

nVeces = 0
while limite > 0 :
    caracter = frase[limite-1]
    if caracter == letra:
        nVeces+=1
    limite-=1

print(" la frase contiene la letra "+letra+" - ", nVeces , " veces")

# otra forma parecida de hacerlo segun el ejercicio :
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
