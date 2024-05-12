'''
    maximo comun divisor -  el numero mayor que se repite segun sus multiplos
'''

# Este algorimo esta creado a mi manera es funcional pero no es recomendable utilizarlo existen mejores maneras de hacerlo
# como por ejemplo el metodo de euclides que es mas eficiente. {
def maximoComundivisor(n1, n2):

    if n1 >= n2:
        mayor = divisores(n1)
        menor = divisores(n2)
    else:
        mayor = divisores(n2)
        menor = divisores(n1)

    mayorTemporal = 0
    mcd = 0
    for n in mayor:
        print(n)
        for j in menor:

            if j > mayorTemporal:
                mayorTemporal = j
                if mayorTemporal in mayor:
                    mcd = mayorTemporal

            print(j)
        print("---------")

    return mayor,"--",menor, "---nf ", mcd


def divisores(numero):

    divisores = []
    for n in range(1, numero+1):
        if numero % n == 0 :
            # es divisible por ese numero
            divisores.append(n)

    return divisores

print(maximoComundivisor(120, 156))
# }

