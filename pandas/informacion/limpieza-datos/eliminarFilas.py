import  pandas as pd
#eliminar datos nulos

leer = pd.read_csv("../archivos/acondicionamiento-fisico.csv")
print(leer)
nuevosDatos  = leer.dropna()# elimina y retonar los datos para ser guardados en una variable sin modificar el datos en la ejecucion
leer.dropna(inplace=True) # Modifica los datos durante la ejecución en memoria, pero no devuelve un nuevo DataFrame y no el archivo original.


print(nuevosDatos)