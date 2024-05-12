'''

los tramos impositivos para la declaracion de la renta en determinado pais son los siguientes :

 Renta en euros              -    Tipo de impositivo
     Menos de 10000          -    5 %
     Entre 10000 y 20000     -    15 %
     Entre 20000 y 35000     -    20 %
     Entre 35000 y 60000     -    30 %
     Mas de 60000            -    45 %

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo
que le corresponde
'''
renta = float(input("su renta anual en euros es : "))

if renta >=1 :
    if renta < 10000 :
        print("su impositivo es : 5%")
        tipoImpositivo  = 0.05
    elif renta < 20000 :
        print("su impositivo es : 15%")
        tipoImpositivo  = 0.15
    elif renta < 35000 :
        tipoImpositivo  = 0.20
        print("su impositivo es : 20%")
    elif renta < 60000 :
        tipoImpositivo  = 0.30
        print("su impositivo es : 30%")
    else:
        tipoImpositivo  = 0.45
        print("su impisitivo es : 45%")
    pagar = tipoImpositivo * renta
    print(f" su impositivo a pagar es de : {pagar:.2f} euros ")
else:
    print("Dato erroneo ")