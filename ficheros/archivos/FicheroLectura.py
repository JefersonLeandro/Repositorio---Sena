
# modo lectura
# "r": Modo de lectura. Abre el fichero para leer. Si el fichero no existe, se producirá un error.

fichero = open("ejemplo.txt", "r")

contenido = fichero.read()

print(contenido)

fichero.close()
