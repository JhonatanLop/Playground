lista = [15, 23, 2, 18, 10, 21, 17, 3, 19, 16];
nov_lista = []

for j in lista:
    menor_numero = lista[0]
    for i in lista:    
        if menor_numero > i:
            menor_numero = i
    lista.remove(menor_numero)
    nov_lista.append(menor_numero)

print(menor_numero)
print(lista)
print(nov_lista)