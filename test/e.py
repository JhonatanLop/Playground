import sys

from b import read_input_file
from c import write_output_file
# Função para validar a posição de uma peça
def validate_piece_positions(positions):
    for position in positions:
        if not (position[0].isalpha() and position[1:].isdigit()):
            return False
    return True

# Função para validar a sobreposição de peças
def validate_piece_overlap(positions, existing_pieces):
    for position in positions:
        if position in existing_pieces:
            return False
    return True

# Função para validar a posição de um torpedo
def validate_torpedo_positions(positions):
    for position in positions:
        if not (position[0].isalpha() and position[1:].isdigit()):
            return False
    return True

# Função para processar os tiros de um jogador
def process_torpedo_shots(positions, pieces):
    points = 0
    for position in positions:
        if position in pieces:
            pieces.remove(position)
            points += 1
    return points

# Função para validar a quantidade de peças
def validate_parts(positions_dict, expected_size, torpedo_list, player_id, write_output):
    for k,v in positions_dict.items():
        if len(v) != expected_size[k]:
            write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))
    if len(torpedo_list) != expected_size['T']:
        write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))

# Função para validar a posição de uma peça ou torpedo
def validate_position(row, column):
    if row > 15 or row < 0 or column > 15 or column < 0:
        return False
    return True

