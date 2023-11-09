
HIT_SCORE = 10
SUNK_BONUS = 50
SHIP_RULES = {
    0: (4, 1),
    1: (5, 1),
    2: (2, 2),
    3: (5, 2)
}
DIRECTION_HORIZONTAL = 'H'
DIRECTION_VERTICAL = 'V'


def get_position(pos_dir):
    x = int(pos_dir[1:]) - 1
    y = ord(pos_dir[0]) - ord('A')
    return x, y


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()


def generate_result_string(player_num, score):
    return f'Jogador {player_num}: {score[0]} pontos ({score[1]} acertos, {score[2]} erros, {score[3]} navios afundados)'


def write_string_in_result(result_string):
    with open('resultado.txt', 'w') as f:
        f.write(result_string)


class Board:
    def __init__(self):
        self.board = [[None for _ in range(15)] for _ in range(15)]
    
    def add_ship(self, x, y, size, direction):
        if direction == 'H':
            for i in range(size):
                if self.board[x][y+i] is not None:
                    raise Exception('ERROR_OVERWRITE_PIECES_VALIDATION')
                self.board[x][y+i] = False
        elif direction == 'V':
            for i in range(size):
                if self.board[x+i][y] is not None:
                    raise Exception('ERROR_OVERWRITE_PIECES_VALIDATION')
                self.board[x+i][y] = False
    
    def add_torpedo(self, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = True
            return False
        elif self.board[x][y] is False:
            self.board[x][y] = True
            return True
        else:
            return False
    
    def get_score(self):
        hit = 0
        miss = 0
        sunk = 0
        for i in range(15):
            for j in range(15):
                if self.board[i][j] is False:
                    miss += 1
                elif self.board[i][j] is True:
                    hit += 1
        for size in [4, 5, 2, 5]:
            for i in range(15):
                for j in range(15):
                    if self.board[i][j] is False:
                        continue
                    if i+size <= 15 and all(self.board[i+k][j] for k in range(size)):
                        sunk += 1
                    if j+size <= 15 and all(self.board[i][j+k] for k in range(size)):
                        sunk += 1
        return HIT_SCORE*hit + SUNK_BONUS*sunk, hit, miss, sunk


class Player:
    def __init__(self, player_num):
        self.board = Board()
        self.torpedos = []
        self.player_num = player_num
    
    def read_file(self, file_name):
        data = read_file(file_name)

        for line in data:
            if line == '#Jogada':
                continue

            [code, value_string] = line.split(';')
            if code == 'T':
                self.torpedos.extend([get_position(torpedo) for torpedo in value_string.split('|')])
            else:
                code = int(code)
                ship_list = value_string.split('|')
                if len(ship_list) != SHIP_RULES[code][1]:
                    raise Exception('ERROR_NR_PARTS_VALIDATION')
                for pos_dir in ship_list:
                    direction = DIRECTION_HORIZONTAL if SHIP_RULES[code][0] > 1 else DIRECTION_VERTICAL
                    x, y = get_position(pos_dir)
                    self.board.add_ship(x, y, SHIP_RULES[code][0], direction)
    
    def resolve_board(self, other_player):
        for torpedo in self.torpedos:
            other_player.board.add_torpedo(*torpedo)
    
    def get_score(self):
        return self.board.get_score()


class Game:
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.current_player = 0
    
    def play(self):
        self.players[0].read_file('jogador1.txt')
        self.players[1].read_file('jogador2.txt')
        self.players[0].resolve_board(self.players[1])
        self.players[1].resolve_board(self.players[0])
        score1 = self.players[1].get_score()
        score2 = self.players[0].get_score()
        if score1[0] > score2[0]:
            result_string = generate_result_string(1, score1)
            write_string_in_result(result_string)
        elif score1[0] < score2[0]:
            result_string = generate_result_string(2, score2)
            write_string_in_result(result_string)
        else:
            result_string = generate_result_string(1, score1) + '\n' + generate_result_string(2, score2)
            write_string_in_result(result_string)


if __name__ == '__main__':
    game = Game()
    game.play()
    os.system('cat resultado.txt')
    write_string_in_result(result_string)
