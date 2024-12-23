
def check_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O':
        return 'O'
    if area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][0] == 'O':
        return 'O'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][1] == 'O' and area[2][0] == 'O':
        return 'O'
    return 'ничья'

def Draw_area():
    for i in area:
        print(*i)
    print()

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики и нолики')
Draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = 'O'
        print('ходят нолики')
    else:
        turn_char = 'X'
        print('Ходять крестики')
    while True:
        row = int(input('Insetr number of row(1,2,3)')) - 1
        if row in [0, 1, 2]:
            break
        print('ввели недопустимое число')
    while True:
        column = int(input('insert number column(1, 2, 3)')) - 1
        if column  in [0, 1, 2]:
            break
        print('ввели недопустимое число')
    while True:
        if area[row][column] == '*':
            area[row][column] = turn_char
            Draw_area()
            break
        else:
            print('ячейка занята, снова')
            Draw_area()
            while True:
                row = int(input('Insetr number of row(1,2,3)')) - 1
                if row in [0, 1, 2]:
                    break
                print('ввели недопустимое число')
            while True:
                column = int(input('insert number column(1, 2, 3)')) - 1
                if column in [0, 1, 2]:
                    break
                print('ввели недопустимое число')


    if check_winner() == 'X':
        print('победа крестиков')
        break
    if check_winner() == 'O':
        print('победа ноликов')
        break
    if check_winner() == '*' and turn ==9:
        print('ничья')

