from copy import deepcopy

def player_won(board, occupant):
    for i in range(len(board)):
        if board[i] == [occupant, occupant, occupant]:
            return True

    diagonal_win = 0
    diagonal_win2 = 0
    for i in range(len(board)):
        if board[i][i] == occupant:
            diagonal_win += 1
        if board[i][2-i] == occupant:
            diagonal_win2 += 1
    if diagonal_win == 3 or diagonal_win2 == 3:
        return True

    for i in range(len(board)):
        win = 0
        for j in range(len(board)):
            if board[j][i] == occupant:
                win += 1
        if win == 3:
            return True
    return False

def print_board(board):
    for i in board:
        print(i)
    print()

def player_move(board):
    x = int(input())
    y = int(input())
    if board[x][y] != 0:
        print("please play on a empty square")
        player_move(board)
    board[x][y] = 1
    print_board(board)
    return board

def comp_defence(inp_board):
    for i in range(len(inp_board)):
        for j in range(len(inp_board)):
            if inp_board[i][j] == 0:
                board_ = deepcopy(inp_board)
                board_[i][j] = 1
                if player_won(board_, 1):
                    board_[i][j] = 2
                    return True, board_
    return False, inp_board

def comp_attack(inp_board):
    for i in range(len(inp_board)):
        for j in range(len(inp_board)):
            if inp_board[i][j] == 0:
                board_ = deepcopy(inp_board)
                board_[i][j] = 2
                if player_won(board_, 2):
                    return True, board_
    return False, inp_board

def comp_optimum(inp_board):
    if  inp_board == [[1, 0, 0], [0, 2, 0], [0, 0, 1]] or inp_board == [[0, 0, 1], [0, 2, 0], [1, 0, 0]]:
             inp_board[0][1] = 2
             return inp_board
    if inp_board == [[2, 0, 0], [0, 1, 0], [0, 0, 1]]:
        inp_board[0][2] = 2
        return inp_board

    possible_wins = 0
    possible_wins_ = 0
    row_ = 0
    column_ = 0
    row = 0
    column = 0
    for i in range(len(inp_board)):
        for j in range(len(inp_board)):
            board_ = deepcopy(inp_board)
            if inp_board[i][j] == 0:
                board_[i][j] = 2
                possible_wins_, row_, column_ = possible_win(board_, i, j, possible_wins)
                if possible_wins < possible_wins_:
                    possible_wins = deepcopy(possible_wins_)
                    row = deepcopy(row_)
                    column = deepcopy(column_)
    inp_board[row][column] = 2
    return inp_board

def possible_win(board, row, column, max_possible_win):
    possible_wins = 0
    win_row = 0
    for i in range(len(board)):
        if board[i][column] == 2 or board[row][i] == 0:
            win_row += 1
    if win_row == 3:
        possible_wins += 1
    win_column = 0
    for i in range(len(board)):
        if board[row][i] == 2 or board[row][i] == 0:
            win_column += 1
    if win_column == 3:
        possible_wins += 1
    diagonal_win = 0
    diagonal_win2 = 0
    for i in range(len(board)):
        if board[i][i] == 0 or board[i][i] == 2:
            diagonal_win += 1
        if board[i][2-i] == 0 or board[i][2-i] == 2:
            diagonal_win2 += 1
    if diagonal_win == 3:
        possible_wins += 1
    if diagonal_win2 == 3:
        possible_wins += 1
    if possible_wins > max_possible_win:
        return possible_wins, row, column
    else:
        return max_possible_win, row, column

# def comp_2attack(inp_board):
#     if  inp_board == [[1, 0, 0], [0, 2, 0], [0, 0, 1]] or inp_board == [[0, 0, 1], [0, 2, 0], [1, 0, 0]]:
#         inp_board[0][1] = 2
#         return True, inp_board
#     for i in range(len(inp_board)):
#         for j in range(len(inp_board)):
#             if inp_board[i][j] == 0:
#                 board = deepcopy(inp_board)
#                 board[i][j] = 2
#                 if double_attack_check(board):
#                     board[i][j] = 2
#                     return True, board
#     return False, inp_board
#
# def double_attack_check(board):
#     attacks_possible = 0
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 0:
#                 board_ = deepcopy(board)
#                 board_[i][j] = 1
#                 if player_won(board_, 1):
#                     attacks_possible += 1
#     if attacks_possible >= 2:
#         return True
#     return False

def main():
    print("The computer places 2, you place 1 and 0 means the place is empty")
    global_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print_board(global_board)
    squares_full = 0
    while True:
        global_board = player_move(global_board)
        squares_full += 1
        if squares_full == 9:
            print("Draw")
            break
        if player_won(global_board, 1):
            print("You Win")
            break
        print("you haven't won yet")

        comp_won, new_board = comp_attack(global_board)
        if comp_won:
            print_board(new_board)
            print("Computer Wins")
            break

        # comp_double, new_board = comp_2attack(global_board)
        # if comp_double:
        #     global_board = deepcopy(new_board)

        comp_def, new_board = comp_defence(global_board)
        if comp_def:
            global_board = deepcopy(new_board)

        else:
            new_board = comp_optimum(global_board)
            global_board = deepcopy(new_board)

        print_board(global_board)
        squares_full += 1

main()
