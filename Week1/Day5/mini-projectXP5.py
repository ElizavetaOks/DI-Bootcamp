# Mini-Project - Tic Tac Toe
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

board = [1,2,3,4,5,6,7,8,9]

print('Welcome to TIC TAC TOE!')

def display_board():
    print("*"*13)
    for i in range(3):
        print('*' + (' '* 3 +'|')*2 + " "*3 + '*')
        print('*'+'',board[i*3], '|', board[1 + i*3], '|', board[2 + i*3], '*')
        print('*'+('-'*3+'|')*2+'-'*3+'*')
    print("*"*13)

def player_input(move, char):
    if (move > 9 or move < 1 or board[move - 1] in ("X", "O")):
        return False
    
    board[move -1] = char
    return True

def check_win():
    win = False
    win_combination = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def play():
    player = 'X'
    step = 1
    display_board()

    while (step <10) and (check_win() == False):
        move = input(f"Your turn to move {player}: " )
        
        if (player_input(int(move), player)):
            #print('Good move')

            if player == 'X':
                player = 'O'
            else:
                player = 'X'

            display_board()
            step += 1 
        else:
            print('Wrong move. Try again')

    if (step == 10):
        print("Game over! No one wins!")
    else:
        print('Win '+ check_win() + '!!!')     

play()
