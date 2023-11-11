TAB_X = [str(i) for i in range(1, 16)]
TAB_Y = [chr(i) for i in range(65, 81)]
RULES_NAV = {1: [4, 5], 2: [5, 2], 3: [1, 10], 4: [2, 5] }
LET_INVALID = ['K']
TORPEDO_TOTAL = 25

class Ship:
    def ler_posicao(posicao):
        posicao_x = posicao[1:]
        posicao_y = posicao[0]
        if posicao_y in LET_INVALID:
            raise Exception('ERROR_POSITION_NONEXISTENT_VALIDATION')

        x = TAB_X.index(posicao_x)
        y = TAB_Y.index(posicao_y)

        if x >= len(TAB_X) or y >= len(TAB_Y):
            raise Exception('ERROR_POSITION_NONEXISTENT_VALIDATION')
        return [x, y]

    def bombardeio(tabuleiro, torpedo_lista):
        for torpedo in torpedo_lista:
            for navio in tabuleiro:
                for tent_acerto in navio:
                    if torpedo[0] == tent_acerto[0] and torpedo[1] == tent_acerto[1]:
                        tent_acerto[2] = True

class Game:
    def gerar_resultado(jogador, ponstuacao):
        resultado = f'J{jogador} {ponstuacao[1]}AA {ponstuacao[2]}AE {ponstuacao[0]}PT'
        return resultado

    def escrever_result(resultado):
        arquivo = open('resultado.txt', 'w')
        arquivo.write(resultado)
        arquivo.close()

    def ler_jogador(nome_arquivo):
        arquivo = open(f'./{nome_arquivo}.txt', 'r')
        data = arquivo.read()
        arquivo.close()
        torpedo_lista = []
        tabuleiro = []
        for line in data.splitlines():
            if line == '#Jogada':
                continue
            [id, valor] = line.split(';')
            if id == 'T':
                aux_list = valor.split('|')
                if len(aux_list) != TORPEDO_TOTAL:
                    raise Exception('ERROR_NR_PARTS_VALIDATION')
                for torpedo in aux_list:
                    position = Ship.ler_posicao(torpedo)
                    torpedo_lista.append(position)
                continue
            id = int(id)
            navio_lista = valor.split('|')
            if len(navio_lista) != RULES_NAV[id][1]:
                raise Exception('ERROR_NR_PARTS_VALIDATION')
            for posicao in navio_lista:
                direcao = 'H'
                if RULES_NAV[id][0] > 1:
                    direcao = posicao[-1]
                    posicao = posicao[:-1]
                navio = []
                [x, y] = Ship.ler_posicao(posicao)
                for _ in range(RULES_NAV[id][0]):
                    navio.append([x, y, False])
                    if direcao == 'H': x += 1
                    elif direcao == 'V': y += 1
                tabuleiro.append(navio)
            piece_lista = []
            for navio in tabuleiro:
                for coordenadas in navio:
                    if coordenadas in piece_lista: raise Exception('ERROR_OVERWRITE_PIECES_VALIDATION')
                    piece_lista.append(coordenadas)
        return [tabuleiro, torpedo_lista]

    def cont_ponto(tabuleiro):
        pontos = 0
        acertos = 0
        erros = 0
        for navio in tabuleiro:
            aux_pontos = 0
            cont_acerto = 0
            for tent_acerto in navio:
                if tent_acerto[2]:
                    cont_acerto += 1
                    aux_pontos += 3
            if cont_acerto == len(navio):
                aux_pontos += 2
            navio_point = aux_pontos

            if navio_point == 0: erros += 1
            else: acertos += 1
            pontos += navio_point

        return [pontos, acertos, erros]

if __name__ == '__main__':
    erro_ = ''
    try:
        erro_ = 'J1'
        [tabuleiro_1, torpedo_lista_1] = Game.ler_jogador('jogador1')
        
        erro_ = 'J2'
        [tabuleiro_2, torpedo_lista_2] = Game.ler_jogador('jogador2')
        
        Ship.bombardeio(tabuleiro_1, torpedo_lista_2)
        Ship.bombardeio(tabuleiro_2, torpedo_lista_1)

        score_1 = Game.cont_ponto(tabuleiro_2)
        score_2 = Game.cont_ponto(tabuleiro_1)

        if score_1[0] > score_2[0]:
            result_string = Game.gerar_resultado(1, score_1)
            Game.escrever_result(result_string)

        if score_1[0] < score_2[0]:
            result_string = Game.gerar_resultado(2, score_2)
            Game.escrever_result(result_string)

        if score_1[0] == score_2[0]:
            result_string = Game.gerar_resultado(1, score_1)
            result_string += f'\n{Game.gerar_resultado(2, score_2)}'
            Game.escrever_result(result_string)

    except Exception as err:
        Game.escrever_result(f'{erro_} {str(err)}')