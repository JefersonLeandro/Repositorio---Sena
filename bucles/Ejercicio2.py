'''
Escribir un preograma que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad)

sR
'''

# solucion 1
edad = int(input("Escriba su edad : "))

# for
print("todos los años que has cumplido son : ")
for i in range(edad):

 if i == 0 :
    print(i+1,"año")
 else:
    print(i+1,"años")

# while
print("Con un while")
stop = 1
while stop<=edad:
    print(stop,"años")
    stop+=1