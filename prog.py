board = [' ' for i in range(9)]

# Display the board
def display():
    print("Your are playing as 'O'\n")
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print("---------")

# Check winner
def winner(player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in win:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

# DFS function
def dfs(player):
    if winner('X'):
        return 1
    if winner('O'):
        return -1
    if ' ' not in board:
        return 0

    if player == 'X':
        best = -2
    else:
        best = 2

    for i in range(9):
        if board[i] == ' ':
            board[i] = player

            if player == 'X':
                score = dfs('O')
                best = max(best, score)
            else:
                score = dfs('X')
                best = min(best, score)

            board[i] = ' '  # Undo move

    return best

# Find best move
def best_move():
    best = -2
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = dfs('O')
            board[i] = ' '

            if score > best:
                best = score
                move = i

    return move

# Main game
while True:
    display()

    move = int(input("Enter position (0-8): "))

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'O'

    if winner('O'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break

    move = best_move()
    board[move] = 'X'

    if winner('X'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break
