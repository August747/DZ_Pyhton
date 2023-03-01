import random


def display_board(board):
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Игрок'


def player_symbol():
    symbol = ''
    while symbol != 'X' and symbol != 'O':
        symbol = input('Выберите X или O: ').upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def player_move(board, symbol):
    while True:
        row = int(input('Введите номер строки (от 1 до 3): '))
        col = int(input('Введите номер столбца (от 1 до 3): '))
        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = symbol
            break
        else:
            print('Эта клетка уже занята, выберите другую.')


def computer_move(board, computer_symbol, player_symbol):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = computer_symbol
                if check_for_winner(board, computer_symbol):
                    return
                else:
                    board[i][j] = ' '
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player_symbol
                if check_for_winner(board, player_symbol):
                    board[i][j] = computer_symbol
                    return
                else:
                    board[i][j] = ' '
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = computer_symbol
            return


def computer_move_easy(board, computer_symbol):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = computer_symbol
            return


def check_for_winner(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def board_is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def check_for_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play_game():
    print('Добро пожаловать в игру Крестики-нолики!')
    difficulty_level = input('Выберете уровень сложности (легкий или сложный): ').lower()
    symbol = input('Вы выбираете X или O?: ').upper()
    while symbol != 'X' and symbol != 'O':
        print('Введенные данные не корректны, попробуйте еще раз.')
        symbol = input('Вы выбираете X или O?: ').upper()
    if symbol == 'X':
        computer_symbol = 'O'
    else:
        computer_symbol = 'X'
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    turn = choose_first()
    print(turn + ' ходит первым.')
    display_board(board)
    if difficulty_level == 'сложный':
        while True:
            if turn == 'Игрок':
                player_move(board, symbol)
                if check_for_winner(board, symbol):
                    display_board(board)
                    print('Вы выиграли! Поздравляем!')
                    break
                elif check_for_tie(board):
                    display_board(board)
                    print('Ничья!')
                    break
                turn = 'Компьютер'
            else:
                computer_move(board, computer_symbol, symbol)
                if check_for_winner(board, computer_symbol):
                    display_board(board)
                    print('Компьютер победил. Попробуйте еще раз!')
                    break
                elif check_for_tie(board):
                    display_board(board)
                    print('Ничья!')
                    break
                turn = 'Игрок'
                display_board(board)
    elif difficulty_level == 'легкий':
        while True:
            if turn == 'Игрок':
                player_move(board, symbol)
                if check_for_winner(board, symbol):
                    display_board(board)
                    print('Вы выиграли! Поздравляем!')
                    break
                elif check_for_tie(board):
                    display_board(board)
                    print('Ничья!')
                    break
                turn = 'Компьютер'
            else:
                computer_move_easy(board, computer_symbol)
                if check_for_winner(board, computer_symbol):
                    display_board(board)
                    print('Компьютер победил. Попробуйте еще раз!')
                    break
                elif check_for_tie(board):
                    display_board(board)
                    print('Ничья!')
                    break
                turn = 'Игрок'
                display_board(board)


play_game()
