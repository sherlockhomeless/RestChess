class PieceType:
    def __init__(self, num_piece):
        num_piece = abs(num_piece)
        self.type = {
            1: "P",
            2: "T",
            3: "KN",
            4: "B",
            5: "K",
            6: "Q"
        }
        self.piece_type = self.type.get(num_piece)
        self.movement_pattern = PieceType.get_movement_pattern(self.piece_type)

    @staticmethod
    def piece_type_to_number(num):
        assert type(num) is int
        pass

    @staticmethod
    def get_movement_pattern(piece_t):
        moves = []

        if piece_t == "P":
            moves.append(lambda pos: [pos[0] + 1, pos[1]])
            moves.append(lambda pos: [pos[0] + 2, pos[1]])

        elif piece_t == "T":
            for x in range(1, 8, 1):
                moves.append(lambda pos: [pos[0] + x, pos[1]])
                moves.append(lambda pos: [pos[0], pos[1] + 1])

        elif piece_t == "KN":
            moves.append(lambda pos: [pos[0] + 2, pos[1] - 1])
            moves.append(lambda pos: [pos[0] + 2, pos[1] + 1])
            moves.append(lambda pos: [pos[0] - 2, pos[1] - 1])
            moves.append(lambda pos: [pos[0] - 2, pos[1] + 1])
            moves.append(lambda pos: [pos[0] - 1, pos[1] + 2])
            moves.append(lambda pos: [pos[0] + 1, pos[1] + 2])
            moves.append(lambda pos: [pos[0] - 1, pos[1] - 2])
            moves.append(lambda pos: [pos[0] + 1, pos[1] - 2])

        elif piece_t == "B":
            # can go into four directions
            for y in range(8):
                moves.append(lambda pos: [pos[0] + y, pos[1] + y])  # go up right
                moves.append(lambda pos: [pos[0] + y, pos[1] - y])  # go up left
                moves.append(lambda pos: [pos[0] - y, pos[1] + y])  # go down right
                moves.append(lambda pos: [pos[0] - y, pos[1] - y])  # go down left

        elif piece_t == "K":
            moves.append(lambda pos: [pos[0] + 1, pos[1] - 1])  # left up
            moves.append(lambda pos: [pos[0] + 1, pos[1]])  # middle up
            moves.append(lambda pos: [pos[0] + 1, pos[1] + 1])  # right up
            moves.append(lambda pos: [pos[0], pos[1] + 1])  # middle right
            moves.append(lambda pos: [pos[0] - 1, pos[1] + 1])  # bottom right
            moves.append(lambda pos: [pos[0] - 1, pos[1]])  # middle bottom
            moves.append(lambda pos: [pos[0] - 1, pos[1] - 1])  # left bottom
            moves.append(lambda pos: [pos[0], pos[1] - 1])  # middle left

        elif piece_t == "Q":
            moves =  PieceType.get_movement_pattern("T") + PieceType.get_movement_pattern("B")

        else:
            raise ValueError

        return moves


class Board:
    """
    class representing the current state of the game.
    this includes:
    * all cells on the board
    * pieces on cells
    * also encapsulates rules enforcement of pieces

    piece mapping:
    + => black, - => white
    pawn = 1
    tower = 2
    knight = 3
    bishop = 4
    queen = 5
    king = 6
    """

    def __init__(self):
        self.board = [[[] for y in range(8)] for x in range(8)]
        self.board = Board.init_pieces(self.board)
        self.rounds = 0

    def __str__(self):
        separator_line = 8 * 2 * '-' + '\n'

        s = "" + separator_line
        for x in range(8):
            for y in range(8):
                s += f'|{self.board[y][x]}'
            s += '|' + '\n' + separator_line

        return s

    def make_move(self, src, dest, piece):
        """
        moves a piece using the algebraic notation syntax
        https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
        :param src: current position on board (e.g. A2, b4,...)
        :param dest: position of piece after round
        :param piece: type of piece
        :return:
        """
        src_index, dest_index = Board.map_chess_notation_to_index(src, dest)
        if self.is_valid_move(src_index, dest_index, piece):


    def is_valid_move(self, src_i, dest_i, piece):
        """
        checks if a given move is valid
        :param src_i: field from which piece should be moved in 'a1'-notation
        :param dest_i: field to which piece should be moved in 'a1'-notation
        :param piece: piece given as number of piece
        :return: bool
        """
        src, dest = Board.map_chess_notation_to_index(src_i, dest_i)

        assert self.board[src[0]][src[1]] == piece

    @staticmethod
    def map_chess_notation_to_index(*chess_notations):
        """
        :param chess_notations: string of kind "a2", "B3",...
        :return: Tupel containing indices of fields denoted by chess_notation
        """
        indices = ()
        for el in chess_notations:
            el = el.lower()
            assert el[0] in "abcdefgh"
            assert el[1] in "12345678"
            i1 = ord(el[0])-97  # convert to int, then convert to base 0
            i2 = int(el[1])-1
            indices += (i1, i2)
        return indices

    @staticmethod
    def init_pieces(board):
        """
        puts all the pieces on the board
        :param board: empty board
        :return: board stacked with pieces
        """
        order_pieces = [2, 3, 4, 5, 6, 4, 3, 2]
        for x in range(8):
            board[x][0] = order_pieces[x]
            board[x][7] = order_pieces[x] * -1
            board[x][1] = 1
            board[x][6] = -1

            for y in range(2, 6, 1):
                board[x][y] = 0

        return board


b = Board()
print(b)