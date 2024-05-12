'''

    Escribir un programa que pida al usuario un numero entero y muestre por
    pantalla si es un numero primo o no.


 '''
# mi solucion

numero = int(input("numero entero  : "))

cont = 0
for i in range(numero): # 1,2,3,4,5,6,7 - n = 7

    resultado = numero / (i+1)
    if resultado.is_integer():
        cont+=1

if cont == 2:
    print(f"{numero} es primo")
else:
    print(f"{numero } no es un numero primo")

# soluciones segun el ejercicio
# solucion 1 encuentra divisores diferentes a 1 y de encontrar mas de uno antes de llegar al mismo numero no es primo ya que son divisibles por ese numero pero si no encuentra ninguno y llega al final es primo donde para saber solo ponen si es igual o no obviamente si es igual fue porque hico todoo el recorrido y no encontro otro divisior
n = int(input("\nIntroduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1

if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# solucion 2
# n = int(input("Introduce un número entero positivo mayor que 2: "))
#
# for i in range(2, n):
#     if n % i == 0:
#         break
# if (i + 1)  == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")
