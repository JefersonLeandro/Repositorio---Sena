# modo automatico con with
# es un modo diferente para abrir un fichero
# este se cierra automaticamente y evita hacerlo manual

# as es un alias

with open("datos.bin" , "rb") as ficheroLectura :

    leer = ficheroLectura.read()

    print(leer)
