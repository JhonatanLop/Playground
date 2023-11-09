import sys

class Game:
    def __init__(self, input_file):
        self.input_file = input_file
        self.torpedo_list = []
        self.positions_dict = {}
        self.ship_types = "1234"
        self.expected_size = {'1':5,'2':2,'3':10,'4':5,'T':25}
        self.valid_letters = "ABCDEFGHIJLMNOPQRSTUVXZ"
        self.ship_sizes = {'1':4,'2':5,'3':1,'4':2}
        self.used_positions = {}
        self.current_ship_id = 0
        self.nonexistent_position = False
        self.read_file()

    def read_file(self):
        with open(self.input_file) as file:
            for i in file.read().split('\n'):
                i = i.rstrip()
                if i[0] in self.ship_types:
                    self.positions_dict[i[0]] = i.split(';')[1].split('|')
                elif i[0] == 'T':
                    self.torpedo_list = i.split(';')[1].split('|')

    def validate_parts(self, player_id):
        for k,v in self.positions_dict.items():
            if len(v) != self.expected_size[k]:
                self.write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))
        if len(self.torpedo_list) != self.expected_size['T']:
            self.write_output("J{} ERROR_NR_PARTS_VALIDATION".format(player_id))

    def validate_position(self, row, column, player_id):
        if row > 15 or row < 0 or column > 15 or column < 0:
            return False
        return True

    def validate_torpedos(self, player_id):
        for t in self.torpedo_list:
            row = self.valid_letters.find(t[:1])
            col = int(t[1:])
            if not self.validate_position(row, col, player_id):
                self.write_output("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(player_id))

    def store_positions(self, player_id):
        for key,val in self.positions_dict.items():
            size = self.ship_sizes[key]
            for pos in val:
                vertical = True
                if pos[-1] in 'HV':
                    if pos[-1] == 'H':
                        vertical = False
                    pos = pos[:-1]
                h = 0
                v = 0
                for i in range(size):
                    new_row = self.valid_letters.find(pos[0])+v
                    new_col = int(pos[1:])+h
                    if vertical:
                        v += 1 
                    else:
                        h += 1
                    if not self.validate_position(new_row, new_col, player_id):
                        self.nonexistent_position = True
                    new_position =  str(new_row)+';'+str(new_col)
                    if new_position in self.used_positions:
                        self.write_output("J{} ERROR_OVERWRITE_PIECES_VALIDATION".format(player_id))
                    self.used_positions[new_position] = self.current_ship_id
                self.current_ship_id += 1
        if self.nonexistent_position:
            self.write_output("J{} ERROR_POSITION_NONEXISTENT_VALIDATION".format(player_id))
        return self.used_positions

    def play_game(self, used_positions, player_id):
        points = 0
        hit_ids = []
        for t in self.torpedo_list:
            row = self.valid_letters.find(t[:1])
            col = int(t[1:])
            position = str(row)+';'+str(col)
            if position in used_positions:
                points += 3
                idn = used_positions.pop(position)
                hit_ids.append(idn)
                if idn not in used_positions.values():
                    points += 2
        hits = len(set(hit_ids))
        misses = 22 - hits
        return {'points':points,'misses':misses,'hits':hits}

    @staticmethod
    def write_output(t):
        with open('result.txt','w') as file:
            file.write(t)
        sys.exit()

def main():
    player1 = Game('jogador1.txt')
    player2 = Game('jogador2.txt')

    player1.validate_parts(1)
    used_positions_p1 = player1.store_positions(1)
    player1.validate_torpedos(1)

    player2.validate_parts(2)
    used_positions_p2 = player2.store_positions(2)
    player2.validate_torpedos(2)

    result1 = player1.play_game(used_positions_p2,1)
    result2 = player2.play_game(used_positions_p1,2)
    
    if result1['points'] == result2['points']:
        Game.write_output("J1 {}H {}M {}P".format(result1['hits'],result1['misses'],result1['points']) + '\n' + "J2 {}H {}M {}P".format(result2['hits'],result2['misses'],result2['points']))
    if result1['points'] >= result2['points']:
        Game.write_output("J1 {}H {}M {}P".format(result1['hits'],result1['misses'],result1['points']))
    if result1['points'] <= result2['points']:
        Game.write_output("J2 {}H {}M {}P".format(result2['hits'],result2['misses'],result2['points']))
    
main()
