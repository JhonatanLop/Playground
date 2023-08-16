lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11]

def num_primo (lt):
    cont = 0
    for i in lt:
        if (idenficiador_primo(lt[i])):
            cont += 1
    return cont
  
def idenficiador_primo (i):
    j = 1
    for j in range(i):
        if i % j == 0:
            return True
    else:
        return False

num_primo(lista)
