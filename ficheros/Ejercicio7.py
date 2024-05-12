'''

    El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:
    Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa),
    Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada),
    Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

    1.Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos
     del fichero por columnas.

    2.Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero
    en formato csv con el mínimo, el máximo y la media de dada columna.


'''


def devolverContizaciones():

    with open("cotizacion.csv", "r") as fichero:

        contenido = fichero.read()

        diccionario = {}
        separacion = contenido.split("\n")#separacion por salto linea
        encabezado = separacion[0].split(",")# nombres de columnas

        for i in range(1, len(separacion)):
            empresa = {}
            datosEmpresa = separacion[i].split(",")  # características separadas de una empresa

            for j in range(len(encabezado)):

                empresa[encabezado[j]] = datosEmpresa[j] # Asinacion de cada item a cada caracteristica

            diccionario[i - 1] = empresa

        return diccionario


def crear():

    minimos = []
    maximos = []
    efectivos = []
    media = 0

    diccionario = devolverContizaciones()
    for clave, valor in diccionario.items():

        minimos.append(float(valor["Minimo"]))
        maximos.append(float(valor["Maximo"]))
        efectivos.append(float(valor["Efectivo"]))


        print("maximo : ",valor["Maximo"])


        print(f"clave : {clave} y valor : {valor} ")

    print(diccionario)
    with open("resultado-cotizacion.csv" , "a" ) as fichero:
        fichero.write(f"Minimo : {min(minimos)}\n")
        fichero.write(f"Maximo : {max(maximos)}\n")
        fichero.write(f"media efetivos : {round(sum(efectivos)/len(efectivos),3)}\n")







































    print("efetivos ", efectivos)


crear()