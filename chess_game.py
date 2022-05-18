from abc import ABC, abstractmethod
class Board:
    def __init__(self):
        self.grid = [[False for _ in range(8)] for _ in range(8)]
    def move(self,starting_position:list,ending_pos):
        self.grid[starting_position[0]][starting_position[1]] = False
        self.grid[ending_pos[0]][ending_pos[1]] = True
class Piece():
    @abstractmethod
    def move(self,*args):
        ...
    @abstractmethod
    def attack(self,*args):
        ...

class Pawn(Piece):
    def __init__(self,player,position):
        self.player = player
        self.position = position
        self.moved = False
        self.path = "/pngs/pawn.png"
    def move(self,changed):
        self.position = changed
        self.moved = True
    def attack(self,changed):
        self.position = changed
        self.moved = True

class Knight(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.path = "/pngs/knight.png"


    def move(self,changed):
        self.position = changed


    def attack(self,changed):
        self.position = changed


class Bishop(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.path = "/pngs/bishop.png"

    def move(self, changed):
        self.position = changed

    def attack(self, changed):
        self.position = changed


class Rook(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.moved = False
        self.path = "/pngs/rook.png"

    def move(self, changed):
        self.position = changed
        self.moved = True

    def attack(self, changed):
        self.position = changed
        self.moved = True

class Queen(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.path = "/pngs/queen.png"

    def move(self, changed):
        self.position = changed

    def attack(self, changed):
        self.position = changed
class King(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.moved = False
        self.path = "/pngs/king.png"

    def move(self, changed):
        self.position = changed
        self.moved = True

    def attack(self, changed):
        self.position = changed
        self.moved = True
class Game:
    def __init__(self,board, p):
        self.board = board
        self.pieces = p.copy()
        for piece in self.pieces:
            board.grid[piece.position[0]][piece.position[1]] = True
    def player_move(self):
        pass
pieces = []
for i in range(8):
    pieces.append(Pawn(True, [i, 6]))
    pieces.append(Pawn(False, [i, 1]))
pieces.append(Knight(True, [1, 7]))
pieces.append(Knight(True, [6, 7]))
pieces.append(Bishop(True, [2, 7]))
pieces.append(Bishop(True, [5, 7]))
pieces.append(Rook(True, [0, 7]))
pieces.append(Rook(True, [7, 7]))
pieces.append(Queen(True, [3, 7]))
pieces.append(King(True, [4, 7]))

pieces.append(Knight(False, [1, 0]))
pieces.append(Knight(False, [6, 0]))
pieces.append(Bishop(False, [2, 0]))
pieces.append(Bishop(False, [5, 0]))
pieces.append(Rook(False, [0, 0]))
pieces.append(Rook(False, [7, 0]))
pieces.append(Queen(False, [3, 0]))
pieces.append(King(False, [4, 0]))
b = Board()
g = Game(b,pieces)
print("ok")













