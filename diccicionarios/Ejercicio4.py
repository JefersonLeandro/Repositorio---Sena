'''

    Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
    por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes>
    es el nombre del mes.


'''

diccionariosMeses = {"01":"Enero","02":"Febrero","03":"Marzo", "04":"Abril", "05":"Mayo", "06":"Junio", "07":"Julio" , "08":"Agosto"
    , "09":"septiembre", "10":"octubre",  "11":"Nomviembre",  "12":"diciembre"  }

print("Escriba una fecha con este formato dd/mm/aaaa : ")
fecha = input("fecha :   ")
print(f"Fecha \n El {fecha[ :-8 ] } de {diccionariosMeses[f"{fecha[ 3 :-5  ]}"]} de {fecha[ 6: ]}")


print("solucion segun el Ejercicio : ")
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha)
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])