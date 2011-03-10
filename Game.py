import sys
import re
import random
import time
from Board import Board
import Analyzer

move_pattern = re.compile(r"([a-h])([1-8])\s*([a-h])([1-8])([pnbrkq])?$", re.IGNORECASE)
level_pattern = re.compile(r"level\s+(\d+)\s+(\d+)\s+(\d+)", re.IGNORECASE)

def str_to_move(move_string):
    m = move_pattern.match(move_string)
    # FileRankFileRank, 97 is ord('a')
    pfrom = int(m.group(2)) - 1, ord(m.group(1)) - 97
    pto   = int(m.group(4)) - 1, ord(m.group(3)) - 97
    if m.lastindex < 5:
        return pfrom, pto
    else:
        return pfrom, pto, m.group(5)

def move_to_str(move):
    pfrom, pto = move[0], move[1]
    return chr(pfrom[1] + 97) + str(pfrom[0] + 1) + chr(pto[1] + 97) + str(pto[0] + 1)

class Game:
    def __init__(self):
        self.board = None
        self.analyzer = Analyzer.Analyzer()
        self.analyzer.sd_limit = 10
        self._log = None
        self._counter = 1
    def reset(self):
        self.board = Board()

    def accept_move(self, move_string):
        move = str_to_move(move_string)
        self.board = self.board.apply_move(move)

    def get_move(self):
        # time.sleep(2)
        # move = random.choice(self.board.get_moves())
        move = self.analyzer.minimax(self.board, 10).move
        self.board = self.board.apply_move(move)
        self._counter += 1
        return move_to_str(move)

    # http://home.hccnet.nl/h.g.muller/interfacing.txt
    def play_xboard(self):
        self._log = open("c:\\temp\\chess.log", "w")
        log = self._log
        log.write("initialized game engine\n\n")
        log.flush()
    
        running = False

        # main game loop
        while(True):
            val = sys.stdin.readline().lower()
            log.write(val)
            val = val.strip()

            if val == "new":
                self.reset()
            if level_pattern.match(val):
                nr_moves, time, time_incr = level_pattern.findall(val)[0]
                pass
            if val == "force":
                # just keep accepting moves, don't make any
                running = False
            elif val == "go":
                # start making moves again
                running = True
                move = self.get_move()
                sys.stdout.write("move " + move + "\n")
                sys.stdout.flush()
                log.write(">" + move + "\n")
                log.write(str(self.board) + "\n\n")
            elif move_pattern.match(val):
                try:
                    game_started = True
                    self.accept_move(val)
                    log.write("\n" + str(self.board) + "\n\n")
            
                    if running:
                        move = self.get_move()
                        sys.stdout.write("move " + move + "\n")
                        sys.stdout.flush()
                        log.write(">" + move + "\n")
                        log.write(str(self.board) + "\n\n")
                except Exception as e:
                    log.write(e)
            elif val == "quit":
                break

            log.flush()
        log.close()

if __name__ == "__main__":
    game = Game()
    game.play_xboard()


## When engine is white:
# xboard
# protover 2
# new
# random
# level 40 5 0
# post
# hard
# force
# computer
# black
# time 30000
# otim 30000
# white
# go

## When engine is black:
# xboard
# protover 2
# new
# random
# level 40 5 0
# post
# hard
# force
# computer
# time 30000
# otim 29999
# d2d4
# black
# go
# >a7a5
# time 29800
# otim 29245
# c2c4


## When engine terminates:
# result * {xboard exit}
# force
# quit

