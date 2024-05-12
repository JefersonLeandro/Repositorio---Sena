'''

    Escribir una función que reciba otra función y una lista, y devuelva otra
    lista con el resultado de aplicar la función dada a cada uno de los
    elementos de la lista.

'''

#realize una funcion de pares e impares para hallar numero total  de pares o impares segun su suma pero pues no aplice un funcion a cada elemento

def paresEimpares(lista, opcion):
    #pares hasta n
    print("---",opcion,"---")
    numeroTotal = sum(lista)
    nuevaLista =[]
    for n in range(numeroTotal+1):
        if opcion == "pares":
            if n % 2 == 0:
                nuevaLista.append(n)
        else:
            if n % 2 != 0:
                nuevaLista.append(n)
    return nuevaLista

def funcion(lista, funcion):

    resultado = paresEimpares(lista, funcion)

    return  resultado
print(funcion([1, 2,3,4,5 ] , "pares"))
print(funcion([1, 2,3,4,5 ] , "impares"))
