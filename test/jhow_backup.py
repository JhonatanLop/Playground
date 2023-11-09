def read_input_file(nome1, nome2):
    arquivo1 = open(nome1)
    arquivo2 = open(nome2)
    torpedos = []
    posicoes = {}
    tipos_navios = "1234"
    for i in arquivo1.read().split('\n'):
        i = i.rstrip()
        if i[0] in tipos_navios:
            posicoes[i[0]] = i.split(';')[1].split('|')
        elif i[0] == 'T':
            torpedos = i.split(';')[1].split('|')
    arquivo1.close()
    for i in arquivo2.read().split('\n'):
        i = i.rstrip()
        if i[0] in tipos_navios:
            posicoes[i[0]] = i.split(';')[1].split('|')
        elif i[0] == 'T':
            torpedos = i.split(';')[1].split('|')
    arquivo2.close()
    return {'posicoes':posicoes,'torpedos':torpedos}

def validate_piece_positions(positions):
    for position in positions:
        if not (position[0].isalpha() and position[1:].isdigit()):
            return False
    return True

def validate_piece_overlap(positions, existing_pieces):
    for position in positions:
        if position in existing_pieces:
            return False
    return True

def validate_torpedo_positions(positions):
    for position in positions:
        if not (position[0].isalpha() and position[1:].isdigit()):
            return False
    return True

def process_torpedo_shots(positions, pieces):
    points = 0
    for position in positions:
        if position in pieces:
            pieces.remove(position)
            points += 1
    return points

def validate_parts(positions_dict, expected_size, torpedo_list, player_id, write_output):
    for k,v in positions_dict.items():
        if len(v) != expected_size[k]:
            write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))
    if len(torpedo_list) != expected_size['T']:
        write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))

def validate_position(row, column):
    if row > 15 or row < 0 or column > 15 or column < 0:
        return False
    return True

def validate_torpedos(torpedo_list, valid_letters, player_id, write_output):
    for t in torpedo_list:
        row = valid_letters.find(t[:1])
        col = int(t[1:])
        if not validate_position(row, col):
            write_output("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(player_id))

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
            for _ in range(size):
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

def play_game(player1_file, player2_file, result_file):
    player1_pieces = set()
    player2_pieces = set()
    player1_piece_counts = {"1": 0, "2": 0, "3": 0, "4": 0}
    player2_piece_counts = {"1": 0, "2": 0, "3": 0, "4": 0}
    player1_torpedo_count = 0
    player2_torpedo_count = 0
    player1_points = 0
    player2_points = 0
    valid_letters = "ABCDEFGHIJKLMNOP"

    input_data = read_input_file(player1_file, player2_file)

    for key, value in input_data['posicoes'].items():
        if not validate_piece_positions(value):
            with open(result_file, "w") as rf:
                rf.write("J1 ERROR_POSITION_NONEXISTENT_VALIDATION")
            return
        if not validate_piece_overlap(value, player1_pieces):
            with open(result_file, "w") as rf:
                rf.write("J1 ERROR_OVERWRITE_PIECES_VALIDATION")
            return
        player1_piece_counts[key] += len(value)
        if key == "1":
            if player1_piece_counts[key] > 5:
                with open(result_file, "w") as rf:
                    rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "2":
            if player1_piece_counts[key] > 2:
                with open(result_file, "w") as rf:
                    rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "3":
            if player1_piece_counts[key] > 10:
                with open(result_file, "w") as rf:
                    rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "4":
            if player1_piece_counts[key] > 5:
                with open(result_file, "w") as rf:
                    rf.write("J1 ERROR_NR_PARTS_VALIDATION")
                return
        for position in value:
            player1_pieces.add(position)

    for key, value in input_data['posicoes'].items():
        if not validate_piece_positions(value):
            with open(result_file, "w") as rf:
                rf.write("J2 ERROR_POSITION_NONEXISTENT_VALIDATION")
            return
        if not validate_piece_overlap(value, player2_pieces):
            with open(result_file, "w") as rf:
                rf.write("J2 ERROR_OVERWRITE_PIECES_VALIDATION")
            return
        player2_piece_counts[key] += len(value)
        if key == "1":
            if player2_piece_counts[key] > 5:
                with open(result_file, "w") as rf:
                    rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "2":
            if player2_piece_counts[key] > 2:
                with open(result_file, "w") as rf:
                    rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "3":
            if player2_piece_counts[key] > 10:
                with open(result_file, "w") as rf:
                    rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                return
        elif key == "4":
            if player2_piece_counts[key] > 5:
                with open(result_file, "w") as rf:
                    rf.write("J2 ERROR_NR_PARTS_VALIDATION")
                return
        for position in value:
            player2_pieces.add(position)

    if not validate_torpedo_positions(input_data['torpedos']):
        with open(result_file, "w") as rf:
            rf.write("J1 ERROR_POSITION_NONEXISTENT_VALIDATION")
        return
    player1_torpedo_count += len(input_data['torpedos'])
    if player1_torpedo_count > 25:
        with open(result_file, "w") as rf:
            rf.write("J1 ERROR_NR_PARTS_VALIDATION")
        return
    player2_points += process_torpedo_shots(input_data['torpedos'], player2_pieces)

    if not validate_torpedo_positions(input_data['torpedos']):
        with open(result_file, "w") as rf:
            rf.write("J2 ERROR_POSITION_NONEXISTENT_VALIDATION")
        return
    player2_torpedo_count += len(input_data['torpedos'])
    if player2_torpedo_count > 25:
        with open(result_file, "w") as rf:
            rf.write("J2 ERROR_NR_PARTS_VALIDATION")
        return
    player1_points += process_torpedo_shots(input_data['torpedos'], player1_pieces)

    if len(player1_pieces) == 0 and len(player2_pieces) == 0:
        result = "EMPATE"
    elif len(player1_pieces) == 0:
        result = "J2"
    elif len(player2_pieces) == 0:
        result = "J1"
    else:
        result = "INDETERMINADO"
    
    with open(result_file, "w") as rf:
        rf.write(f"{result} {player1_points} {len(player2_pieces)} {player1_points + len(player2_pieces)}\n")
        rf.write(f"{result} {player2_points} {len(player1_pieces)} {player2_points + len(player1_pieces)}\n")

player1_file = "jogador1.txt"
player2_file = "jogador2.txt"
result_file = "resultado.txt"

play_game(player1_file, player2_file, result_file)
