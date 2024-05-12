'''

    Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
    pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
    ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

    Fruta	Precio
    Plátano	1.35
    Manzana	0.80
    Pera	0.85
    Naranja	0.70


'''

diccionarioFrutas = {"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70, }


fruta =  input("Escriba una fruta : ").title()
nkilos =  float(input("Escriba el numero de kilos : "))

if fruta in diccionarioFrutas:
    precio = diccionarioFrutas[f"{fruta}"] * nkilos
    print(f"Usted debe pagar {precio:.2f} Euros")
else:
    print("Fruta no disponible ")