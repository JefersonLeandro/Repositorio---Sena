'''


    Escribir una función que calcule el módulo de un vector.


'''
import math


def moduloVector(a , b):
    formula = math.sqrt(a**2 + b**2)
    return formula

print(moduloVector(3,4))
