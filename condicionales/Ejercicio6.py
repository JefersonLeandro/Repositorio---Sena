'''
los Alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con nombre anterior a la M y los hombres con un nombre posterior
a la N y el grupo B por el resto.

Escribir un programa que pregunte al usuario su nombre y sexo , y muestre por pantalla el grupo
que le corresponde.


'''
'''
    grupo A = ( a, b, c , d , e, f, g , h , i , j ,k , l  ) m -mujeres 
    grupo A = n ( o, p , q , r, s, t u , v, w , x , y , z ) -hombres
    grupo B = (n , m)
    
'''

nombre = input("Escriba su nombre : ").lower()
sexo = input("Escriba su sexo : ").lower()




if nombre < 'm' and (sexo == 'femenino' or sexo == 'f'):
    # mejures
    print("tu nombre es anterior a la M \n")
    print(f"perteneces al GRUPO A - MUJERES")
elif nombre > 'n' and (sexo == 'masculino' or sexo == 'm') :
    # hombres
    print(f"tu nombre es posterior ")
    print("perteneces al GRUPO A - HOMBRES ")
else:
    print("perteneces al GRUPO B")