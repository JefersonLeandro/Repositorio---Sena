'''

    Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
    {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos
    de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura>
    es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
    también el número total de créditos del curso.

'''


diccionariosAsignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

totalCreditos = 0
for asignatura in diccionariosAsignaturas:
    totalCreditos += diccionariosAsignaturas[f"{asignatura}"]
    print(f"{asignatura} tiene {diccionariosAsignaturas[f"{asignatura}"]} creditos" )


print(f" El total de creditos es : {totalCreditos}")

print("solucion segun el ejercicio : ")

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)