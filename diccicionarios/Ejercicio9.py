'''


    Escribir un programa que gestione las facturas pendientes de cobro de una empresa.

    Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número
    de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere
    añadir una nueva factura, pagar una existente o terminar.

    Si desea añadir una nueva factura se preguntará por el número de factura y su coste
    y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número
    de factura y se eliminará del diccionario.

    Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada
    hasta el momento y la cantidad pendiente de cobro.

'''

respuesta  = 0
cantidadCobrada = 0

facturas = {}
while respuesta != 3 :
    print("----Menu facturas---")
    print(" 1. añadir una nueva factura  \n 2. Pagar una factura existente \n 3. Salir")
    respuesta = int(input("Opcion :   "))
    if respuesta == 1:
        numeroFactura = int(input("Escriba el numero de factura : "))
        costeFactura = float(input("Escriba el coste de la factura : "))
        facturas[numeroFactura] = costeFactura
        print("--añadida con exito-- ")
    elif respuesta == 2:
        numeroFactura = int(input(" Numero de factura a pagar : "))
        if numeroFactura in facturas:

            cantidadCobrada += facturas[numeroFactura]
            print("cantidad cobrada : ", cantidadCobrada)
            del(facturas[numeroFactura])
            print("pagada con exito ")
            if len(facturas) >= 1:
                cobroPendiente = 0
                for clave , valor in facturas.items():
                    cobroPendiente += valor
                print(f"La catidad pendiente de cobro es : {cobroPendiente}")
            else :
                print("Usted no tiene facturas por pagar")
        else:
            print("la factura no se encuentra en nuestro registros")
    elif respuesta != 3 :
        print("Digite una opcion valida ")


