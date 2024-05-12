'''

    El fichero titanic.csv contiene información sobre los pasajeros del Titanic.

    Escribir un programa con los siguientes requisitos:

    -Generar un DataFrame con los datos del fichero.

    -Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
     los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.

    -Mostrar por pantalla los datos del pasajero con identificador 148.

    -Mostrar por pantalla las filas pares del DataFrame.

    -Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.

    -Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.

    -Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

    -Eliminar del DataFrame los pasajeros con edad desconocida.

    -Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

    -Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.

    -Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.


'''

import pandas as pd


#Generar un DataFrame con los datos del fichero.

datos = pd.read_csv("../informacion/archivos/titanic.csv")

df = pd.DataFrame(datos)

df.set_index('PassengerId', inplace=True)
print(df)
#Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene,
#los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.

print("------------------")
print("Informacion basica")
print("------------------")
df.info()

print("------------------")
print("-10 primeras filas")
print("------------------")
head = df.head(10)#primeras 10 filas
print("---------")
print(head.to_string())

print("------------------")
print("-10 ultimas filas")
print("------------------")
tail = df.tail(10)
print(tail.to_string())

#Mostrar por pantalla los datos del pasajero con identificador 148.
print("------------------")
print("-Pasajero 148 ")
print("------------------")
pasejero148 = df.loc[148]
print(pasejero148)

#Mostrar por pantalla las filas pares del DataFrame.
print("------------------")
print("-filas pares ")
print("------------------")
filasPares = df[df.index % 2 == 0]
print(filasPares)

#Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print("------------------")
print("-Nombres clase 1  ")
print("------------------")
nombres= df[['Name','Pclass']].sort_values(by='Name')#ordenar por orden alfabetico
resultado= nombres[nombres['Pclass'] == 1]
print(resultado)


#Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print("------------------")
print("-Porcentajes  ")
print("------------------")
print("-----Sobrevivientes------")

sobrevivientes = df['Survived']
totalSobrevivientes = sobrevivientes[df['Survived'] == 1].sum()
totalMuertos = sobrevivientes[df['Survived'] == 0].count()
totalPersonas = df['Survived'].count()
print(f"numero - {totalSobrevivientes}")
print(round((totalSobrevivientes/totalPersonas)*100 , 2), "%")

print("-----No sobrevivientes------")
print(f"numero - {totalMuertos}")
print(round((totalMuertos/totalPersonas)*100, 2, ), "%")


#Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.

# 1,2,3
clases = df['Pclass']
sobrevivientes = df['Survived'] == 1

print(sobrevivientes)
sobrevivientesClase1 = sobrevivientes[(df['Pclass'] == 1)].sum()
sobrevivientesClase2 = sobrevivientes[(df['Pclass'] == 2)].sum()
sobrevivientesClase3 = sobrevivientes[(df['Pclass'] == 3)].sum()

ntotalClase1 = clases[clases == 1].count()
ntotalClase2 = clases[clases == 2].count()
ntotalClase3 = clases[clases == 3].count()

print(" Porcentajes de sobrevivientes de la clase 1 : ", round(sobrevivientesClase1/ntotalClase1 , 2)*100 , "%")
print(" Porcentajes de sobrevivientes de la clase 2 : ", round(sobrevivientesClase2/ntotalClase2 , 2)*100, "%")
print(" Porcentajes de sobrevivientes de la clase 3 : ", round(sobrevivientesClase3/ntotalClase3 , 2)*100, "%")



#Eliminar del DataFrame los pasajeros con edad desconocida.

print("edad sin datos vacios")

df.dropna(subset=['Age'] , inplace=True)

print(df.to_string())


#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.

# sexo -> female , edad promedio en cada clase 1, 2, 3
# mujeres de la clase 1

print("Promedio de edades de mujeres de cada clase ")
mujeres = df[df['Sex'] == 'female']

promedios = {}
for i in range(1, 4):

    clase = mujeres[mujeres['Pclass'] == i]
    media = int(clase['Age'].mean())
    print(f" Media de la clase ({i}) : {media} años")
    promedios[i] = media


#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
print("nueva columna booleana segun la edad\n")
df['menorEdad'] = df['Age'] < 18

print(df.to_string())

#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.

    #porcentajes de sobrevivientes de menores y mayores de edad en cada clase
print("\n porcentajes")



menores = df['menorEdad']
sobrevivientes = df['Survived'] == 1

menoresEdad = df[(menores == True) & (sobrevivientes)]
mayoresEdad = df[(menores == False) & (sobrevivientes)]

    #total personas de cada clase

clasificarMenores = df[menores == True]
clasificarMayores = df[menores == False]

diccionarioTotalesMenores = {}
diccionarioTotalesMayores = {}

for i in range(1, 4):

    totalPersonasMenores = clasificarMenores[clasificarMenores['Pclass'] == i]['Survived'].count()
    diccionarioTotalesMenores[i] =  totalPersonasMenores

    totalPersonasMayores = clasificarMayores[clasificarMayores['Pclass'] == i]['Survived'].count()
    diccionarioTotalesMayores[i] =  totalPersonasMayores

print("personas totales")
print(diccionarioTotalesMenores)
print(diccionarioTotalesMayores)



porcentajesMenores = {}
porcentajesMayores = {}

print("porcentajes de los sobrevientes por clase \n")

for i in range(1, 4):


    sobrevivientesMenores = menoresEdad[menoresEdad['Pclass'] == i]
    porcentajeMenores = round( (sobrevivientesMenores['Survived'].count()) / diccionarioTotalesMenores[i],2 ) * 100

    porcentajesMenores[i] = {porcentajeMenores}
    print(f"clase ({i}) Menores ",round(porcentajeMenores,2),"%")

    sobrevivientesMayores = mayoresEdad[mayoresEdad['Pclass'] == i]
    porcentajeMayores = round((sobrevivientesMayores['Survived'].count()) / diccionarioTotalesMayores[i] , 2) * 100

    porcentajesMayores[i] = {porcentajeMayores}
    print(f"clase ({i}) Mayores ", porcentajeMayores, "%")

print(porcentajesMenores)
print(porcentajesMayores)

#se pudo haber hecho con gropuby para simplificar todoo pero por falta de conocimiento se desconocia dicho metodo.







