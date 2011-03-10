import sys
import random
from Board import Board
from datetime import datetime

piece_weights = {
     0 : 0,
    -1 : -1,
    -3 : -3,
    -4 : -3,
    -5 : -5,
    -9 : -9,
  -999 : -1000000,
     1 : 1,
     3 : 3,
     4 : 3,
     5 : 5,
     9 : 9,
   999 : 1000000
}

# heuristic components
def piece_total(board):
    tot = 0
    for i in range(8):
        rank = board.board[i]
        for j in range(8):
            tot += piece_weights.get(rank[j], 0)
    return tot

def offence_level(board):
    """
    Returns the total of the other side's pieces that are under attack
    """
    tot = 0
    if board.is_in_check():
        tot -= 1000000 * board.turn
    for move in board.get_moves():
        target = move[1]
        #tot += piece_weights.get(board.board[target[0]][target[1]])
        tot += board.board[target[0]][target[1]]
    return tot

def defence_level(board):
    return 0

def center_control(board):
    # needs eval of both sides
    #return sum([1 for move in board.get_moves() if move[0][1] > 1 and move[0][1] < 6])
    return sum([board.board[move[0][0]][move[0][1]] for move in board.get_moves() if \
                    move[0][1] > 1 and move[0][1] < 6])
    
class MoveWrapper:
    def __init__(self, move, value, depth, next):
        self.move = move
        self.value = value
        self.depth = depth
        self.next = next

class Analyzer:

    default_move = ((0,0), (0,0))

    def __init__(self):
        self._trans_tab = {}
        self._board = None

        # search depth (ply)
        self.sd_limit = 4
        self._last_sd = 2

        # time elapsed for current search, in ms
        self._start_time = None
        self.time_limit = 20
        self._side = 1
        self.dbg = False
        self.counter = 0

    def score(self, b):
        return 3*piece_total(b) - 2*offence_level(b) #+ center_control(b)

    def minimax(self, board, time_limit):
        # todo: is erroring out occasionally with the iterative deepening bit...
        self._trans_tab = {}
        self.time_limit = time_limit
        self.counter = 0
        self._start_time = datetime.now()
        self._side = board.turn
        self._last_sd = 1
        best_move = MoveWrapper(self.default_move, - sys.maxint - 1, 0, None)
        while self.sd_limit >= self._last_sd:
            next_move = self._max_value(board, -sys.maxint - 1, sys.maxint, self._last_sd)
            if self._is_timeout():
                if next_move.move != self.default_move and next_move.value > best_move.value and \
                        next_move.depth >= best_move.depth:
                    return next_move
                else:
                    return best_move
            best_move = next_move
            self._last_sd += 1
        return best_move

    def _is_timeout(self):
        return (datetime.now() - self._start_time).seconds >= self.time_limit

    def _is_game_over(self, board):
        # todo - return -1, 0, or 1 for wins/draw, else something else None (?)
        white_king_found = False
        black_king_found = False
        for i in range(8):
            rank = board.board[i]
            for j in range(8):
                if rank[j] == 999:
                    white_king_found = True
                elif rank[j] == -999:
                    black_king_found = True

        return not (white_king_found and black_king_found)

    def _max_value(self, board, alpha_max, beta_min, sd):
        saved = self._trans_tab.get(board, None)
        if saved and saved.depth and saved.depth >= sd:
            return saved
        if sd == 0 or self._is_game_over(board) or self._is_timeout():
            return MoveWrapper(self.default_move, self.score(board) * self._side, 0, None)

        move_list = board.get_moves()
        best_move = MoveWrapper(move_list[0], alpha_max, 0, None)
        for move in move_list:
            minm = self._min_value(board.apply_move(move), alpha_max, beta_min, sd - 1)
            if minm.value > alpha_max:
                alpha_max = minm.value
                best_move = MoveWrapper(move, minm.value, sd, minm)
            if minm.value >= beta_min:
                return MoveWrapper(move, alpha_max, 0, minm)

        if not saved or saved.depth < best_move.depth:
            self._trans_tab[board] = best_move
        return best_move

    def _min_value(self, board, alpha_max, beta_min, sd):
        saved = self._trans_tab.get(board, None)
        if saved and saved.depth and saved.depth >= sd:
            return saved
        if sd == 0 or self._is_game_over(board) or self._is_timeout():
            return MoveWrapper(self.default_move, self.score(board) * self._side, 0, None)

        move_list = board.get_moves()
        best_move = MoveWrapper(move_list[0], beta_min, 0, None)
        for move in move_list:
            maxm = self._max_value(board.apply_move(move), alpha_max, beta_min, sd - 1)
            if maxm.value < beta_min:
                beta_min = maxm.value
                best_move = MoveWrapper(move, maxm.value, sd, maxm)
            if maxm.value <= alpha_max:
                return MoveWrapper(best_move, beta_min, 0, maxm)

        if not saved or saved.depth < best_move.depth:
            self._trans_tab[board] = best_move
        return best_move
