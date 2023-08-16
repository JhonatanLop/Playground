import numpy as np
import  matplotlib.pyplot as  plt 

# Grupos |1|2|3|4|5|    --> são 5 requisitos
grupo1 = [4,3,5,4,2]   #--> grupos
grupo2 = [5,4,3,4,5]
grupo3 = [4,2,4,5,4]
grupo4 = [2,3,4,5,3]

# criando uma lista para acumular as médias que será usado para gerar uma linha no código de barras
soma =[0] * 5

# um contador de 0 até o número número máximo de requisitos:
for i in range(0,len(grupo1)):
#   no índice 0 da lista soma: somar todos os índeces zeros das outras listas(grupos) e dividir pela quantidade de grupos
    soma[i] += (grupo1[i] + grupo2[i] + grupo3[i] + grupo4[i]) / 4 

# Define a expessura da barra
barWidth = 0.2
# Defini a ampliação do grafico
plt.figure(figsize=(10,5))

# Aqui eu estou definindo a posição de cada barra no grafico
# Não me pergunte como funciona, eu não sei... mas se você souber pode me dizer kkk
r1 = np.arange(len(grupo1))
r2 = [x + 0.02 + barWidth for x in r1]
r3 = [x + 0.02 + barWidth for x in r2]
r4 = [x + 0.02 + barWidth for x in r3]

#Aqui eu construo a barra
plt.bar(r1, grupo1, color='#fce8e8', width=barWidth, label="grupo 1")
plt.bar(r2, grupo2, color='#f6c6c6', width=barWidth, label="grupo 2")
plt.bar(r3, grupo3, color='#e6adad', width=barWidth, label="grupo 3")
plt.bar(r4, grupo4, color='#0f210d', width=barWidth, label="grupo 4")

# Construindo a linha 
ypoints = np.array(soma)

plt.xlabel('Críterio avaliativo')
plt.xticks( [r + barWidth for r in range(len(grupo1))],['TG','PO','KE', 'PT', 'QU'])
plt.ylabel("Notas")
plt.title('Sprint 1')

# plt.plot(xpoints)
plt.plot(ypoints, marker = 'o')
plt.legend()
plt.show()