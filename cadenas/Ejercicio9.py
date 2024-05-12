'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento
en formato dd/mm/aaaa y muestra por pantalla , el dia , el mes y el año .

adaptar el programa anterior para que tambien funcione cuando el dia o el mes se introduzcan
con un solo caracter

'''

print("mi solucion :  ")
print("Escriba su fecha nacimiento con el siguiente formato  ")
fecha = input("dd/mm/aaaa -> ")

dia = fecha[:fecha.find("/")]
añoMes = fecha[fecha.find("/")+1:]
mes = añoMes[:añoMes.find("/")]
año = añoMes[añoMes.find("/")+1:]


print(f"el dia es : {dia} ")
print("el mes es :", mes)
print("el año es : "+ año)

print("Solucion segun el ejercicio :  ")
print( "dia - " , fecha[0:2])
print( "mes - " , fecha[3:5])
print( "año - " , fecha[6:])




