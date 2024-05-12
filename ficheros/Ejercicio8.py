'''
    El fichero calificaciones.csv contiene las calificaciones de un curso.
    Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
    Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la
    al final del curso (convocatoria ordinaria).

    Escribir un programa que contenga las siguientes funciones:

    1.Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios,
    donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno.
    La lista tiene que estar ordenada por apellidos.

    2.Una función que reciba una lista de diccionarios como la que devuelve la función anterior
    y añada a cada diccionario un nuevo par con la nota final del curso.
    El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

    3.Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva
    dos listas, una con los alumnos aprobados y otra con los alumnos suspensos.
    Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes
    parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.


    analisis
    -2 examenes de TEORIA y 1 de  PRACTICAS
    -las calicaciones menos 4 se les dio la posibilidad de repetir el examen al final del curso
     (convocatoria ordinaria)
    -nota final del curso , peso de cada parcial de teoria en lo nota final -> 30% , peso del examen de practicas 40%

    -las asitencias son trismetrales equivalente a 66 dias de estudio y 90 dias de dias en total

    Tareas
    -

    codiciones para aprobar el curso

    -la asistecia debe ser mayor o igual al 75 %
    -notas de examanes parciales y de practicas debe ser mayor o igual que 4
    -la nota final mayor o igual que 5

'''

def calicaciones():

    with open("calificaciones.csv", "r") as fichero:
        contenido = fichero.read()

        lista = []
        separacion = contenido.split("\n")
        encabezado = separacion[0].split(",")

        tamanoEncabezado= len(encabezado)

        for i in range(1,len(contenido.split("\n"))):
            datos = separacion[i].split(",")

            diccionario = {}
            for j in range(tamanoEncabezado):

                 diccionario[encabezado[j]] = datos[j]

            lista.append(diccionario)

        return lista


def procesarCalicaciones():

    lista = calicaciones()

    for items in lista:

        examen1 = float( items["examen1"]) #30%
        examen2 = float(items["examen2"])#30%
        practica =float( items["practica"])#40%

        notaFinal = round( ((examen1+examen2) * 0.30) + (practica * 0.40) , 2 )
        items["notaFinal"] = notaFinal
        print(items)
    return lista



def evaluar():

    lista = procesarCalicaciones()
    aprobados = []
    suspensos = []

    #asistencia trimestral
    diasFestivos = 24
    diasTotales = 90
    asistenciaMinima = int( (diasTotales - diasFestivos ) * 0.75)

    for items in lista:

        asistencia = int(items["asistencia"])
        examen1 = float(items["examen1"])
        examen2 = float(items["examen2"])
        practica = float(items["practica"])
        notaFinal  = items["notaFinal"]

        if asistencia >= asistenciaMinima and examen1 >= 4 and examen2 >= 4 and practica >= 4 and notaFinal >= 5:
            aprobados.append(items["apellido"])
        else:
            suspensos.append(items["apellido"])


    print("alumnos aprobados : ",aprobados,"\n alumnos suspensos : ", suspensos)

    return  aprobados,suspensos

evaluar()