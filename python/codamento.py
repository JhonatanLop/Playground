# # declaração de variáveis
# num_alunos = int(input("digite o número de alunos"))
# lista_notas = []
# soma = 0

# # contador de 0 até número de alunos:
# for i in range(0, num_alunos):
#     # adiciona nota a uma lista de notas atravéz d eum input float
#     lista_notas.append(float(input(f"digite a nota {i+1}: ")))
#     # acumula a soma das notas 
#     soma += lista_notas[i]

# media = soma / num_alunos
# print(media)

# acima_media = []
# for i in range(0, num_alunos):
#     if lista_notas[i] >= media:
#         acima_media.append(lista_notas[i])

# print(acima_media)

import time

start_time = time.time()

# Faça alguma coisa que demore um tempo...
time.sleep(5)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)  # imprime 5.0