'''

    Escribir una función que reciba una serie de Pandas con el número de ventas de un producto
    durante los meses de un trimestre y un título y cree un diagrama de sectores con las ventas en
    formato png con el titulo dado.

    El diagrama debe guardarse en un fichero con formato png y el título dado.

'''
import pandas as pd
import matplotlib.pyplot as plt

meses = ['Abril','Mayo', 'Junio']
datos = [50, 120, 80]
serie = pd.Series(datos)

def registroVentas(serie, titulo):

    fig, ax = plt.subplots()

    ax.pie(serie, labels=meses, autopct='%1.1f%%') # autopct mostrar porcentajes con formato de un decimal
    plt.title("Ventas de empanadas")
    plt.savefig(f'../Pruebas/Imagenes/{titulo}.png')
    plt.show()

registroVentas(serie, "Registro de ventas")
#autopct='%1.1f%%'
# significa que se mostrará un número flotante con un dígito en la parte entera y un dígito en la parte decimal.
