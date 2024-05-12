'''

La pizzeria Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuacion.
-Ingredientes vegetarianos: pimiento y tofu
-Ingredientes no vegetarianos: peperoni, jamon y salmon.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no , y en funcion de su respuesta
le muestre un menu con los ingredientes disponibles para que elija . solo se puede eligir un ingrediente ademas
de la mozzarella y el tomate que estan en todas las pizzas. Al final se debe msotrar por pantalla si la pizza elegida es vegetariana
o no y todos los ingredientes que lleva.

'''

print("PIZZERIA BELLA NAPOLI")
vegetariana = input("Quiere una pizza vegetariana (si o no)  :  ").lower()
extra = "mozzarella , tomate"
if vegetariana == "si":
# vegetariana
    print("\t---Menu vegetariano -- \n1- pimiento\n2- tofu ")
    opcion = int(input("opcion aqui : "))
    if opcion == 1:
        ingredientes = "pimiento, "+extra
        print(f"tu pizza es vegetariana con los siguientes ingredientes : {ingredientes}")
    elif opcion == 2:
        ingredientes = "tofu, "+extra
        print(f"tu pizza es vegetariana con los siguientes ingredientes : {ingredientes}")
    else:
        print("Opcion erronea vuelve a intentarlo")
elif vegetariana == "no":
    # no vegetariana
    print("\t---Menu no vegetariano -- \n1- peperoni \n2- jamon\n3-salmon ")
    opcion = int(input("opcion aqui : "))
    if opcion == 1:
        ingredientes = "peperoni, " + extra
        print(f"tu pizza es no  vegetariana con los siguientes ingredientes : {ingredientes}")
    elif opcion == 2:
        ingredientes = "jamon, " + extra
        print(f"tu pizza es no vegetariana con los siguientes ingredientes : {ingredientes}")
    elif opcion == 3:
        ingredientes = "salmon, " + extra
        print(f"tu pizza es no vegetariana con los siguientes ingredientes : {ingredientes}")
    else:
        print("Opcion erronea vuelve a intentarlo")
else:
    print("vuelve a intentarlo")