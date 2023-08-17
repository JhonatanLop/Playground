# adicionar um número numa lista e ela continuar ordenado

lista = [1,3,5,7,8,10,12,16,25,36]
numero_pendente = 11
maiorNumProx = lista[-1];
indice = lista.index(maiorNumProx)
print(indice)

for item in lista:
    if item > numero_pendente and maiorNumProx > item:
      maiorNumProx = item
      indice = lista.index(maiorNumProx)

lista.insert(indice,numero_pendente)
print(lista)