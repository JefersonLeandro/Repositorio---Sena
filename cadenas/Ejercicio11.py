'''
Escribir un programa que pregunte el nombre el un producto , su precio y un numero de unidades
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario
con 6 digitos enteros y 2 decimales, el numero de unidades con tres digitos y el coste total con 8 digitos enteros
y 2 decimales

'''
print("mi solucion pensando que era cadena concatenando numeros :  ")

nombre = input("Escriba el nombre del producto :")
precio = float(input("Escriba el precio del producto :"))
stock  = int(input("Escriba las unidades del producto :"))

coste  = precio * stock

xx
print(f"{precio}123456.23-{stock}987-{coste}87654321.09")

print("solucion segun el ejercicio :  ")

print('{nombre} : {precio:9.2f} x {unidades:3d}  = {total:11.2f}   '.format(nombre = nombre, precio = precio, unidades = stock, total = precio * stock))