def player_won(board, occupant):
    for i in range(len(board)):
        if board[i] == [occupant, occupant, occupant]:
            return True

    diagnal_win = 0
    diagnal_win2 = 0
    for i in range(len(board)):
        if board[i][i] == occupant:
            diagnal_win += 1
        if diagnal_win == 3:
            return True
        for j in range(len(board) - 1, -1, -1):
            if board[i][j] == occupant:
                diagnal_win2 += 1
            if diagnal_win2 == 3:
                return True
        if i == 2:
            diaganol_win = 0
            diaganol_win2 = 0

    for j in range(len(board)):
        win = 0
        for i in range(len(board)):
            if board[i][j]:
                win += 1
        if win == 3:
            return True
    return False
def print_board(board):
    for i in board:
        print(i)
    print("")

def player_move(board):
    x = int(input())
    y = int(input())
    board[x][y] = 1
    print_board(board)


def computer_alg(board):
    if comp_attack(board):
        print_board(board)
        return True

def comp_defence():
    pass

def comp_attack(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board_ = board
            if board_[i][j] == 0:
                board_[i][j] = 2
                if player_won(board_, 2):
                    return True
                else:
                    board_[i][j] = 0
    return False


def comp_optimum():
    pass


def main():
    print("The computer places 2, you place 1 and 0 means the place is empty")
    board = [[2, 0, 0], [0, 0, 0], [2, 0, 0]]
    print_board(board)
    player_move(board)
    while True:
        if computer_alg(board):
            print("Computer Wins")
            break
        player_move(board)
        player_won(board, 1)
        if player_won(board, 1):
            print("You Win")
            break
        else:
            print("you haven't won yet")

main()
