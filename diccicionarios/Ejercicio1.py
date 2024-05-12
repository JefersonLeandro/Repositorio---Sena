'''

Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa
no está en el diccionario.


'''

diccionarioDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa =  input("Escriba una divisa : ").title()

if divisa in diccionarioDivisas :
  print(diccionarioDivisas[divisa])
else:
    print("la divisa escrita no se encuentra en el registro")