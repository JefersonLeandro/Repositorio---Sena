'''

    Ejercicio 2
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo
    Matematicas , Fisica , Quimica, Historia y Lengua ) en una lista y la muestre por pantalla el
    mensaje 'yo estudio <asignatura>' donde <asignatura> es cada una de las asignaturas de la
    lista


'''
listaAsignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

# solucion 1
print("for : ")
for i in listaAsignaturas:
    print(f"yo estudio ' {i}'")

# solucion 2
print("\n solucion 2 : ")
print(f"yo estudio ' {listaAsignaturas[0]}'")
print(f"yo estudio ' {listaAsignaturas[1]}'")
print(f"yo estudio ' {listaAsignaturas[2]}'")
print(f"yo estudio ' {listaAsignaturas[3]}'")
print(f"yo estudio ' {listaAsignaturas[4]}'")

