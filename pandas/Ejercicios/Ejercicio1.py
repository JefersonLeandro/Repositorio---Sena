'''


    Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla
    una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.


'''

import pandas as pd

print("INDEXAR VENTAS")

opcion = ''
diccionario = {}

while opcion != 'no':
    año = input("Escriba el año : ")
    ventas = float(input("Escriba las ventas :  "))
    diccionario[año] = ventas
    opcion = input("Desea continuar ? (si/no) : ").lower()


print("\n----------------ventas sin descuento-------------")
serie = pd.Series(diccionario)
print(serie)
print("-----------------------------\n")

print("--------------ventas con descuento---------------")

porcentaje = 0.10

for años , ventas in diccionario.items():

    descuento = ventas * porcentaje # descuento de la venta
    diccionario[años] = ventas - descuento # venta total con el descuento

print(pd.Series(diccionario))