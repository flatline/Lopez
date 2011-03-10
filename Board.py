import random

class Board:

    # the piece values are used as a mnemonic, approximating the piece weights
    _pieces = [-1,  -3,  -4,  -5,  -9, -999,  1,   3,   4,   5,   9,   999]
    _names  = ['p', 'k', 'b', 'r', 'q', 'k', 'P', 'K', 'B', 'R', 'Q', 'K']

    _piece_names = dict(zip(_pieces, _names))
    _piece_values = dict(zip(_names, _pieces))

    def __init__(self, *args):
        """
        Creates a board in the start state.  Also accepts an optional Board argument, 
        which works as a copy constructor.
        """

        # current side's moves
        self._own_moves = []

        # tracked for heuristic purposes, all potential opponent's moves on one's own turn
        self._opponent_moves = []

        self._fen = "" # storage for FEP text
        
        if (len(args) == 0):
            # start state - board layout as follows  
            #              A1 A2 ...              A8
            self.board = [[5, 3, 4, 9, 999, 4, 3, 5],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [-1, -1, -1, -1, -1,   -1, -1, -1],
                          [-5, -3, -4, -9, -999, -4, -3, -5]]
            #              H1  H2 ...                    H8

            self.fifty_moves = 0
            
            # the file ordinal of the piece that may be captured
            self.en_passant = 0

            # 4 bits for flag; bit is set if can castle.
            # 1 = white, queen side
            # 2 = white, king side
            # 4 = black, queen side
            # 8 = black, king side
            self.castle = 2**4 - 1
            self.move = 0

            # 1 for white, -1 for black
            self.turn = 1
        else:
            # copy
            board = args[0]
            self.board = []
            for i in range(8):
                rank = []
                brank = board.board[i]
                self.board.append(rank)
                for j in range(8):
                    rank.append(brank[j])
        
            self.fifty_moves = board.fifty_moves
            self.en_passant = board.en_passant
            self.castle = board.castle
            self.move = 0
            self.turn = board.turn

    def __eq__(self, other):
        # compare the defining attributes of the board
        if (self.__class__ != other.__class__):
            return False
        return self.board == other.board and \
               self.en_passant == other.en_passant and \
               self.fifty_moves == other.fifty_moves and \
               self.turn == other.turn and \
               self.castle == other.castle

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # todo: faster hash generation
        # strip off the move number
        return self.to_FEN()[:-2].__hash__()

    def __str__(self):
        result = ''
        for i in range(7,-1,-1):            
            for j in range(8):
                result += self._piece_names.get(self.board[i][j], ".") + " "
            if i > 0:
                result += '\n'
        return result

    def to_FEN(self):
        """
        Generates Forsyth-Edwards Notation version of the current board.
        """
        if self._fen != '':
            return self._fen

        result = ""
        for i in range(7,-1,-1):
            rank = self.board[i]
            blanks = 0
            for j in range(8):
                next = self._piece_names.get(self.board[i][j], '')
                if next == '':
                    blanks += 1
                elif blanks > 0:
                    result += str(blanks)
                    blanks = 0
                    result += next
                else:
                    result += next
            if blanks > 0:
                result += str(blanks)
                blanks = 0
            if i > 0:
                result += '/'

        if self.turn == 1:
            result += ' b '
        else:
            result += ' w '

        if not self.castle:
            result += ' -'
        else:
            if self.castle & 2:
                result += 'K'
            if self.castle & 1:
                result += 'Q'
            if self.castle & 8:
                result += 'k'
            if self.castle & 4:
                result += 'q'

        # todo - en-passant, fifty-move.
        result += ' - 0 ' + str(self.move / 2)
        self._fen = result
        return result

    def _get_pawn_moves_black(self, pc, r, f):
        """Params:
        pc - the piece value, e.g. 1, -1, 3, -3, etc.
        r - the piece's rank, 0-based index
        f - the piece's file, 0-based index"""

        # todo: refactor
        moves = []
        # forward, forward from home r
        if r > 1:
            if self.board[r-1][f] == 0:
                moves.append(((r, f), (r-1, f)))
                if r == 6 and self.board[r-2][f] == 0:
                    # two moves from home rank
                    moves.append(((r, f), (r-2, f)))
            if self.en_passant:
                moves.append(((r, f), (r-1, self.en_passant)))
        else:
            # just always promote to queen
            if self.board[r-1][f] == 0:
                moves.append(((r, f), (r-1, f), 'q'))
                if r == 6 and self.board[r-2][f] == 0:
                    moves.append(((r, f), (r-2, f), 'q'))
            
        # captures
        if r > 1:
            if f < 7:
                fd1 = self.board[r-1][f+1]
                if fd1 * pc < 0: #if opponent's piece
                    moves.append(((r, f), (r-1, f+1)))        
            if f > 0:
                fd2 = self.board[r-1][f-1]
                if fd2 * pc < 0:
                    moves.append(((r, f), (r-1, f-1)))
        elif r == 1:
            if f < 7:
                fd1 = self.board[r-1][f+1]
                if fd1 * pc < 0: #if opponent's piece
                    moves.append(((r, f), (r-1, f+1), 'q'))        
            if f > 0:
                fd2 = self.board[r-1][f-1]
                if fd2 * pc < 0:
                    moves.append(((r, f), (r-1, f-1), 'q'))
        return moves

    def _get_pawn_moves_white(self, pc, r, f):
        # todo: refactor
        moves = []
        # forward, forward from home row
        if r < 6:
            if self.board[r+1][f] == 0:
                moves.append(((r, f), (r+1, f)))
                if r == 1 and self.board[r+2][f] == 0:
                    # two moves from home rank
                    moves.append(((r, f), (r+2, f)))
            if self.en_passant:
                moves.append(((r, f), (r+1, self.en_passant)))
        else:
            # just always promote to queen
            if self.board[r+1][f] == 0:
                moves.append(((r, f), (r+1, f), 'Q'))
                if r == 1 and self.board[r+2][f] == 0:
                    moves.append(((r, f), (r+2, f), 'Q'))
            
        # captures
        if r < 6:
            if f < 7:
                fd1 = self.board[r+1][f+1]
                if fd1 * pc < 0: #if opponent's piece
                    moves.append(((r, f), (r+1, f+1)))
            if f > 0:
                fd2 = self.board[r+1][f-1]
                if fd2 * pc < 0:
                    moves.append(((r, f), (r+1, f-1)))
        elif r == 6:
            if f < 7:
                fd1 = self.board[r+1][f+1]
                if fd1 * pc < 0: #if opponent's piece
                    moves.append(((r, f), (r+1, f+1), 'Q'))
            if f > 0:
                fd2 = self.board[r+1][f-1]
                if fd2 * pc < 0:
                    moves.append(((r, f), (r+1, f-1), 'Q'))
        return moves

    def _walk_piece(self, pc, rank, file, dr, df, dist):
        """
        Returns all moves for a piece in a given direction.  The walk
        stops when a friendly piece or capture is encountered, including
        the capture move if applicable.

        Params:
        pc - the numeric piece identifier
        rank - rank of the piece
        file - file of the piece
        dr - change in rank (e.g. -1)
        df - change in file (e.g. 1)
        dist - cut-off number of steps to walk; default(none) should = 8
        """
        moves = []
        r, f = rank, file
        while (dist > 0):
            r += dr
            f += df
            if r >= 0 and f >= 0 and r <= 7 and f <= 7:
                comp = pc * self.board[r][f]
                if comp <= 0:
                    moves.append(((rank,file),(r,f)))
                    # capture?
                    if comp < 0: 
                        break
                else:
                    break
            else:
                break
            dist -= 1
        return moves

    def _get_bishop_moves(self, pc, r, f):
        def walk(dx, dy):
            return self._walk_piece(pc,r,f,dx,dy,8)

        result = walk(1,1)
        result.extend(walk(-1,1))
        result.extend(walk(1,-1))
        result.extend(walk(-1,-1))
        return result        

    def _get_knight_moves(self, pc, r, f):
        def walk(dr, df):
            return self._walk_piece(pc,r,f,dr,df,1)

        result = walk(2,1)
        result.extend(walk(2,-1))
        result.extend(walk(-2,1))
        result.extend(walk(-2,-1))
        result.extend(walk(1,2))
        result.extend(walk(1,-2))
        result.extend(walk(-1,2))
        result.extend(walk(-1,-2))
        return result

    def _get_rook_moves(self, pc, r, f):
        def walk(dr, df):
            return self._walk_piece(pc,r,f,dr,df,8)
        
        result = walk(1,0)
        result.extend(walk(-1,0))
        result.extend(walk(0,1))
        result.extend(walk(0,-1))
        return result

    def _get_queen_moves(self, pc, r, f):
        def walk(dr, df):
            return self._walk_piece(pc,r,f,dr,df,8)

        result = walk(1,0)
        result.extend(walk(-1,0))
        result.extend(walk(0,1))
        result.extend(walk(0,-1))
        result.extend(walk(1,1))
        result.extend(walk(-1,1))
        result.extend(walk(1,-1))
        result.extend(walk(-1,-1))
        return result

    def _get_king_moves(self, pc, r, f):
        def walk(dr, df):
            return self._walk_piece(pc,r,f,dr,df,1)

        result = walk(1,0)
        result.extend(walk(-1,0))
        result.extend(walk(0,1))
        result.extend(walk(0,-1))
        result.extend(walk(1,1))
        result.extend(walk(-1,1))
        result.extend(walk(1,-1))
        result.extend(walk(-1,-1))            
        return result

    def _get_castling_moves(self, side):
        """
        Params:
        side = 1 for white, -1 for black
        """
        result = []
        # holy crap we have to check a lot of stuff!

        # todo: check that the rooks haven't actually been captured!
        if side == 1:
            back_rank = self.board[0]

            # white, queen side
            if self.castle & 1 and not (back_rank[1] + back_rank[2] + back_rank[3]):
                threatened = False
                for move in self.get_opponent_moves():
                    if move[1] in [(0,0), (0,1), (0,2), (0,3), (0,4)]:
                        threatened = True
                if not threatened:
                    result.append(((0,4),(0,2)))

            # white, king side
            if self.castle & 2 and not (back_rank[5] + back_rank[6]):
                threatened = False
                for move in self.get_opponent_moves():
                    if move[1] in [(0,4), (0,5), (0,6), (0,7)]:
                        threatened = True
                if not threatened:
                    result.append(((0,4),(0,6)))
        else:
            back_rank = self.board[7]
            # black, queen side
            if self.castle & 1 and not (back_rank[1] + back_rank[2] + back_rank[3]):
                threatened = False
                for move in self.get_opponent_moves():
                    if move[1] in [(7,0), (7,1), (7,2), (7,3), (7,4)]:
                        threatened = True
                if not threatened:
                    result.append(((7,4),(7,2)))

            # black, king side
            if self.castle & 2 and not (back_rank[5] + back_rank[6]):
                threatened = False
                for move in self.get_opponent_moves():
                    if move[1] in [(7,4), (7,5), (7,6), (7,7)]:
                        threatened = True
                if not threatened:
                    result.append(((7,4),(7,6)))

        return result

    def is_in_check(self):
        """Checks if the opponent has any direct moves against the king"""
        if len(self._opponent_moves) == 0:
            self.get_moves()

        own_king = self.find_piece(999 * self.turn)
        for move in self._opponent_moves:
            if move[1] == own_king:
                return True
        return False

    def is_opponent_in_check(self):
        """
        Checks whether the current side to move has any direct moves against the opponent's
        king.  used to determine checkmate scenarios; obviously such a board configuration
        is not valid in regular play
        """
        if len(self._own_moves) == 0:
            self.get_moves()

        opp_king = self.find_piece(-999 * self.turn)
        for move in self._own_moves:
            if move[1] == opp_king:
                return True
        return False
        
    def find_piece(self, pc):
        """Searches for the piece with value pc, returns (rank, file) if found,
        else None"""
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == pc:
                    return (i, j)
        return None

    def get_moves(self):
        """
        Gets all possible moves on the current board, for the currently playing side.
        Does not screen for illegal moves, such as exposing the king to attack.
        Has a side-effect of generating all opponent's possible moves, even though it is not
        their turn, for calculating heuristics and determining check scenarios.

        Returns: 
        Array of tuples of form ((from_rank, from_file), (to_rank, to_file))
        These may be applied directly to the board via apply_move
        """
        # compute once and cache
        if len(self._own_moves) == 0:
            for i in range(8):
                for j in range(8):
                    pc = self.board[i][j]
                    
                    moves = self._own_moves
                    # only for current side's turn
                    if pc * self.turn <= 0:
                        moves = self._opponent_moves

                    pc_value = abs(pc)

                    if pc == 1:
                        moves.extend(self._get_pawn_moves_white(pc, i, j))
                    elif pc == -1:
                        moves.extend(self._get_pawn_moves_black(pc, i, j))
                    elif pc_value == 3:
                        moves.extend(self._get_knight_moves(pc, i, j))
                    elif pc_value == 4:
                        moves.extend(self._get_bishop_moves(pc, i, j))
                    elif pc_value == 5:
                        moves.extend(self._get_rook_moves(pc, i, j))
                    elif pc_value == 9:
                        moves.extend(self._get_queen_moves(pc, i, j))
                    elif pc_value == 999:
                        moves.extend(self._get_king_moves(pc, i, j))

            # note: don't include opponent castle moves, they would only throw off heuristics
            # and are needed for no other purpose as they are not capturing moves
            self._own_moves.extend(self._get_castling_moves(self.turn))

            # todo - order by anticipated weights, e.g. capturing moves then threatening ones
            random.shuffle(self._own_moves)
        return self._own_moves

    def get_opponent_moves(self):
        """Get all of the opponent's possible moves for this board, even though it is not 
        their turn"""
        if len(self._opponent_moves) == 0:
            self.get_moves()
        return self._opponent_moves

    def get_all_moves(self):
        """Returns all moves for current side and for opponent on the current board"""
        return self.get_moves() + self._opponent_moves

    def apply_move(self, move):
        """
        Returns a new board with the move applied
        
        Params:
        move - ((from), (to)) as pairs of int coordinates of form (rank, file), 0-based.
            alternatively, ((from), (to), 'x'), where x is a piece designator for pawn
            promotion, e.g. 'q', 'Q', 'r', 'R', etc.
        """
        b = Board(self)
        r, f = move[0]
        tr, tf = move[1]
        pc = b.board[r][f]
        b.board[r][f] = 0

        if abs(pc) == 1 and len(move) == 3:
            # pawn promotion
            b.board[tr][tf] = self._piece_values[move[2]]
            self.en_passant = 0
        elif abs(pc) == 1 and self.en_passant and f != tf and self.board[tr][tf] == 0:
            # en-passant if the file changed and the target square is empty.
            b.board[tr][tf] = pc
            b.board[r][self.en_passant] = 0
        else:
            #default, just move the piece
            b.board[tr][tf] = pc

        # set the en-passant flag
        if pc == -1 and r == 6 and tr == 4 and \
                ((f > 0 and self.board[tr][f-1] == 1) or (f < 7 and self.board[tr][f+1] == 1)):
            b.en_passant = f
        elif pc == 1 and r == 1 and tr == 3 and \
                ((f > 0 and self.board[tr][f-1] == -1) or (f < 7 and self.board[tr][f+1] == -1)):
            b.en_passant = f
        else:
            b.en_passant = 0

        b.move += 1
        b.turn = self.turn * -1

        # clear the castle bits if king or rook moves, and move the rook if castling
        if pc == 999:
            if (f-tf > 1) and (self.castle & 1):
                b.board[0][0] = 0
                b.board[0][3] = 5
            elif (f-tf < -1) and (self.castle & 2):
                b.board[0][7] = 0
                b.board[0][5] = 5
            b.castle &= 12
        elif pc == -999:
            if (f-tf > 1) and (self.castle & 4):
                b.board[7][0] = 0
                b.board[7][3] = -5
            elif (f-tf < -1) and (self.castle & 8):
                b.board[7][7] = 0
                b.board[7][5] = -5            
            b.castle &= 3
        elif pc == 5:
            if r == 0 and f == 0:
                b.castle &= 14
            elif r == 0 and f == 7:
                b.castle &= 13
        elif pc == -5:
            if r == 7 and f == 0:
                b.castle &= 11
            if r == 7 and f == 7:
                b.castle &= 7
        return b

def main():
    return
    b = Board()
    print ''
    print b
    moves = b.get_moves()
    boards = []
    for move in moves:
        boards.append(b.apply_move(move))

    for board in boards:
        print ''
        print board
        mvs = board.get_moves()
        for mv in mvs:
            print ''
            print board.apply_move(mv)

if __name__ == "__main__":
    main()
