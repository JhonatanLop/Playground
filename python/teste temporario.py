# def mistura2(a):
#     list(a)
#     # list(b)
#     a = a:[2]
#     print(a)
#     b = a[2:]
#     print(b)
#     print ("a: ",a, "b :",b)

# mistura2("palavra")

# a[:2]
# 0 1 |2 3 4 5 6
# p a |l a v r a
# p a |* * * * *

# a[2:]
# 0 1 |2 3 4 5 6
# p a |l a v r a
# * * |l a v r a

# def mistura2(a):
#     list(a)
#     # list(b)
#     a = a[2:] #b[:2] +
#      # b = a[:2] + b[2:]
#     return a #+b

# mistura2("tamo")

# def mistura2(a, b):
#     lisa = list(a)
#     lisb = list(b)
#     lisa = b[:2] + a[2:]
#     lisb += a[:2] + b[2:]
#     return lisa

# mistura2('mix', 'pod')


# s = "asa"
# # transforma s em lista sendo cada elemento uma letra da string
# s = list(s)
# print(s)
# # cria var sr que é o reverso da lista s
# # var = list(reverse(lista))
# sr = list(reversed(s))
# print(sr)
# # defini o separador usado para juntar a lista numa string
# separador = ""
# # junto os elementos da lista numa string usando o separador informado.
# # var = separador.join(lista)
# # join só funciona com um separador definido
# s = separador.join(s)
# sr = separador.join(sr)
# # se as strings forem iguais então é verdade que elas são palíndromes
# if s == sr:
#     v = True
# else:
#     v = False
# print(v)


# palavra = 'ana'
# frase ='ana e mariana gostam de banana'
# cont = 0
# while palavra.find(frase)-1:
#     cont+=1
#     frase = frase[(frase.find(palavra))+1:]
#     print(frase)
# print(cont)

# s = "casa"
# reverse_s = ''
# for indice in range(0, len(s)):
#     reverse_s = s[indice] + reverse_s
# print( reverse_s == s)

# s = "swiming"
# if len(s) >= 3:
#     sc = s[-3:]
#     if sc == "ing":
#         s = list(s)
#         s.append("ly")
#         s = "".join(s)
#     else:
#         s = list(s)
#         s.append("ing")
#         s = "".join(s)

# para saber se um número é impar:
# if numero % 2 == 0:
#   ele é impar
# numero % 2 é para saber se o resto da divisão por 2 da zero

# a = "çlksdfç"
# cont = len(a)
# if cont % 2 == 0:
#     print("é par")
#     print(cont)
# else:
#     print("é impar")
#     pass

# a1 = ""
# a2 = ""
# a = "kitten"
# b = "donut"
# ca = int((len(a)/2))
# if len(a) % 2 != 0:
#     a1 = a[:ca+1]
#     a2 = a[ca+1:]
#     # print(a1+a2)
# else:
#     a1 = a[:ca]
#     a2 = a[ca:]

# cb = int((len(b)/2))
# if len(b) % 2 != 0:
#     b1 = b[:cb+1]
#     b2 = b[cb+1:]
#     # print(b1+b2)
# else:
#     b1 = a[:cb]
#     b2 = a[cb:]
# a = a1+b1
# b = a2+b2
# print(a,b)

# n = 480650000
# indice = "0"
# cont = 0
# n = str(n)
# while indice == "0":
#     if n[-1:] == "0":
#         n = n[:len(n)-1]
#         cont = cont + 1
#     else:
#         indice = "cabo irmão"
# n = int(n)
# print(cont)

# palavra = "palavra"
# print(palavra)
# palavra = palavra[:1]
# print(palavra)

n = 23
cont = 0
# for i in range(n):
#     indice = i
#     if "2" in str(i):
#         while "2" in str(indice):
#             cont += 1
#             indice = str(indice)
#             indice = indice[1:]
# print(cont)

n = int(input("digite n"))
cont = 0
for i in range(n):
    n2 = str(i)
    for letra in n2:
        if letra =="2":
            cont+= 1
print(cont)