import sys

class Jogo:
    def __init__(self, arquivo_entrada):
        self.arquivo_entrada = arquivo_entrada
        self.lista_torpedos = []
        self.dicionario_posicoes = {}
        self.navios_tipos = "1234"
        self.tamanho_esperado = {'1':5,'2':2,'3':10,'4':5,'T':25}
        self.letras_validas = "ABCDEFGHIJLMNOPQRSTUVXZ"
        self.tamanhos_navios = {'1':4,'2':5,'3':1,'4':2}
        self.posicoes_usadas = {}
        self.idNavioAtual = 0
        self.posicao_inexistente = False
        self.ler_arquivo()

    def ler_arquivo(self):
        with open(self.arquivo_entrada) as arquivo:
            for i in arquivo.read().split('\n'):
                i = i.rstrip()
                if i[0] in self.navios_tipos:
                    self.dicionario_posicoes[i[0]] = i.split(';')[1].split('|')
                elif i[0] == 'T':
                    self.lista_torpedos = i.split(';')[1].split('|')

    def validar_partes(self, id_jogador):
        for k,v in self.dicionario_posicoes.items():
            if len(v) != self.tamanho_esperado[k]:
                self.escrever_saida("J{} ERROR_NR_PARTS_VALIDATION".format(id_jogador))
        if len(self.lista_torpedos) != self.tamanho_esperado['T']:
            self.escrever_saida("J{} ERROR_NR_PARTS_VALIDATION".format(id_jogador))

    def validar_posicao(self, linha, coluna, id_jogador):
        if linha > 15 or linha < 0 or coluna > 15 or coluna < 0:
            return False
        return True

    def validar_torpedos(self, id_jogador):
        for t in self.lista_torpedos:
            linha = self.letras_validas.find(t[:1])
            colu = int(t[1:])
            if not self.validar_posicao(linha, colu, id_jogador):
                self.escrever_saida("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(id_jogador))

    def guardar_posicoes(self, id_jogador):
        for key,val in self.dicionario_posicoes.items():
            tam = self.tamanhos_navios[key]
            for pos in val:
                vertical = True
                if pos[-1] in 'HV':
                    if pos[-1] == 'H':
                        vertical = False
                    pos = pos[:-1]
                h = 0
                v = 0
                for i in range(tam):
                    novaLinha = self.letras_validas.find(pos[0])+v
                    novaColuna = int(pos[1:])+h
                    if vertical:
                        v += 1 
                    else:
                        h += 1
                    if not self.validar_posicao(novaLinha, novaColuna, id_jogador):
                        self.posicao_inexistente = True
                    novaPosicao =  str(novaLinha)+';'+str(novaColuna)
                    if novaPosicao in self.posicoes_usadas:
                        self.escrever_saida("J{} ERROR_OVERWRITE_PIECES_VALIDATION".format(id_jogador))
                    self.posicoes_usadas[novaPosicao] = self.idNavioAtual
                self.idNavioAtual += 1
        if self.posicao_inexistente:
            self.escrever_saida("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(id_jogador))
        return self.posicoes_usadas

    def realizar_jogadas(self, posicoes_usadas, id_jogador):
        pontos = 0
        ids_acertadas = []
        for t in self.lista_torpedos:
            linha = self.letras_validas.find(t[:1])
            colu = int(t[1:])
            posicao = str(linha)+';'+str(colu)
            if posicao in posicoes_usadas:
                pontos += 3
                idn = posicoes_usadas.pop(posicao)
                ids_acertadas.append(idn)
                if idn not in posicoes_usadas.values():
                    pontos += 2
        acertos = len(set(ids_acertadas))
        erros = 22 - acertos
        return {'pontos':pontos,'alvos':erros,'acertos':acertos}

    @staticmethod
    def escrever_saida(t):
        with open('resultado.txt','w') as arquivo:
            arquivo.write(t)
        sys.exit()

def main():
    jogador1 = Jogo('jogador1.txt')
    jogador2 = Jogo('jogador2.txt')

    jogador1.validar_partes(1)  
    posicoes_usadas_j1 = jogador1.guardar_posicoes(1)
    jogador1.validar_torpedos(1)

    jogador2.validar_partes(2)
    posicoes_usadas_j2 = jogador2.guardar_posicoes(2)
    jogador2.validar_torpedos(2)

    resultado1 = jogador1.realizar_jogadas(posicoes_usadas_j2,1)
    resultado2 = jogador2.realizar_jogadas(posicoes_usadas_j1,2)
    
    if resultado1['pontos'] == resultado2['pontos']:
        Jogo.escrever_saida("J1 {}AA {}AE {}PT".format(resultado1['acertos'],resultado1['alvos'],resultado1['pontos']) + '\n' + "J2 {}AA {}AE {}PT".format(resultado2['acertos'],resultado2['alvos'],resultado2['pontos']))
    if resultado1['pontos'] >= resultado2['pontos']:
        Jogo.escrever_saida("J1 {}AA {}AE {}PT".format(resultado1['acertos'],resultado1['alvos'],resultado1['pontos']))
    if resultado1['pontos'] <= resultado2['pontos']:
        Jogo.escrever_saida("J2 {}AA {}AE {}PT".format(resultado2['acertos'],resultado2['alvos'],resultado2['pontos']))
    
main()