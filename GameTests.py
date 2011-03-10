import Game

def test_str_to_move():
    print("testing string to move conversion")
    
    print("\tnormal move")
    move = Game.str_to_move('a1a2')
    assert(move == ((0, 0), (1, 0)))
    print("\tpromotion")
    move = Game.str_to_move('c7c8q')
    assert(move == ((6, 2), (7, 2), 'q'))
