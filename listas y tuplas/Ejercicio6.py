'''

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura y elimine de la lista las asignaturas aprobadas.

Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

----------
-pop() elimina por posicion

'''


listaAsignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

cont = 0
for j in range(len(listaAsignaturas)):
    nota = float(input(f"En {listaAsignaturas[j-cont]} cuanto ha sacado : "))
    if nota >= 3.5: # solo las aprobadas
        listaAsignaturas.pop(j - cont) #elimina restandole ya las posiciones eliminadas de lo contrario eliminara una posicion equivocada
        cont += 1

if cont != 5  :
    print("debes repetir las siguientes asignaturas : ")
    for asignatura in listaAsignaturas:
        print(f"- {asignatura} ")
else:
    print("no debes repetir ninguna asignatura  ")

