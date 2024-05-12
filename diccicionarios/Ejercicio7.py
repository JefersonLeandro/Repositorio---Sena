'''

    Escribir un programa que cree un diccionario simulando una cesta de la compra.
    El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
    hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista
    de la compra y el coste total, con el siguiente formato

    Lista de la compra

    Artículo 1	Precio
    Artículo 2	Precio
    Artículo 3	Precio
    …	…
    Total	Coste

'''

diccionarioProductos = {}
salir = ""
coste  = 0
while salir != "si":
    producto = input("Ingrese el producto : ")
    precio = float(input("Ingrese el precio : "))
    diccionarioProductos[producto] = precio
    coste += precio
    salir = input("Desea salir? : ").lower()
    print(diccionarioProductos)

print("\nlista de la compra")
for clave, valor  in diccionarioProductos.items():
    print(clave, valor)

print(f"total : {coste} ")