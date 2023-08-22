lista = [1,2,3,4,5]
indice = 4

def print_recursivo (indice, lista):
    if indice >= 0:
        print(lista[indice])
        print_recursivo(indice-1, lista)

print_recursivo(indice, lista)