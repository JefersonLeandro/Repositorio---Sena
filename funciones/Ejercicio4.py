'''
    Escribir una función que calcule el total de una factura tras aplicarle el IVA.
    La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
    Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


'''

def facturacion(cantidad, porcentaje=None):
    if porcentaje == None:
        porcentaje = 21

    iva = (cantidad * porcentaje) / 100
    total = cantidad + iva
    return total

print(facturacion(45000))
print(facturacion(45000,19))
