'''

    Detectar y corregir los errores del siguiente programa que devuelve y elimina el teléfono
    de un listín telefónico a través del nombre del usuario:

    listin = {'Juan':123456789, 'Pedro':987654321}

    def elimina(listin, usuario):
        del listin[usuario]
        return listin[usuario]

    print(elimina(listin, 'Pablo'))


'''

listin = {'Juan': 123456789, 'Pedro': 987654321}


def elimina(listin, usuario):

    if usuario in listin:
        for persona in listin:

            if persona == usuario:
                # del(listin[usuario])
                listin[usuario] = ""
                break

        print(listin)
        return usuario
    else:
        print("usuario no encontrado")

print(elimina(listin, 'Pedro'))