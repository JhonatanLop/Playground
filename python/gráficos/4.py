from random import randint

lista_input = []

for i in range(150):
    lista_input.append(randint(0, 9))

print(f'lista_input: {lista_input}')


def algoritmo (numeros):
    seq_count_A = 0
    seq_sum_A = 0
    max_seq_count_A = 0
    max_seq_sum_A = 0

    seq_count_B = 0
    seq_val_B = 0
    max_seq_count_B = 0
    max_seq_val_B = 0

    prev = 0

    for num in numeros:
        
        # verifica se o numero está em sequencia
        if num > prev:

            # conta a sequencia
            seq_count_A += 1

            # soma o numero
            seq_sum_A += num

        # não está em sequencia
        else:

            # reseta a sequencia pra 1 
            seq_count_A = 1
            
            # reseta a soma pra num
            seq_sum_A = num
        
        # verifica se a sequencia atual supera a maxima encontrada ate o momento
        if seq_count_A > max_seq_count_A or (seq_count_A == max_seq_count_A and seq_sum_A > max_seq_sum_A):
            max_seq_count_A = seq_count_A
            max_seq_sum_A = seq_sum_A

        
        # verifica se o numero está em sequencia
        if num == prev:

            # conta a sequencia
            seq_count_B += 1

            # soma o numero
            seq_val_B = num

        # não está em sequencia
        else:
            seq_count_B = 1
            seq_val_B = num
        if seq_count_B > max_seq_count_B or (seq_count_B == max_seq_count_B and seq_val_B > max_seq_val_B):
            max_seq_count_B = seq_count_B
            max_seq_val_B = seq_val_B

        prev = num


    print(f'sequencia A: {max_seq_count_A} | sum: {max_seq_sum_A}')
    print(f'sequencia B: {max_seq_count_B} | val: {max_seq_val_B}')

algoritmo(lista_input)