# Função para validar a posição de um torpedo
def validate_torpedos(torpedo_list, valid_letters, player_id, write_output):
    for t in torpedo_list:
        row = valid_letters.find(t[:1])
        col = int(t[1:])
        if not validate_position(row, col):
            write_output("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(player_id))

# Função para armazenar as posições das peças
def store_positions(positions_dict, ship_sizes, valid_letters, used_positions, current_ship_id, player_id, write_output):
    for key,val in positions_dict.items():
        size = ship_sizes[key]
        for pos in val:
            vertical = True
            if pos[-1] in 'HV':
                if pos[-1] == 'H':
                    vertical = False
                pos = pos[:-1]
            h = 0
            v = 0
            for i in range(size):
                new_row = valid_letters.find(pos[0])+v
                new_col = int(pos[1:])+h
                if vertical:
                    v += 1 
                else:
                    h += 1
                if not validate_position(new_row, new_col):
                    write_output("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(player_id))
                    return
                new_position =  str(new_row)+';'+str(new_col)
                if new_position in used_positions:
                    write_output("J{} ERROR_OVERWRITE_PIECES_VALIDATION".format(player_id))
                    return
                used_positions[new_position] = current_ship_id
            current_ship_id += 1
    return used_positions

# Função para processar o jogo
def play_game(player1_file, player2_file, result_file):
    # Inicializa as variáveis
    player1_pieces = set()
    player2_pieces = set()
    player1_piece_counts = {"1": 0, "2": 0, "3": 0, "4": 0}
    player2_piece_counts = {"1": 0, "2": 0, "3": 0, "4": 0}
    player1_torpedo_count = 0
    player2_torpedo_count = 0
    player1_points = 0
    player2_points = 0
    valid_letters = "ABCDEFGHIJKLMNOP"

    # Lê os arquivos de entrada
    with open(player1_file, "r") as f1, open(player2_file, "r") as f2:
        # Processa o arquivo do jogador 1
        for line in f1:
            if line.startswith("1;") or line.startswith("2;") or line.startswith("4;"):
                # Valida a posição da peça
                piece_code, piece_positions = line.strip().split(";")
                piece_positions = piece_positions.split("|")
                if not validate_piece_positions(piece_positions):
                    with open(result_file, "w") as rf:
                        rf.write("J1 ERROR_POSITION_NONEXISTENT_VALIDATION")
                    return
                # Valida a sobreposição de peças
                if not validate_piece_overlap(piece_positions, player1_pieces):
                    with open(result_file, "w") as rf:
                        rf.write("J1 ERROR_OVERWRITE_PIECES_VALIDATION")
                    return
                # Valida a quantidade de peças
                player1_piece_counts[piece_code] += 1
                if piece_code == "1":
                    if player1_piece_counts[piece_code] > 5:
                        with open(result_file, "w") as rf:
                            rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "2":
                    if player1_piece_counts[piece_code] > 2:
                        with open(result_file, "w") as rf:
                            rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "3":
                    if player1_piece_counts[piece_code] > 10:
                        with open(result_file, "w") as rf:
                            rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "4":
                    if player1_piece_counts[piece_code] > 5:
                        with open(result_file, "w") as rf:
                            rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                        return
                # Adiciona a peça ao conjunto de peças do jogador 1
                for position in piece_positions:
                    player1_pieces.add(position)
            elif line.startswith("# Jogada"):
                # Processa os tiros do jogador 1
                torpedo_positions = line.strip().split(";")[1].split("|")
                if not validate_torpedo_positions(torpedo_positions):
                    with open(result_file, "w") as rf:
                        rf.write("J1 ERROR_POSITION_NONEXISTENT_VALIDATION")
                    return
                player1_torpedo_count += len(torpedo_positions)
                if player1_torpedo_count > 25:
                    with open(result_file, "w") as rf:
                        rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                    return
                points = process_torpedo_shots(torpedo_positions, player2_pieces)
                player1_points += points

        # Processa o arquivo do jogador 2
        for line in f2:
            if line.startswith("1;") or line.startswith("2;") or line.startswith("4;"):
                # Valida a posição da peça
                piece_code, piece_positions = line.strip().split(";")
                piece_positions = piece_positions.split("|")
                if not validate_piece_positions(piece_positions):
                    with open(result_file, "w") as rf:
                        rf.write("J2 ERROR_POSITION_NONEXISTENT_VALIDATION")
                    return
                # Valida a sobreposição de peças
                if not validate_piece_overlap(piece_positions, player2_pieces):
                    with open(result_file, "w") as rf:
                        rf.write("J2 ERROR_OVERWRITE_PIECES_VALIDATION")
                    return
                # Valida a quantidade de peças
                player2_piece_counts[piece_code] += 1
                if piece_code == "1":
                    if player2_piece_counts[piece_code] > 5:
                        with open(result_file, "w") as rf:
                            rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "2":
                    if player2_piece_counts[piece_code] > 2:
                        with open(result_file, "w") as rf:
                            rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "3":
                    if player2_piece_counts[piece_code] > 10:
                        with open(result_file, "w") as rf:
                            rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                        return
                elif piece_code == "4":
                    if player2_piece_counts[piece_code] > 5:
                        with open(result_file, "w") as rf:
                            rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                        return
                # Adiciona a peça ao conjunto de peças do jogador 2
                for position in piece_positions:
                    player2_pieces.add(position)
            elif line.startswith("# Jogada"):
                # Processa os tiros do jogador 2
                torpedo_positions = line.strip().split(";")[1].split("|")
                if not validate_torpedo_positions(torpedo_positions):
                    with open(result_file, "w") as rf:
                        rf.write("J2 ERROR_POSITION_NONEXISTENT_VALIDATION")
                    return
                player2_torpedo_count += len(torpedo_positions)
                if player2_torpedo_count > 25:
                    with open(result_file, "w") as rf:
                        rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                    return
                points = process_torpedo_shots(torpedo_positions, player1_pieces)
                player2_points += points
    
    # Calcula o resultado do jogo
    if len(player1_pieces) == 0 and len(player2_pieces) == 0:
        result = "EMPATE"
    elif len(player1_pieces) == 0:
        result = "J2"
    elif len(player2_pieces) == 0:
        result = "J1"
    else:
        result = "INDETERMINADO"
    
    # Escreve o resultado no arquivo de saída
    with open(result_file, "w") as rf:
        rf.write(f"{result} {player1_points} {len(player2_pieces)} {player1_points + len(player2_pieces)}\n")
        rf.write(f"{result} {player2_points} {len(player1_pieces)} {player2_points + len(player1_pieces)}\n")

# Chama a função para jogar o jogo

player1_file = "jogador1.txt"
player2_file = "jogador2.txt"
result_file = "resultado.txt"

input_data = read_input_file(player1_file, player2_file)
output_data = play_game(*input_data)
write_output_file(result_file, output_data)
