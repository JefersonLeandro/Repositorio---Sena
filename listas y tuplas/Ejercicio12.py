'''

    Escribir un programa que almacene las matrices


    A = (  1  2 3 )    y  B = ( -1  0 )
        (  4  5 6 )           (  0  1 )
                              (  1  1 )

    en una lista y muestre por pantalla su producto.
    Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.


'''

print("Nota : El ejercicio propuesto es diferente al de la solucion   ")
print("solucion separadas : ")
listaA = [1,2,3,4,5,6]
listaB = [-1,0,1,0,1,1]
productoListas = []
suma = 0

for i in range(len(listaA)):
    suma += listaA[i] * listaB[i]
    productoListas.append(listaA[i]* listaB[i])

print("producto final : ",suma)
print(f"todos los productos : {productoListas}")

print("\nsolucion unidas :")

lista = [1,2,3,4,5,6,-1,0,1,0,1,1]
indice = 6
producto  = 0
resultadosP = []

for i in range(indice):
    producto += lista[i] * lista[indice + i]
    resultadosP.append(lista[i] * lista[indice + i])

print(f"el producto final es : {producto}")
print(f"todos los productos son : {resultadosP} ")

