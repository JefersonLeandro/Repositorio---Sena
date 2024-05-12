'''


    Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

'''

#metodo euclides de 2 numeros - > mcd
# se devide el numero mas grande entre el mas pequeño se toma el residuo y este pasa al dividendo con el otro numero
# despues se hace la division entre resudios hasta llegar a cero.
import math

print("-----------maximo comun divisor ---------------------")
def mcd(n1, n2):

    if n1 == 0 or n2 == 0:
        return max(n1,n2)

    elif n1 > n2:
        nMayor = n1
        nMenor = n2
    else:
        nMayor = n2
        nMenor = n1

    residuo = -1
    while residuo != 0:

        residuo = nMayor % nMenor
        nMayor = nMenor
        nMenor = residuo

        if residuo == 0 :
            return nMayor

#mcds
print(mcd(156, 120))
print(mcd(24, 36))
print(mcd(48, 18))
print(mcd(81, 27))
print(mcd(105, 45))
print("funcion para sacar el maximo como un divisor -gcd : ,  ", math.gcd(105 , 45))


print("-----------minimo comun multiplo ---------------------")

#minimo comun multiplo
def mcm(n1,n2):
    if n1 > 0 and n2 > 0: #deben ser positivos
        #se halla el maximo comun divisor primero
        rMcd = mcd(n1,n2)
        # despues se procede a multiplicar y su resultado se  devide
        resultado = (n1 * n2 ) / rMcd

    else:
        return " los numeros debe ser positivos"

    return resultado


print(mcm(20 , 2))
print(mcm(12 , 18))
print(mcm(25 , 35))
print(mcm(48, 72))
print(mcm(100 , 140))


# mismo mcd pero realizado por la IA -> chat gpt
def maximoComundivisor(n1, n2):
    # Implementación del algoritmo de Euclides para encontrar el MCD de n1 y n2
    # Inicio del bucle while, se ejecuta mientras n2 no sea cero
    while n2:
        # Actualización de variables dentro del bucle:
        # Calcula el residuo de la división de n1 entre n2
        n1, n2 = n2, n1 % n2
    # Fin del bucle: n2 es cero, y n1 contiene el MCD de los dos números originales
    return n1

# Ejemplo de uso de la función con los números 6 y 12
print("mcd con ")
print("IA -> ",maximoComundivisor(156, 120))


