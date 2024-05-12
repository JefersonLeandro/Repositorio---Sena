'''

    Escribir un programa que pida al usuario una palabra y
    muestre por pantalla el número de veces que contiene cada vocal.

'''

# mi solucion
palabra = list( input("Escriba una palabra : "))
vocales = ["a","e","i", "o","u"]


a=0
e=0
i=0
o=0
u=0

for q in range(len(palabra)):
    for j in range(len(vocales)):

        if palabra[q]  == vocales[j] and j == 0:
          a+=1
        elif palabra[q] == vocales[j] and j == 1:
          e+=1
        elif palabra[q] == vocales[j] and j == 2:
          i+=1
        elif palabra[q] == vocales[j] and j == 3:
          o+=1
        elif palabra[q] == vocales[j] and j == 4:
          u+=1


print(f"\nla palabra {palabra} tiene un numero de vocales de : \n  a : {a} , e : {e} , i: {i} , o : {o} , u : {u}     ")


# solucion segun el ejercicio
# word = input("Introduce una palabra: ")
# vocals = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocals:
#     times = 0
#     for letter in word:
#         if letter == vocal:
#             times += 1
#     print("La vocal " + vocal + " aparece " + str(times) + " veces")