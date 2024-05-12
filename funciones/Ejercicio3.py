'''

    Escribir una función que reciba un número entero positivo y devuelva su factorial.

    5X4X3X2X1

'''

# range([start], stop, [step])

def numeroFactorial(numero):

   factorial = numero
   for n in  range(numero, 1, -1):
        factorial *=  (n-1)

   return print(factorial)
numeroFactorial(5)