'''

    los telefonos de una empresa tienen el siguiente formato ' prefijo - numero - extension'
    donde el prefijo es el codigo del pais +34 , y la extension tiene dos digitos (por ejemplo
    +34-913724710 - 56 ) .
    Escribir un programa que pregunte por numero de telefono con este formato y muestre por pantalla
    el numero de telefono sin el prefijo y la extension


'''

numeroFormato = input("Escriba el numero con formato ")

print("el numero es : ", numeroFormato[4:-3])