'''

    Escribir un programa que acceda a un fichero de internet mediante su url
    y muestre por pantalla el número de palabras que contiene.


'''
import requests

url = "https://www.gutenberg.org/files/11/11-0.txt"

response = requests.get(url , stream=True) #stream para cargar por partes

if response.status_code == 200:
    print("Éxito")

    cont = 0
    for cadena in response.iter_lines():

        cadena = cadena.decode("utf-8").split()
        cont += len(cadena)

    print("numero de palabras ", cont )

else:
    print("Fallo")

    # with open("archivoDescargado.txt", "w",  encoding="utf-8") as fichero:
    #     contenido = fichero.write(response.text)
    #
