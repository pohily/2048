from random import choice

class Board():
    def __init__(self):
        self.board = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'] ]
        self.blanks_left = list(range(16))
        self.score = 0
        self.add_two()
        self.add_two()
        
        
    def __str__(self):
        lines = ['\nUp - Q   Down - A    Left - Z    Right - X']
        lines.append(f'Score: {self.score}')
        lines.append('------------------------------------------')
        
        for x in range(4):
            line = []
            for y in range(4):
                line.append(self.board[x][y])
            lines.append(' '.join(line))
        return '\n'.join(lines)


    def find_blanks(self):
        self.blanks_left = []
        for row in range(4):
            for column in range(4):
                if self.board[row][column] == '0':
                    self.blanks_left.append(row * 4 + column + 1)


    def add_two(self):
        if not self.blanks_left:
            print('You lose!')
        else:
            self.find_blanks()
            taken = choice(self.blanks_left) 
            self.blanks_left.remove(taken)
            
            ver = taken // 4
            hor = taken - 4 * ver
            self.board[ver][hor] = '2'


    def turn(self):
        self.board = list(zip(*self.board))
        for row in range(4):
            self.board[row] = list(self.board[row][::-1])


    def up(self):
        for row in range(1, 4):
            for column in range(4):
                for check_row in range(row - 1, -1, -1):
                    if self.board[check_row + 1][column] == '0':
                        continue
                    if self.board[check_row][column] == '0':
                        self.board[check_row][column], self.board[check_row + 1][column] = self.board[check_row + 1][column], self.board[check_row][column]
                        continue
                    elif self.board[check_row][column] == self.board[check_row + 1][column]:
                        self.board[check_row][column] = str(2 * int(self.board[check_row][column]))
                        self.score += 2 * int(self.board[check_row + 1][column])
                        self.board[check_row + 1][column] = '0'
                        break


    def down(self):
        self.turn()
        self.turn()
        self.up()
        self.turn()
        self.turn()


    def left(self):
        self.turn()
        self.up()
        self.turn()
        self.turn()
        self.turn()


    def right(self):
        self.turn()
        self.turn()
        self.turn()
        self.up()
        self.turn()
            

board = Board()
print(board)
while board.blanks_left:
    hand = input('--> ')
    if hand == 'q':
        board.up()
    elif hand == 'a':
        board.down()
    elif hand == 'z':
        board.left()
    elif hand == 'x':
        board.right()
    board.add_two()
    print(board)


