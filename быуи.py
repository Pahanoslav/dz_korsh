import random

board = [[random.randint(1, 9),random.randint(1, 9) ,random.randint(1, 9)], [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)], [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]]
score1 = 0
score2 = 0


def draw_board(board, score1, score2):
    print('  0  1  2')
    print('  _______')
    num_row = 0
    for row in board:
        print(f'{num_row} |', end='')
        for column in row:
            print(f'{column}', end='|')
        print('\n  -------')
        num_row+=1
    print(f'Сумма очков первого игрка: {score1}')
    print(f'Сумма очков первого игрка: {score2}')


def check_digit_in_row(num_row):
    global board
    flag = 0
    for i in board[num_row]:
        if i != ' ':
            flag = 1
    if flag == 1:
        return True
    else:
        return False


def check_digit_in_column(num_column):
    global board
    flag = 0
    for i in range(3):
        if board[i][num_column] != ' ':
            flag = 1
    if flag == 1:
        return True
    else:
        return False



def player1_move(num_column):
    global BOARD
    global score1
    if check_digit_in_row(num_row):
        column = int(input(f'В строке {num_row} выберете столбец'))
        if board[num_row][column] != ' ':
            score1 += board[num_row][column]
            board[num_row][column] = ' '
        else:
            print('В данной ячейке нет числа. Повторите попытку')
            return True
    else:
        print('В строке нет цифр. Снова ходит второй игрок')
        return False

def player2_move(num_row):
    global BOARD
    global score1
    if check_digit_in_column(num_column):
        row = int(input(f'В строке {num_row} выберите строку'))
        if board[row][num_column] != ' ':
            score2 += board[num_row][column]
            board[row][num_column] = ' '
        else:
            print('В данной ячейке нет числа. Повторите попытку')
    else:
        print('В столбце нет цифр. Снова ходит первый игрок')


print('Старт')
draw_board(board, score1, score2)

row = int(input('Введите номер строки'))
column = int(input('Введите номер столбца'))

score1 += board[row][column]
board[row][column] = ' '

while True:
    last_row = player2_move(column)
    last_column = player1_move(row)

    if last_row is None and last_column is None:
        print('Игра окончена')

draw_board(board)
