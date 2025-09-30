import math

# Board is a list of 9 cells, empty = ' ', X = player, O = AI
board = [' ' for _ in range(9)]

def print_board(b):
    for i in range(0, 9, 3):
        print(b[i] + '|' + b[i+15] + '|' + b[i+2])
    print()

# Check for winner
def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b_,c in wins:
        if board[a]==board[b_]==board[c] and board[a]!=' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

# Minimax function
def minimax(b, depth, is_max):
    result = check_winner(b)
    if result == 'O': return 1
    elif result == 'X': return -1
    elif result == 'Tie': return 0

    if is_max:
        best_score = -math.inf
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                score = minimax(b, depth+1, False)
                b[i]=' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                score = minimax(b, depth+1, True)
                b[i]=' '
                best_score = min(score, best_score)
        return best_score

# AI move
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score = minimax(board, 0, False)
            board[i]=' '
            if score > best_score:
                best_score = score
                move = i
    board[move]='O'

# Simple game simulation
print_board(board)
while True:
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move]==' ':
        board[player_move]='X'
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Winner:", winner)
            break
        best_move()
        winner = check_winner(board)
        print_board(board)
        if winner:
            print("Winner:", winner)
            break
