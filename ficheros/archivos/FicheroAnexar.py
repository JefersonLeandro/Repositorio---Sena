#modo anexar
# "a": Modo de anexar. Abre el fichero para escribir. Si el fichero no existe, se crea. Si el fichero ya existe, se posiciona al final y comienza a escribir desde ahí, sin truncar el contenido existente.

fichero = open("ejemplo.txt", "a")

fichero.write("este texto se agregara al txt ejemplo ")

fichero.close()

