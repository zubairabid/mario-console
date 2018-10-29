from gamestate import Game

def test_game_init_with_proper_params():
    '''
    Checks for proper initialization of Game
    '''

    GAME = Game(0, 100, 1)
    PLAYER_POS_I = GAME.player.i
    PLAYER_POS_J = GAME.player.j
    PLAYER_SIZE_I = GAME.player.get_size()[0]
    PLAYER_SIZE_J = GAME.player.get_size()[1]

    # Check time allocated is correct
    assert GAME.etime - GAME.stime == 100

    # Checking that Mario exists within bounds
    for i in range(PLAYER_POS_I+1-PLAYER_SIZE_I, PLAYER_POS_I+1):
        for j in range(PLAYER_POS_J-1, PLAYER_POS_J-1+PLAYER_SIZE_J):
            assert GAME.screen.gmap[i, j] == 5
