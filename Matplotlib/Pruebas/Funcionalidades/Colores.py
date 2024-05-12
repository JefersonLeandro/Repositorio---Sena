
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


crecimiento2023 = {'JavaScript': 29.80, 'python' : 19.64, 'Java' : 17.78, 'C#':12.21,'Php': 9.39,'C/C++' : 9.14, 'Sql' : 1.73     }
ax.bar(crecimiento2023.keys(),crecimiento2023.values(), color = "purple",marker="o")

plt.title("Crecimiento de \n 1 de enero 2022 a 31 de mayo 2023")
plt.ylabel("Porcentajes")
plt.xlabel("Lenguajes")

plt.show()