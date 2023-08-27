lista = [1,2,3,4,5]
indice = 4

def print_recursivo (indice, lista):
    if indice >= 0:
        print(lista[indice])
        print_recursivo(indice-1, lista)

# print_recursivo(indice, lista)

#Fatorial: Calculando o fatorial de um número usando recursão.
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    if numero != 0:
        print(numero)
        return numero * calcular_fatorial(numero - 1)
# print(calcular_fatorial(10))

#Soma de Números: Calculando a soma dos primeiros N números inteiros usando recursão.
def soma_n(num):
    if num == 0:
        return 0
    else:
        print
        return num + soma_n(num-1)
# print(soma_n(10))

#Sequência de Fibonacci: Calculando o termo N da sequência de Fibonacci usando recursão.
# 0 1 1 2 3 5 8 13
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(7))

#Escreva uma função recursiva para calcular a potência de um número, ou seja, base^expoente.

def potencia(b, e):
    soma = 0
    if e == 1:
        return b
    else:
        soma = b * potencia(b, e - 1)
        return soma

# print(potencia(2, 4))

# Crie uma função recursiva para inverter uma string. Por exemplo, se a entrada for "python", a saída deve ser "nohtyp".

# Escreva uma função recursiva para calcular o MDC (Máximo Divisor Comum) de dois números inteiros.

# Implemente uma função recursiva para gerar todos os subconjuntos de um conjunto dado. Por exemplo, se a entrada for {1, 2, 3}, a saída deve ser {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}.

# Crie uma função recursiva para verificar se uma palavra é um palíndromo (ou seja, lê-se da mesma forma da esquerda para a direita e da direita para a esquerda).

# Implemente uma função recursiva para calcular o N-ésimo termo da sequência de números de Catalan.