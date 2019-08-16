import random
from time import sleep


class TicTacToe(object):

    def __init__(self, board_size, player1, player2):
        self.board_size = board_size
        self.board = []
        self.palyer1 = player1
        self.player2 = player2

        # initialize board
        for i in range(self.board_size):
            self.board.append([0 for i in range(self.board_size)])

    def _print_board(self):

        for y in range(self.board_size):
            x_counter = 0
            board_column = []
            for x in range(self.board_size):

                if x_counter == self.board_size - 1:
                    board_column.append(self.board[x][y])
                    print(board_column)
                else:
                    x_counter += 1
                    board_column.append(self.board[x][y])
        print('')

    def _possibilities(self):
        possibilities = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[x][y] == 0:
                    possibilities.append((x, y))

        return possibilities

    def play(self, player, x, y):

        if (x, y) in self._possibilities():
            self.board[x][y] = player
            if self._win_row(player, y) or self._win_colum(player, x) or self._win_diagonal(player):
                return True
            else:
                return False

    def _get_play_position(self):
        possibilities = self._possibilities()
        if possibilities:
            return random.choice(possibilities)

        return None

    def _win_row(self, player, y):
        win = True
        for x in range(self.board_size):
            if self.board[x][y] != player:
                win = False
                break
        return win

    def _win_colum(self, player, x):
        win = True
        for y in range(self.board_size):
            if self.board[x][y] != player:
                win = False
                break
        return win

    def _win_diagonal(self, player):
        win = True
        n = self.board_size
        for x in range(n):
            if self.board[x][x] != player:
                win = False
                break

        if win:
            return True
        else:
            win = True
            for x in range(n):
                y = n - x - 1
                if self.board[x][y] != player:
                    win = False
                    break
        return win

    def play_game(self):
        win = False
        counter = 0
        self._print_board()
        # sleep(2)
        while not win:
            for player in [self.palyer1, self.player2]:
                loc = self._get_play_position()
                self._print_board()
                sleep(1)
                if not loc:
                    self._print_board()
                    print("It's a draw")
                    win = 0
                    return
                else:
                    x, y = loc
                    counter += 1
                    print("{} play, location [{},{}], move {}".format(player, x, y, counter))
                    if self.play(player, x, y):
                        self._print_board()
                        print("{} wins!!!".format(player))
                        win = 0
                        return
                    else:
                        continue


if __name__ == '__main__':
    tictac = TicTacToe(5, 'O', 'X')
    tictac.play_game()
