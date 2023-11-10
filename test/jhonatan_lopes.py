TAB_X = [str(i) for i in range(1, 16)]
TAB_Y = [chr(i) for i in range(65, 81)]
LET_INVALID = ['K']
PONTUACAO_HIT = 3
DIR_H = 'H'
DIR_V = 'V'

TORPEDO_TOTAL = 25
RULES_NAV = {1: [4, 5], 2: [5, 2], 3: [1, 10], 4: [2, 5] }

class Ship:
    def criar_navio(id, posicao):
        direcao = DIR_H
        if RULES_NAV[id][0] > 1:
            direcao = posicao[-1]
            posicao = posicao[:-1]

        ship = []
        [x, y] = Ship.ler_posicao(posicao)
        for _ in range(RULES_NAV[id][0]):
            ship.append([x, y, False])
            if direcao == DIR_H: x += 1
            elif direcao == DIR_V: y += 1
        return ship
    
    def verif_navio(ship):
        cont_acerto = 0
        pontos = 0
        for tent_acerto in ship:
            if tent_acerto[2]:
                pontos += 3
                cont_acerto += 1
        if cont_acerto == len(ship):
            pontos += 2
        return pontos

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
    
    def add_torpedo(list, value_string):
        torpedo_list = value_string.split('|')
        if len(torpedo_list) != TORPEDO_TOTAL:
            raise Exception('ERROR_NR_PARTS_VALIDATION')
        for torpedo in torpedo_list:
            pos = Ship.ler_posicao(torpedo)
            list.append(pos)

    def bombardeio(board, torpedo_list):
        for torpedo in torpedo_list:
            for ship in board:
                Ship.acertar_navio(ship, torpedo)

    def acertar_navio(ship, torpedo):
        for tent_acerto in ship:
            if torpedo[0] == tent_acerto[0] and torpedo[1] == tent_acerto[1]:
                tent_acerto[2] = True

    def cont_ponto(board):
        pontos = 0
        hit = 0
        miss = 0
        for ship in board:
            ship_point = Ship.verif_navio(ship)
            if ship_point == 0: miss += 1
            else: hit += 1
            pontos += ship_point
        return [pontos, hit, miss]

class Board:
    def add_navio_tab(board, id, value_string):
        id = int(id)
        ship_list = value_string.split('|')
        if len(ship_list) != RULES_NAV[id][1]:
            raise Exception('ERROR_NR_PARTS_VALIDATION')
        for posicao in ship_list:
            ship = Ship.criar_navio(id, posicao)
            board.append(ship)


    def verif_sobreposicao_nav(board):
        piece_list = []
        for ship in board:
            for coords in ship:
                if coords in piece_list: raise Exception('ERROR_OVERWRITE_PIECES_VALIDATION')
                piece_list.append(coords)

class Game:
    def ler_arquivo(file_name):
        file = open(f'./{file_name}.txt', 'r')
        data = file.read()
        file.close()
        return data.splitlines()

    def escrever_result(write_str):
        file = open('resultado.txt', 'w')
        file.write(write_str)
        file.close()

    def gerar_resultado(player, score):
        write_str = f'J{player} {score[1]}AA {score[2]}AE {score[0]}PT'
        return write_str
    

    def escrever_erro(message):
        Game.escrever_result(message)

    def add_navio_tab(board, id, value_string):
        id = int(id)
        ship_list = value_string.split('|')
        if len(ship_list) != RULES_NAV[id][1]:
            raise Exception('ERROR_NR_PARTS_VALIDATION')
        for posicao in ship_list:
            ship = Ship.criar_navio(id, posicao)
            board.append(ship)

    def verif_navio(ship):
        pontos = 0
        cont_acerto = 0
        for tent_acerto in ship:
            if tent_acerto[2]:
                cont_acerto += 1
                pontos += 3
        if cont_acerto == len(ship):
            pontos += 2
        
        return pontos

    def verif_sobreposicao_nav(board):
        piece_list = []
        for ship in board:
            for coords in ship:
                if coords in piece_list: raise Exception('ERROR_OVERWRITE_PIECES_VALIDATION')
                piece_list.append(coords)

    def ler_jogador(file_name):
        data = Game.ler_arquivo(file_name)

        board = []
        torpedo_list = []
        for line in data:
            if line == '#Jogada':
                continue

            [id, value_string] = line.split(';')
            if id == 'T':
                Ship.add_torpedo(torpedo_list, value_string)
                continue
            
            Game.add_navio_tab(board, id, value_string)
            Game.verif_sobreposicao_nav(board)

        return [board, torpedo_list]

    def cont_ponto(board):
        pontos = 0
        hit = 0
        miss = 0
        for ship in board:
            ship_point = Game.verif_navio(ship)
            if ship_point == 0: miss += 1
            else: hit += 1
            pontos += ship_point

        return [pontos, hit, miss]

if __name__ == '__main__':
    err_scope = ''
    try:
        err_scope = 'J1'
        [board_1, torpedo_list_1] = Game.ler_jogador('jogador1')
        
        err_scope = 'J2'
        [board_2, torpedo_list_2] = Game.ler_jogador('jogador2')
        
        Ship.bombardeio(board_1, torpedo_list_2)
        Ship.bombardeio(board_2, torpedo_list_1)

        score_1 = Game.cont_ponto(board_2)
        score_2 = Game.cont_ponto(board_1)

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
        Game.escrever_erro(f'{err_scope} {str(err)}')