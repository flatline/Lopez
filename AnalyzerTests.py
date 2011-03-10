from Analyzer import Analyzer
from Board import Board

def test_capture():
    print("testing simple capture and advance")
    print("\tsimple choice white")
    b = Board()
    b.board = [[0, 0, 0, 0, 0, 0, 0, -999],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [-1, 0, -3, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 999]]
    
    a = Analyzer()
    a.sd_limit = 2
    res = a.minimax(b, 20)
    assert(res.move == ((2, 1), (3, 2)))

    print("\tsimple choice black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 3, 0, 0, 0, 0, 0],
               [0, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    
    # a = Analyzer(20)
    a.sd_limit = 2
    res = a.minimax(b, 20)
    assert(res.move == ((4, 1), (3, 2)))

def print_move_chain(analyzer, board, move):
    while move:
        print board
        print "score: " + str(analyzer.score(board)) + ", next: " + str(move.move) + \
            " " + str(move.value)
        board = board.apply_move(move.move)
        move = move.next

def test_endgame_heuristics():
    a = Analyzer()
    b = Board()
    b.board = [[0, 5, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 999, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [5, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]

    res = a.minimax(b, 200)
    print_move_chain(a, b, res)

    b = Board()
    b.turn = -1
    b.board = [[0, -5, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, -999, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [-5, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 999]]

    res = a.minimax(b, 200)
    print_move_chain(a, b, res)
    
def test_scenarios():
    # some puzzles from Reinfeld's Chess Tactics for Beginners
    print("testing move pruning")
    a = Analyzer()
    a.sd_limit = 4
    print("\tPuzzle #21")
    b = Board()
    b.board = [[0,  0, 0, 0, 0,     0, 0, 0],
               [0,  0, 0, 0, 0,     0, 0, 0],
               [0, -1, 9, 0, 0,     0, 0, 0],
               [0,  0, 0, 0, -999, -1, 0, 0],
               [0,  0, 0, 0, 0,     0, 0, 999],
               [0,  0, 0, 0, 0,     0, 0, -1],
               [0,  0, 0, 0, 0,     0, 0, 0],
               [-9, 0, 0, 0, 3,     0, 0, 0]]

    res = a.minimax(b, 100)
    print_move_chain(a, b, res)
    assert(res.move == ((7,4),(5,3)))

    # todo - pawn promotion is required for this one!
    # print("\tPuzzle #23")
    # b = Board()
    # b.turn = -1
    # b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 999, 0, 0, 0, 0, -1],
    #            [-5, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, -999, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 5]]   

    # res = a.minimax(b)
    # print_move_chain(b, res)

    print("\tPuzzle 52")
    b = Board()
    b.turn = -1
    b.board = [[0, 0,  5, 0, 0, 0, 999, 0],
               [0, 0,  0, 0, 0, 1, 1, 1],
               [1, 0,  0, -9, 0, 0, 0, 0],
               [0, 1,  0, 0, 0, 0, 0, 0],
               [0, 0,  0, 0, 0, 0, 0, 0],
               [-1, -1, 0, 0, 0, 0, 0, -1],
               [0, 0,  9, 0, 0, -1, -1, 0],
               [0, 0,  0, -5, 0, 0, -999, 0]]    
    
    res = a.minimax(b, 100)
    print_move_chain(a, b, res)

def main():
    test_capture()
    test_endgame_heuristics()
    test_scenarios()

if __name__ == "__main__":
    main()
