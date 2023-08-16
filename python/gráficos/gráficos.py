# importando matplitlib
import matplotlib.pyplot as plt

# declarando as listas com os valores que serão usados no gráfico
meses = ["janeiro", "fevereiro", "março", "abrio", "maio", "junho"]
valores = [32131,64516,31321,43155,65435,37621]
valores2 = [45322, 74562, 36624, 78421, 30154, 45321]

# titulo do gráfico
plt.title("Primeiro gráfico")

# adicionando labels no eixo x e y
plt.xlabel("valores postos")
plt.ylabel("meses postos")

# inicializando a tela com o gráfico
plt.plot(meses, valores, valores2)
plt.show()