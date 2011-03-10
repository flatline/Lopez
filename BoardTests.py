from Board import Board

empty_board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

def test_bishop_moves():
    print("testing bishop moves:")
    b = Board()

    print("\ttesting full expanse for bishop")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res1 = b._get_bishop_moves(4, 3, 3)
    exp1 = [((3, 3), (4, 4)), ((3, 3), (5, 5)), ((3, 3), (6, 6)), \
            ((3, 3), (7, 7)), ((3, 3), (2, 4)), ((3, 3), (1, 5)), \
            ((3, 3), (0, 6)), ((3, 3), (4, 2)), ((3, 3), (5, 1)), \
            ((3, 3), (6, 0)), ((3, 3), (2, 2)), ((3, 3), (1, 1)), \
            ((3, 3), (0, 0))]

    [res1.index(x) for x in exp1]
    assert(len(res1) == len(exp1))

    res2 = b._get_bishop_moves(-4, 3, 4)
    exp2 = [((3, 4), (4, 5)), ((3, 4), (5, 6)), ((3, 4), (6, 7)), \
            ((3, 4), (2, 5)), ((3, 4), (1, 6)), ((3, 4), (0, 7)), \
            ((3, 4), (4, 3)), ((3, 4), (5, 2)), ((3, 4), (6, 1)), \
            ((3, 4), (7, 0)), ((3, 4), (2, 3)), ((3, 4), (1, 2)), \
            ((3, 4), (0, 1))]

    [res2.index(x) for x in exp2]
    assert(len(res2) == len(exp2))
    
    print("\tno moves - surrounded")

    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 4, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_bishop_moves(4, 3, 3)
    assert(len(res) == 0)

    print("\tone move, one capture")

    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 4, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, -1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_bishop_moves(4, 3, 3)
    exp = [((3, 3), (2, 4)), ((3, 3), (4, 2)), ((3, 3), (5, 1))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_knight_moves():
    print("testing knight moves:")
    b = Board()
    
    print("\tevery direction")        
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_knight_moves(3, 3, 3)
    exp = [((3, 3), (5, 4)), ((3, 3), (5, 2)), ((3, 3), (1, 4)), \
           ((3, 3), (1, 2)), ((3, 3), (4, 5)), ((3, 3), (4, 1)), \
           ((3, 3), (2, 5)), ((3, 3), (2, 1))]

    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print("\tcorners")
    b.board = [[3, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_knight_moves(3, 0, 0)
    exp = [((0, 0), (2, 1)), ((0, 0), (1, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 3]]

    res = b._get_knight_moves(3, 7, 7)
    exp = [((7, 7), (5, 6)), ((7, 7), (6, 5))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print ("\tblocked, capture")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 3, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_knight_moves(3, 3, 3)
    exp = [((3, 3), (5, 4))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_rook_moves():
    print("testing rook moves:")
    b = Board()

    print("\tedges")
    b.board = [[5, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_rook_moves(5,0,0)
    exp = [((0, 0), (1, 0)), ((0, 0), (2, 0)), ((0, 0), (3, 0)), \
           ((0, 0), (4, 0)), ((0, 0), (5, 0)), ((0, 0), (6, 0)), \
           ((0, 0), (7, 0)), ((0, 0), (0, 1)), ((0, 0), (0, 2)), \
           ((0, 0), (0, 3)), ((0, 0), (0, 4)), ((0, 0), (0, 5)), \
           ((0, 0), (0, 6)), ((0, 0), (0, 7))]

    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print("\tcenter")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_rook_moves(5,3,3)
    exp = [((3, 3), (4, 3)), ((3, 3), (5, 3)), ((3, 3), (6, 3)), \
           ((3, 3), (7, 3)), ((3, 3), (2, 3)), ((3, 3), (1, 3)), \
           ((3, 3), (0, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 5)), \
           ((3, 3), (3, 6)), ((3, 3), (3, 7)), ((3, 3), (3, 2)), \
           ((3, 3), (3, 1)), ((3, 3), (3, 0))]

    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print ("\tcapture and block")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 5, 0, -4, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_rook_moves(5,3,3)
    exp = [((3, 3), (3, 4)), ((3, 3), (3, 5))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_queen_moves():
    print("testing queen moves")
    b = Board()
    
    # assumes that since bishops and rooks work, the edge conditions,
    # etc. have already been taken care of.
    print("\tblock and capture")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, -1, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 9, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_queen_moves(9,3,3)
    exp = [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (1, 3)), \
           ((3, 3), (3, 4)), ((3, 3), (3, 5)), ((3, 3), (3, 2)), \
           ((3, 3), (4, 4)), ((3, 3), (5, 5)), ((3, 3), (2, 4)), \
           ((3, 3), (1, 5)), ((3, 3), (4, 2)), ((3, 3), (2, 2))]

    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_pawn_moves():
    print("testing pawn moves")
    b = Board()

    print("\tmove from home rank")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0, 0, 1],
                [0, 0, -1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    res = b._get_pawn_moves_white(1,1,2)
    exp = [((1, 2), (2, 2)), ((1, 2), (3, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    res = b._get_pawn_moves_black(-1,6,2)
    exp = [((6, 2), (5, 2)), ((6, 2), (4, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print("\tnon-home move")
    res = b._get_pawn_moves_white(1,2,5)
    exp = [((2, 5), (3, 5))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    res = b._get_pawn_moves_black(-1,5,4)
    exp = [((5, 4), (4, 4))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    print("\tblocked")
    res = b._get_pawn_moves_white(1,1,7)
    assert(len(res) == 0)

    res = b._get_pawn_moves_black(-1,6,7)
    assert(len(res) == 0)

    print("\twhite and black capture")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 0],
                [0, -1, 0, -1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_pawn_moves_white(1,1,2)
    exp = [((1, 2), (2, 3)), ((1, 2), (2, 1)), ((1, 2), (2, 2)), ((1, 2), (3, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

    res = b._get_pawn_moves_black(-1,2,3)
    exp = [((2, 3), (1, 3)), ((2, 3), (1, 4)), ((2, 3), (1, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_pawn_promotion():
    # todo: implement in game
    print("testing pawn promotion")
    b = Board()

    print("\tpromote, white")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, -999, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]

    promotion = ((6, 0), (7, 0), 'Q')
    assert(promotion in b.get_moves())
    b = b.apply_move(promotion)
    assert(b.board[7][0] == 9)

    print("\tpromote, black")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    promotion = ((1, 1), (0, 1), 'q')
    assert(promotion in b.get_moves())
    b = b.apply_move(promotion)
    assert(b.board[0][1] == -9)

    print("promote, white, capture")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, -999, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, -4, 0, 0, 0, 0, 0, 0]]
    promotion = ((6, 0), (7, 1), 'Q')
    assert(promotion in b.get_moves())
    b = b.apply_move(promotion)
    assert(b.board[7][1] == 9)

    print("\tpromote, black, capture")
    b.board = [[0, 0, 4, 0, 0, 0, 0, 999],
               [0, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    promotion = ((1, 1), (0, 2), 'q')
    assert(promotion in b.get_moves())
    b = b.apply_move(promotion)
    assert(b.board[0][2] == -9)

def test_en_passant():
    print("testing en-passant")
    b = Board()
    print("\ten-passant against white")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [-1, 0, -1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    b = b.apply_move(((1,1), (3,1)))
    assert(b.en_passant == 1)

    move = ((3, 2), (2, 1))
    assert(move in b.get_moves())
    c = b.apply_move(move)
    assert(c.board[3][1] == 0)
    assert(c.board[2][1] == -1)

    move = ((3,0),(2,1))
    assert(move in b.get_moves())
    c = b.apply_move(move)
    assert(c.board[3][1] == 0)
    assert(c.board[2][1] == -1)

    print("\ten-passant against black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    b = b.apply_move(((6,1), (4,1)))
    assert(b.en_passant == 1)

    move = ((4, 2), (5, 1))
    assert(move in b.get_moves())
    c = b.apply_move(move)
    assert(c.board[4][1] == 0)
    assert(c.board[5][1] == 1)

    move = ((4,0),(5,1))
    assert(move in b.get_moves())
    c = b.apply_move(move)
    assert(c.board[4][1] == 0)
    assert(c.board[5][1] == 1)

    print("\ten-passant missed, white")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [-1, 0, -1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    b = b.apply_move(((1,1), (3,1)))
    assert(b.en_passant == 1)
    b = b.apply_move(((5,6),(5,5)))
    assert(b.en_passant == 0)
    b = b.apply_move(((0,7),(1,7)))
    move = ((3, 2), (2, 1))
    assert(move not in b.get_moves())

    print("\ten-passant missed, black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 999],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, -999, 0],
               [0, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
    b = b.apply_move(((6,1), (4,1)))
    assert(b.en_passant == 1)
    b = b.apply_move(((0,7),(1,7)))
    assert(b.en_passant == 0)
    b = b.apply_move(((5,6),(5,5)))
    move = ((4, 2), (5, 1))
    assert(move not in b.get_moves())

def test_king_moves():
    # king can make any number of illegal moves by putting self
    # into check; ignore these, the heuristic should filter them out
    print("testing king moves")
    b = Board()

    print("\tevery direction")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 999, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -4, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_king_moves(999,3,3)
    exp = [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 2)), \
           ((3, 3), (4, 4)), ((3, 3), (2, 4)), ((3, 3), (4, 2)), ((3, 3), (2, 2))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))    

    print("\tcapture and block")
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 999, 1, 0, 0, 0],
                [0, 0, 1, -1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    
    res = b._get_king_moves(999,3,3)
    exp = [((3, 3), (4, 3))]
    [res.index(x) for x in exp]
    assert(len(res) == len(exp))

def test_check(): 
    print("testing check")
    print("\tin check, white")
    b = Board()
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, -9, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -4, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    assert(b.is_in_check())

    print("\tin check, black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 9, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, -999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 4, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 999]]
    assert(b.is_in_check())

    print("\tnot in check, white")
    b = Board()
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    assert(not b.is_in_check())

    print("\tnot in check, black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, -999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 999]]
    assert(not b.is_in_check())

    print("\topponent in check, white")
    b = Board()
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, 0, 0, 0, 0, -999]]
    assert(b.is_opponent_in_check())

    print("\topponent not in check, white")
    b = Board()
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 5, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    assert(not b.is_opponent_in_check())

    print("\topponent in check, black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    assert(b.is_opponent_in_check())

    print("\topponent not in check, black")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 999, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, -999]]
    assert(not b.is_opponent_in_check())
   
def test_castling():
    print("testing castling")
    print("\twhite, queen side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]

    b = b.apply_move(((0,4),(0,2)))
    assert(b.board[0][3] == 5)
    assert(b.castle == 12)

    print("\twhite, king side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((0,4),(0,6)))
    assert(b.board[0][5] == 5)
    assert(b.castle == 12)

    print("\tblack, queen side")
    b = Board()
    b.turn = -1
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]

    b = b.apply_move(((7,4),(7,2)))
    assert(b.board[7][3] == -5)
    assert(b.castle == 3)

    print("\tblack, king side")
    b = Board()
    b.turn = -1
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((7,4),(7,6)))
    assert(b.board[7][5] == -5)
    assert(b.castle == 3)

    print("\twhite, 86 queen side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((0,0),(0,1)))
    assert(b.castle == 14)

    print("\twhite, 86 king side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((0,7),(0,6)))
    assert(b.castle == 13)
    
    print("\twhite, 86 both")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((0,4),(0,5)))
    assert(b.castle == 12)

    print("\tblack, 86 queen side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((7,0),(7,1)))
    assert(b.castle == 11)

    print("\tblack, 86 king side")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((7,7),(7,6)))
    assert(b.castle == 7)
    
    print("\tblack, 86 both")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 1, 1, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [-1, -1, -1, 0, 0, -1, -1, -1],
               [-5, 0, 0, 0, -999, 0, 0, -5]]
    
    b = b.apply_move(((7,4),(7,5)))
    assert(b.castle == 3)

def test_castling_moves():
    print("testing castling move generation")
    print("\twhite, safe")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -999, 0, 0, 0, 0, 0, 0]]

    res = b.get_moves()
    [res.index(x) for x in [((0, 4), (0, 2)), ((0, 4), (0, 6))]]

    print("\twhite, obstructed")
    b = Board()
    b.board = [[5, 0, 4, 0, 999, 4, 0, 5],
               [1, 1, 0, 1, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 0, 0, 0, -5, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -999, 0, 0, 0, 0, 0, 0]]

    for move in b.get_moves():
        assert(move != ((0, 4), (0, 2)))
        assert(move != ((0, 4), (0, 6)))
    
    print("\twhite, threatened")
    b = Board()
    b.board = [[5, 0, 0, 0, 999, 0, 0, 5],
               [1, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -5, 0, 0, 0, 0, -5, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, -999, 0, 0, 0, 0, 0, 0]]

    for move in b.get_moves():
        assert(move != ((0, 4), (0, 2)))
        assert(move != ((0, 4), (0, 6)))

    print("\tblack, safe")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 999, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [-5, 0, 0, 0, -999, 0, 0, -5]]

    res = b.get_moves()
    [res.index(x) for x in [((7, 4), (7, 2)), ((7, 4), (7, 6))]]

    print("\tblack, obstructed")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 0, 0, 999, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [-5, 0, -4, 0, -999, -4, 0, -5]]

    for move in b.get_moves():
        assert(move != ((7, 4), (7, 2)))
        assert(move != ((7, 4), (7, 6)))

    print("\tblack, threatened")
    b = Board()
    b.turn = -1
    b.board = [[0, 0, 5, 0, 999, 0, 5, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [-5, 0, 0, 0, -999, 0, 0, -5]]

    for move in b.get_moves():
        assert(move != ((7, 4), (7, 2)))
        assert(move != ((7, 4), (7, 6)))

def main():
    print('')
    test_bishop_moves()
    test_knight_moves()
    test_rook_moves()
    test_queen_moves()
    test_pawn_moves()
    test_pawn_promotion()
    test_en_passant()
    test_king_moves()
    test_check()
    test_castling()
    test_castling_moves()

    print('')
    print("All Tests Passed")

if __name__ == "__main__":
    main()
