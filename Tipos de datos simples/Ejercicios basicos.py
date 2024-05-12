# Ejercicio 1: mostrar la cadena hola mundo

# print("¡Hola mundo!")

# Ejercicio 2: almacene la cadena ¡Hola mundo! en un variable y luego muestre
# depues por pantalla el contenido de la variable

# miVariable = "¡Hola mundo!"
# print(miVariable)

'''

Ejercicio 3
pregunte el nombre del usuario en la consola y despues de que el usuario
usuario lo intruduzca muestre por pantalla la cadena hola <nombre>, donde
<nombre> es el nombre del usuario
'''

# nombre =  input("Escriba un nombre : ")
# print(f"hola , {nombre}")

'''

Ejercicio 4 
Escribir un programa que muestre por pantalla el resultado 
de la siguiente opereracion aritmetica
(3+2/2.5) elevado 2 . 

'''

# expresion  = ((3+2)/(2 * 5))**2
# print(expresion)
'''
 
Ejercicio 5

Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el coste 
por hora .Despues debe mostrar por pantalla la paga que le corresponde 

'''

# horasT = float(input("Horas trabajadas : "))
# costeH =  float(input("costo por hora "))
#
# totalPaga = costeH * horasT
#
# print(f"su pago total es de : {totalPaga}")


'''
Ejercicio Escribir un programa que lea un entero positivo, 
N , introducido por el usuario y despues muestre en pantalla 
la suma de todos los enteros desde 1 hasta N .  La suma de los N primeros 
enteros positivos puede ser calculada asi : 

suma = ( (n(n+1)) / 2 ) 

'''
#
# n= int(input("Escriba un entero positivo "))
#
# suma = ( (n * ( n + 1 ))/ 2 )
#
# print(f"la suma de todos los numeros es : {suma}")

'''

Escribir un programa que pida al usuario su peso en (kg) y estatura en (m), calcule 
el indice de masa corporal y lo almacene en un variable y muestre por pantalla la frase
'tu indice de masa corporal es <imc> donde <imc> es el indice de masa corporal calculado redondeado
con dos decimales 

pR

'''


# peso = float(input("Escriba su peso : "))
# estatura = float(input("Escriba su estatura : "))
#
#
# imc =  round(peso /(estatura*estatura))
# print(f"tu indice de masa corporal es :  {imc:.2f}")


'''
Ejecicio 8 

Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla la <n>
entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los numeros introducidos por el 
usuario , y <c> y <r> son el cociente y el resto de la division entera respectivamente.

'''
#
# numero1 = float(input(" numero 1 :  "))
# numero2 = float(input(" numero 2 :  "))
#
# cociente = numero1 / numero2
# resto = numero1 % numero2
#
# print(f" el cociente  es {cociente:.4f} y el resto es : {resto} de la division")

'''

Ejercicio 9 

Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual, y 
el numero de años, y muestre por pantalla el capital obtenido en la inversion . 

pR

'''
#mi solucion pensando que los intereses se restan a la inversion final, segun mi logica pero
# pensandolo bien es una inversion , si invierte es para aumentar su inversion por lo tanto esta mal esta logica.

# cantidadInvertir = float(input("La cantidad a invertir : "))
# interesAnual = float(input("el interes anual : "))
# años = int(input("el numero de años : "))
#
# interesFinal = interesAnual * años
# totalInversion = ((cantidadInvertir*años) - interesFinal)
#
# print(f" su inversion es de : {totalInversion}")
#
# # #solucion 2 segun el ejercicio
# #
# capital = round(cantidadInvertir * (interesAnual / 100 + 1 ) ** años , 2 )
# print(f"\t solucion 2 \n el capital ganado es de : {capital} ")


'''
Ejercicio 10 

Una jugueteria tiene mucho exito en dos de sus productos : payasos y muñecas. Suele hacer venta 
por correo y la empresa de logistica le cobra por peso de cada paquete asi que deben calcular el 
peso de los payasos y muñecas que saldran en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75 g. 

Escribir un programa que lea el numero de payasos y muñecas vendidos en el ultimo pedido y calcule el peso total del 
paquete que sera enviado.


'''
# print("cantidades vendidas del ultimo año ")
# nPayasos = int(input("numero de payasos  : "))
# nMunecas = int(input("numero de muñecas  : "))
#
# pesoEnviar = ((nPayasos * 112) + (nMunecas * 75) )
#
# print(f"el peso del paquete final es de : {pesoEnviar}")

'''
Ejercicio 11

Imagina que acabas de abrir un nueva cuenta de ahorros que te ofrece el 4 %  de interes al año 
estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
de tu cuenta de ahorros. 

Escribir un programa que comience leyendo la cantidad de dinero depositado en la cuenta de ahorros, introducida por el 
usuario . Despues  el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer , segundo y tercer años
redondear cada cantidad a dos dicimales 

'''

# cuenta = float(input("cuanto va a  depositar en su cuenta : "))
#
# interes = 0.04
# inversionBase = cuenta * interes
#
# año1 = ((cuenta * interes) + cuenta)
# año2 = (año1 + inversionBase)
# año3 = (año2 + inversionBase)
# año4 = (año3 + inversionBase)
#
# print("> año 1",round(año1,2))
# print("> año 2",round(año2,2))
# print("> año 3 ",round(año3,2))
#
#
# print("solucion 2 , segun el ejerccio \n  ")
#
# balance1 = cuenta * (interes + 1)  # saca el porcentaje del 4% y se le suma a la cuenta
# balance2 = balance1 * (interes + 1)
# balance3 = balance2 * (interes + 1)
#
# print(f" 1 año : {round(balance1,2)}")
# print(f" 2 año : {round(balance2,2)}")
# print(f" 3 año : {round(balance3,2)}")
#
#
# print(f"interes de : {interes}")


'''
Ejercicio 12 

Una panaderia vende barras de pan a 3.49E cada una. El pan que no es el dia tiene un descuento 
del 60 % . 

Escribir un programa que comience leyendo el numero de barras de pan vendidas que no son del dia. 
Despues el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y coste final total. 

'''

# descuento = 0.60
# barrasVendidas = int(input("numero de barras de pan vendidas que no son  del dia  : "))
#
# # solucion segun mi logica
# totalBase = barrasVendidas * 3.49
# descuentoTotal = totalBase - (descuento * totalBase)
# descuentoIndivual = descuentoTotal / barrasVendidas
#
# #solucion segun el ejerccio
# # costo = barrasVendidas * 3.49 * ( 1 - descuento)
#
# # ambas soluciones dan el mismo resultado
#
#
# print(f" - Precio habitual del pan fresco : 3.49 euros ")
# print(f" - El costo por barra : {descuentoIndivual:.2f} euros sobre un descuento del 60 %   ")
# print(f" - El coste final  de las barras es : {descuentoTotal:.2f} euros ")
















