'''

    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.

    Escribir una tercera función que reciba un diccionario con los precios y
    porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la
    función pasada para aplicar los descuentos o el IVA a los productos de la cesta
    y devolver el precio final de la cesta.


'''

#descuento
def descuento(precio , descuento):

    descuento = (precio * descuento)/100
    precioFinal = precio - descuento
    return precioFinal

#iva al 19 %
def iva(precio):
    descuento = precio * 0.19
    precioFinal = precio + descuento
    return precioFinal


def cestaCompra(diccionario):

    precioFinal = 0
    for clave , valor in diccionario.items():
         precioNeto = descuento(clave, valor )
         precioFinal += precioNeto

    return precioFinal

print(descuento(23000 , 5))
print(iva(23000))
print(cestaCompra({23000 : 4 , 40000 : 5 , 12000:3 , 67000: 5 , 78000 : 5 } ))

#920,2000,360,3350,3900