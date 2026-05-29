from enum import Enum
from dataclasses import dataclass


class Piece(Enum):
    PAWN = 1
    ROOK = 3
    KNIGHT = 4
    BISHOP = 6
    QUEEN = 8
    KING = 10


@dataclass
class P:
    piece: Piece
    player: int


row = [0] * 8
board = [row.copy() for _ in range(8)]


def disp_board(board):
    for row in board:
        print(row)


board[1] = [P(Piece.PAWN, 0)] * 8
board[-1] = [P(Piece.PAWN, 1)] * 8

board[0] = [
    P(Piece.ROOK, 0),
    P(Piece.KNIGHT, 0),
    P(Piece.BISHOP, 0),
    P(Piece.QUEEN, 0),
    P(Piece.KING, 0),
    P(Piece.BISHOP, 0),
    P(Piece.KNIGHT, 0),
    P(Piece.ROOK, 0),
]
board[-2] = [
    P(Piece.ROOK, 1),
    P(Piece.KNIGHT, 1),
    P(Piece.BISHOP, 1),
    P(Piece.QUEEN, 1),
    P(Piece.KING, 1),
    P(Piece.BISHOP, 1),
    P(Piece.KNIGHT, 1),
    P(Piece.ROOK, 1),
]

disp_board(board)
