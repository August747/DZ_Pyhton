import random


def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


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
        x = int(input('Введите номер ячейки (от 1 до 9): '))
        if board[x - 1] == ' ':
            board[x - 1] = symbol
            break
        else:
            print('Эта клетка уже занята, выберите другую.')


def computer_move(board, computer_symbol, player_symbol):
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_symbol
            if check_for_winner(board, computer_symbol):
                return
            else:
                board[i] = ' '
    for i in range(9):
        if board[i] == ' ':
            board[i] = player_symbol
            if check_for_winner(board, player_symbol):
                board[i] = computer_symbol
                return
            else:
                board[i] = ' '
    while True:
        x = random.randint(0, 8)
        print(x)
        if board[x] == ' ':
            board[x] = computer_symbol
            return


def computer_move_easy(board, computer_symbol):
    while True:
        x = random.randint(0, 8)
        print(x)
        if board[x] == ' ':
            board[x] = computer_symbol
            return


def check_for_winner(board, symbol):
    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True
    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[6] == board[4] == board[2] == symbol:
        return True
    return False


def board_is_full(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True


def check_for_tie(board):
    for cell in board:
        if cell == ' ':
            return False
    return True


def hard_game(board, turn, symbol, computer_symbol):
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


def ez_game(board, turn, symbol, computer_symbol):
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
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    turn = choose_first()
    print(turn + ' ходит первым.')
    if difficulty_level == 'сложный':
        hard_game(board, turn, symbol, computer_symbol)
    elif difficulty_level == 'легкий':
        ez_game(board, turn, symbol, computer_symbol)

play_game()
