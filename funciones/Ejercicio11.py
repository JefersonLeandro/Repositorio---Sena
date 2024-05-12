'''

    Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
    que contiene y su frecuencia.

    Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla
    con la palabra más repetida y su frecuencia.

    cadena = Hola mundo!
    Frecuencia de caracteres en 'Hola mundo!':

      H: 1
      o: 2
      l: 1
      a: 1
      : 1
      m: 1
      u: 1
      n: 1
      d: 1
      !: 1


'''
def frecuencia(cadena):

    diccionario = {}
    for i in cadena:
        cont = 0
        for j  in cadena:
            if j == i:
                cont += 1

        diccionario[f"{i}"] = cont

    print("version 1 --> valor repetido ",valorRepetido(diccionario))
    print("version 2 --> valor repetido ",valorRepetidoVersion2(diccionario))

    return diccionario


def valorRepetido(diccionario):

    verificacion = True

    for clave , valor_i in diccionario.items():

        verificacion = False
        for valor_j in diccionario.values():
            if valor_i < valor_j:
                    verificacion = True

        if not verificacion:
            tupla = (f"{clave}", valor_i)
            return tupla
    return "------", verificacion



def valorRepetidoVersion2(diccionario):
    valormaximo = max(diccionario.values())

    for clave , valor in diccionario.items():
        if valor == valormaximo:
            tupla = (f" {clave} - {valor}")
            return tupla
    return tupla





print(frecuencia('Hola mundo!'))
print(frecuencia('cabeza rodilla muslos cadera'))
print(frecuencia('ohhh por dioss!'))

