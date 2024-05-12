import pandas as pd
#lee las ultimas lineas de los datos
leer = pd.read_json("../archivos/data.json")




print(leer.tail()) # 5 ultimas filas
print(leer.tail(10)) # 10 ultimas filas

