#modo binario
# "b": Modo binario. Se utiliza junto con los modos anteriores para indicar que
# el fichero se abrirá en modo binario, útil para trabajar con ficheros binarios en lugar de ficheros de texto.

fichero = open("datos.bin" , "wb")

cadena = b'hola esto es un mensaje en binario'

Escribir = fichero.write(cadena)
fichero.close()