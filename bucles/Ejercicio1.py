'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla
10 veces .

sR

'''


palabra =  input("Escriba una palabra : ")

stop = 0
while stop != 10:
    print(stop+1, palabra)
    stop+=1