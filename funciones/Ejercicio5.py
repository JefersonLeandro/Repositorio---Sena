'''


    Escribir una función que calcule el área de un círculo y otra que calcule el volumen
    de un cilindro usando la primera función.

    (A = π . r²). - circulo
    (V = π . h . r²) - cilindro

    diametro = linea completa
    radio = mitad del diametro o la mitad de esa linea
'''

def areaCirculo(diametro):
    area  = 3.14 * ((diametro/2)**2)
    return area

def volumenCilindro(altura , diametro):
    area = areaCirculo(diametro)
    volumen = area * altura
    return volumen

print(areaCirculo(16))
print(volumenCilindro(2 , 450))



