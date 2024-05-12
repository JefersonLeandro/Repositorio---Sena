'''
En una determinada empresa , sus empleados son evaluados al final de cada año .
Los puntos que pueden obtener en la evaluacion comienzan en 0.0 y pueden ir aumentando,
traduciendose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden
ser 0.0, 0.4, 0.6 o mas , pero no valores intermedios entre las cifras mencionadas . A continuacion
se muestra una tabla con los niveles correspondientes a cada puntuacion. la cantidad de dinero
conseguida en cada nivel es de 2.400 euros multiplicada por la puntuacion del nivel

nivel       - puntuacion
inaceptable - 0.0
Aceptable   - 0.4
Meritorio   - 0.6 o mas

Escribir un programa que lea la puntuacion del usuario e indique su nivel de rendimiento, asi
como la cantidad de dinero que recibira el usuario.

'''
dineroBase = 2400
nivel = "Anaceptable"
puntuacion = float(input("Escriba su puntuacion : "))


if puntuacion == 0.0 :
    print(f"su nivel de rendiento es : {nivel} \n  por lo tanto usted no tiene bonificacion")

elif puntuacion == 0.4:
    nivel = "Aceptable"
    dineroBase *= puntuacion
    print(f"su nivel de rendiento es : {nivel} \nsu bonificacion es de : {dineroBase:.2f}")

elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dineroBase *= puntuacion
    print(f"su nivel de rendiento es : {nivel} \nsu bonificacion es de : {dineroBase:.2f}")

else:
    print("digite una puntuacion dentro de los rangos ")




















