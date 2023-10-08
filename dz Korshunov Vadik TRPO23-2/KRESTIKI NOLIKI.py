
BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def draw_board(board):
    print('  0  1  2')
    print('  _______')
    num_row = 0
    for row in board:
        print(f'{num_row} |', end='')
        for column in row:
            print(f'{column}', end='|')
        print('\n  _______')
        num_row+=1


def cross_move():
    global BOARD
    print('Ход крестика')
    row = int(input('Введите номер строки '))
    if 0 <= row <= 2:
        pass
    else:
        print('Некорректная строка. Попробуйте еще раз')
        cross_move()

    column = int(input('Введите номер столбца '))
    if 0 <= row <= 2:
        pass
    else:
        print('Некорректный столбец. Попробуйте еще раз')
        cross_move()

    if BOARD[row][column] == ' ':
        BOARD[row][column] = 'X'
    else:
        print('Поле уже занято. Попробуйте еще раз')
        cross_move()


def zero_move():
    global BOARD
    print('Ход нолика')
    row = int(input('Введите номер строки '))
    if 0 <= row <= 2:
        pass
    else:
        print('Некорректная строка. Попробуйте еще раз')
        cross_move()

    column = int(input('Введите номер столбца '))
    if 0 <= row <= 2:
        pass
    else:
        print('Некорректный столбец. Попробуйте еще раз')
        zero_move()

    if BOARD[row][column] == ' ':
        BOARD[row][column] = '0'
    else:
        print('Поле уже занято. Попробуйте еще раз')
        cross_move()


def check_win():
    global BOARD
    for row in BOARD:
        if row[0] == row[1] == row[2] != ' ':
            if row[0] == 'X':
                print('Крестики победили')
            else:
                print('Нолики победили')
            return True
    for column in range(3):
        if BOARD[0][column] == BOARD[1][column] == BOARD[2][column] != ' ':
            if BOARD[0][column] == 'X':
                print('Крестики победили')
            else:
                print('Нолики победили')
            return True
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != ' ':
        if BOARD[0][0] == 'X':
            print('Крестики победили')
        else:
            print('Нолики победили')
        return True
    if BOARD[2][0] == BOARD[1][1] == BOARD[0][2] != ' ':
        if BOARD[2][0] == 'X':
            print('Крестики победили')
        else:
            print('Нолики победили')
        return True


def play_game():
    global BOARD
    BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print('Начало игры')
    move = 0
    while True:
        draw_board(BOARD)
        if move % 2 == 0:
            zero_move()
            move += 1
        else:
            cross_move()
            move += 1
        if check_win():
            draw_board(BOARD)
            print('Игра закончена')
            restart = input('Хотите начать заново(да/нет)')
            if restart == 'Да':
                play_game()
            else:
                break


play_game()
