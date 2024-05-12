'''

    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
    Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha
    sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
    has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
    cada una de las correspondientes notas introducidas por el usuario.


'''

listaAsignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

print("solucion 1 ")
listaMaterias = []
for asignatura in listaAsignaturas:
    nota = float(input(f"Escriba la nota de  {asignatura} :  "))
    listaMaterias.append(f"En {asignatura} has sacado {nota}")
print("++++++++++NOTAS++++++++++")

for materia in listaMaterias:
    print(materia)

print("solucion 2 ")

listaNotas = []
for asignatura in listaAsignaturas:
    nota = float(input(f"Escriba la nota de  {asignatura} :  "))
    listaNotas.append(nota)


cont = len(listaAsignaturas)
listaAsignaturas.reverse()
listaNotas.reverse()

print("-----------NOTAS-----------------")
while cont != 0:
    print(f"En {listaAsignaturas[(cont-1)]} has sacado {listaNotas[cont-1]} ")
    cont-=1

print("\nsolucion segun el ejercicio ")

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

