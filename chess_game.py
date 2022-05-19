from abc import ABC, abstractmethod
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtGui import QPicture, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
import sys
class Board:
    def __init__(self):
        self.grid = [[False for _ in range(8)] for _ in range(8)]
    def move(self,starting_position:list,ending_pos):
        self.grid[starting_position[0]][starting_position[1]] = False
        self.grid[ending_pos[0]][ending_pos[1]] = True
class Piece(ABC):
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
        if player:
            self.path = "./pngs/pawn.png"
        else:
            self.path = "./pngs/b_pawn.png"
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
        if player:
            self.path = "./pngs/knight.png"
        else:
            self.path = "./pngs/b_knight.png"


    def move(self,changed):
        self.position = changed


    def attack(self,changed):
        self.position = changed


class Bishop(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        if player:
            self.path = "./pngs/bishop.png"
        else:
            self.path = "./pngs/b_bishop.png"

    def move(self, changed):
        self.position = changed

    def attack(self, changed):
        self.position = changed


class Rook(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.moved = False
        if player:
            self.path = "./pngs/rook.png"
        else:
            self.path = "./pngs/b_rook.png"

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
        if player:
            self.path = "./pngs/queen.png"
        else:
            self.path = "./pngs/b_queen.png"

    def move(self, changed):
        self.position = changed

    def attack(self, changed):
        self.position = changed


class King(Piece):
    def __init__(self, player, position):
        self.player = player
        self.position = position
        self.moved = False
        if player:
            self.path = "./pngs/king.png"
        else:
            self.path = "./pngs/b_king.png"

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


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Chess game")
        self.setFixedSize(QSize(1000, 750))
        self.MainDisplay()


    def MainDisplay(self):
        board = Board()
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
        self.game = Game(board, pieces)
        self.board = QLabel(self)
        self.selected = False
        self.circle = QLabel(self)
        self.p1 = []
        self.board.setGeometry(0, 0, 750, 750)
        self.board.setPixmap(QPixmap("./pngs/chess_board.PNG").scaled(750,750))
        self.board.show()
        self.update()


    def update(self):
        self.circle.hide()
        self.circle = QLabel(self)
        for i in range(len(self.p1)):
            self.p1[i].hide()
        self.p1 = []
        for piece in self.game.pieces:
            self.p2 = QLabel(self)
            self.p2.hide()
            self.p2.setGeometry(30 + piece.position[0] * 89, 10 + 89 * piece.position[1], 85, 85)
            self.p2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.p2.setPixmap(QPixmap(piece.path).scaledToHeight(85, Qt.TransformationMode.SmoothTransformation))
            self.p1.append(self.p2)
        for i in range(len(self.p1)):
            self.p1[i].show()

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if not self.circle.isHidden():
                self.circle.hide()
            self.pos = event.pos()
            self.rect = [(self.pos.x() - 27) // 90, (self.pos.y() - 10) // 90]
            self.circle.setGeometry(25 + self.rect[0] * 90, 8 + self.rect[1] * 89, 89, 89)
            self.circle.setPixmap(
                QPixmap("./pngs/circle.png").scaledToHeight(89, Qt.TransformationMode.SmoothTransformation))
            self.circle.show()
            if not self.selected:
                for piece in self.game.pieces:
                    if piece.position == self.rect:
                        self.selected = True
                        self.piece_selected = piece
            else:
                for ind,piece in enumerate(self.game.pieces):
                    if self.rect == piece.position:
                        self.game.pieces.pop(ind)
                self.selected = False
                self.piece_selected.move(self.rect)
                self.update()















app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()














