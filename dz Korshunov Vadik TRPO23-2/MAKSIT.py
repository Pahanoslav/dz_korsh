import random
BOARD = [[random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)], [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)], [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]]
SCORE1 = 0
SCORE2 = 0


def draw_board(board, score1, score2):
    print('  0  1  2')
    print('  _______')
    num_row = 0
    for row in board:
        print(f'{num_row} |', end='')
        for column in row:
            print(f'{column}', end='|')
        print('\n  _______')
        num_row+=1
    print(f'Сумма очков первого игрока: {score1}')
    print(f'Сумма очков второго игрока: {score2}')
    print('--------------------------')

def check_digit_in_row(num_row):
    global BOARD
    flag = 0
    for i in BOARD[num_row]:
        if i != ' ' :
            flag = 1
    if flag == 1:
        return True
    else:
        return False


def check_digit_in_column(num_column):
    global BOARD
    flag = 0
    for i in range(3):
        if BOARD[i][num_column] != ' ':
            flag = 1
    if flag == 1:
        return True
    else:
        return False


def player1_move(num_row):
    global BOARD
    global SCORE1
    print('Ход первого игрока')
    if check_digit_in_row(num_row):
        while True:
            column = int(input(f'В строке {num_row} выберете столбец'))
            if BOARD[num_row][column] != ' ':
                SCORE1 += BOARD[num_row][column]
                BOARD[num_row][column] = ' '
                break
            else:
                print('В данной ячейке нет числа. Повторите попытку')
        return column
    else:
        print('В строке нет цифр. Снова ходит второй игрок')
        return None


def player2_move(num_column):
    global BOARD
    global SCORE2
    print('Ход второго игрока')
    if check_digit_in_column(num_column):
        while True:
            row = int(input(f'В столбце {num_column} выберете строку'))
            if BOARD[row][num_column] != ' ':
                SCORE2 += BOARD[row][num_column]
                BOARD[row][num_column] = ' '
                break
            else:
                print('В данной ячейке нет числа. Повторите попытку')
        return row
    else:
        print('В столбце нет цифр. Снова ходит первый игрок')
        return None



print('Старт')
draw_board(BOARD, SCORE1, SCORE2)

row = int(input('Введите номер строки'))
column = int(input('Введите номер столбца'))

SCORE1 += BOARD[row][column]
BOARD[row][column] = ' '

last_row = row
last_column = column
while True:
    last_row = player2_move(last_column)
    draw_board(BOARD, SCORE1, SCORE2)
    last_column = player1_move(last_row)
    draw_board(BOARD, SCORE1, SCORE2)
    if last_row is None and last_column is None:
        print('Игра закончена')
        break


