# Olá!
# Este será meu primeiro teste mexendo com arquivos em python
# se n funcionar... foda né
# meu professor de algoritmo que não da aula deixou uns slides pra estudar
# vou ver se consigo fazer alguma coisa seguindo essa merd... esse material.

# criando a variável "arquivo"
# a função que lê arquivos é open
# w == escrever

arquivo = open("arquivo_teste.txt", "w")
# para cada index num range de 1 a 100
for linha in range(1, 100):
    # escrever em arquivo (n sei oq)
    arquivo.write('%d\n' % linha)
# fechar conexão com arquivo
arquivo.close()

# bora executar!!
# ...
# não rolou nada
# no slide ele mandou procurar numa pasta no C:\ mas n tava lá tmb

# tem um outro código pra ler linhas e printar. vamos ver!

#r == reed == leitura
arquivo = open("arquivo_teste.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# Rodou!!! pena q n sei onde tá a merda desse arquivo...
# achei kkkk, tava na mesma pasta que esse arquivo.py


print(linha.rstrip())

# agora ele ta pedindo pra abrir um arquivo e reescrever e salvar num arquivo diferente... show

texto = open("arquivo_teste.txt")
saida = open("saida.txt", "w")

for linha in texto.readlines():
    for par in linha:
        if par == "2":
            saida.write("*")
        else:
            saida.write(par)

texto.close()
saida.close()

# funcionou. ele trocou todo numero 2 por * num arquivo chamado saida.txt
# nesse arquivo eu tive a experiência de trabalhar com arquivos.