# adicionar um número numa lista e ela continuar ordenado

lista = [1,3,5,7,8,10,12,16,25,36]
numero_pendente = 11
maiorNumProx = lista[-1];
indice = lista.index(maiorNumProx)

# for item in lista:
#     if item > numero_pendente and maiorNumProx > item:
#       maiorNumProx = item
#       indice = lista.index(maiorNumProx)

# lista.insert(indice,numero_pendente)
# print(lista)

# adicionar com uma varredura
# lista2 = [None] * 11
lista2 = [1,3,5,7,8,10,12,16,25,36,None]
meuNum = 11

for item in lista2[::-1]:
    if lista2[lista2.index(item)] == None:
        lista2[lista2.index(item)] = meuNum
    elif item > meuNum:
        lista2[lista2.index(item) + 1] = item
    else:
        lista2[lista2.index(item) + 1] = meuNum
        break
print(lista2)    