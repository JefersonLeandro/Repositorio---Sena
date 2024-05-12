import pandas as pd

#metodo unidimensional representado por una sola columna

data = ["a","b","c","d","e","f","g"]

print(pd.Series(data))
print("----------")

labels = {"-a" : "ei","-b": "bi","-c" : "ci","-d":"di","-e":"i","-f":"ef","-g":"yi"}

m = pd.Series(labels, index=["-a", "-d"])
print(m)