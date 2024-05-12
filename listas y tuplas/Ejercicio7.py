'''
    Escribir un programa que almacene el abecedario en una lista,
    elimine de la lista las letras que ocupen posiciones multiplos de 3
    y muestre por pantalla la lista resultante.



    -------------------------------------------------------------------------
     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
    "a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","n","o","p","q","r","s","t","u","v","w","x","y","z"
                 d          g            j           m           o           r           u           x
'''

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
print("multiplos de 3 ")
print("tamano : ",len(abecedario))

cont = 0
for i in range(3, len(abecedario), 3):
    print(i,end=", ")
    abecedario.pop(i-cont)
    cont+=1


print("\nabecedario final :  ")
print(abecedario)

print("solucion 2 : ")

cont = 0
abecedario =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","ñ","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for j in range(1,len(abecedario)):
    if j % 3 == 0:
       abecedario.pop(j - cont)
       cont +=1

print("abecedario 2  ")
print(abecedario)