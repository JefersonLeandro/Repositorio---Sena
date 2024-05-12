'''
Escribir un programa que almacene en una lista los siguientes
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.


'''


print("solucion 1 ")
listaPrecios = [50,75,46,22,80, 65,8]

listaPrecios.sort()
print(listaPrecios)
print(f"el precio menor es : {listaPrecios[0]} \nel precio mayor : {listaPrecios[-1]}")

print("\nsolucion 2 : ")

listaPrecios = [50,75,46,22,80, 65,8]
tamano = len(listaPrecios)-1

for precio in listaPrecios:
    contMayor = contMenor = 0
    for i in range(len(listaPrecios)):
        if precio > listaPrecios[i]:
            contMayor += 1
        elif precio < listaPrecios[i]:
            contMenor += 1
    if contMayor == tamano:
        print(f"el precio mayor es : {precio}")

    elif contMenor == tamano:
        print(f"el precio menor es : {precio}")

print("\nsolucion segun el ejercicio : ")

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))

