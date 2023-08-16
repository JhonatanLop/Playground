# importa biblioteca matplotlib
import matplotlib.pyplot

# dando valores que irão alimentar o gráfico
meses = ['índice 1', 'índice 2', 'índice 3', 'índice 4']
valores = [150,400,250,250]
dias = [300,250,123,342]

# dizendo à função, usando o método plot quais parâmetros ele deve usar
matplotlib.pyplot.plot(meses,valores,dias)

# gerar e mostrar o gráfico
matplotlib.pyplot.show()