from matplotlib import pyplot as plt 
import numpy as np 
  
cars = ["Pessoas não Avaliadas", " pessoas Avaliadas"]
id_integrante = [1,2,3,2,4,5,3,2,4]

indice = 0
data = []

for indice, objeto in enumerate(id_integrante):
    if id_integrantes_avaliados[objeto] == id_integrante[objeto]:
        data[indice] = objeto
        print(indice, objeto)

fig = plt.figure(figsize =(5, 5))

plt.pie(data, labels = cars) 
plt.legend()
plt.show()