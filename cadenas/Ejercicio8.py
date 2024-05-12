'''

    Escribir un programa que pregunte por consola el precio de un producto
    en euros con dos decimales y muestre por pantalla el numero de euros y el
    numero de centimos del precio introducido
'''


precio = input("Escriba el precio del producto : ")



print(f"Euros : {precio[:precio.find(".")]} \n" f"precio en centimos  : {precio[precio.find(".")+1:]}")



