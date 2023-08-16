import numpy as np
import  matplotlib.pyplot as  plt 

ti1id1 = [4,3,5,4,2]
ti1id2 = [5,4,3,4,5]
ti1id3 = [4,2,4,5,4]
ti1id4 = [2,3,4,5,3]

soma = [0] * 5

for i in range(0,len(ti1id1)):
    print (i)
    soma[i] += (ti1id1[i] + ti1id2[i] + ti1id3[i] + ti1id4[i]) /len(ti1id1)
    print(soma)

#Define a expessura da barra
barWidth = 0.2
#Defini a ampliação do grafico
plt.figure(figsize=(10,5))

#Aqui eu estou definindo a posição de cada barra no grafico
r1 = np.arange(len(ti1id1))
r2 = [x + 0.02 + barWidth for x in r1]
r3 = [x + 0.02 + barWidth for x in r2]
r4 = [x + 0.02 + barWidth for x in r3]

#Aqui eu construo a barra
plt.bar(r1, ti1id1, color='red', width=barWidth, label="grupo 1")
plt.bar(r2, ti1id2, color='green', width=barWidth, label="grupo 2")
plt.bar(r3, ti1id3, color='blue', width=barWidth, label="grupo 3")
plt.bar(r4, ti1id4, color='pink', width=barWidth, label="grupo 4")

# Construindo a linha 
ypoints = np.array(soma)

plt.xlabel('Críterio avaliativo')
plt.xticks( [r + barWidth for r in range(len(ti1id1))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Notas")
plt.title('Sprint 1')

# plt.plot(xpoints)
plt.plot(ypoints, marker = 'o')
plt.legend()
plt.show()
