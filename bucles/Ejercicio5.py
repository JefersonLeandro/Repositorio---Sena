'''
    Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual
    y el numero de años y muestre por pantalla el capital obtenido en la inversion cada año que
    dura la inversion
sR

'''


cantidadInvertir = float(input("Cantidad Invertir : "))
interesAnual = float(input("El interes anual : "))
años = int(input("El numero de años : "))

print("for : ")

for i in range(años):
    capital = round(cantidadInvertir * (interesAnual / 100 + 1) **(i+1), 2)
    print(f"el captital del año {i+1} es : {capital}")

print("while: ")

j = 1
while j <= años:
    capital = round(cantidadInvertir * (interesAnual / 100 + 1) **j, 2)
    print(f"el captital del año {j} es : {capital}")
    j+=1