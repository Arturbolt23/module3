# Задача "Матрица воплоти":
#
# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
#
#
#
# Пункты задачи:
#
# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.
#
#
# Пример результата выполнения функции:
#
# Исходный код:
#
# result1 = get_matrix(2, 2, 10)
#
# result2 = get_matrix(3, 5, 42)
#
# result3 = get_matrix(4, 2, 13)
#
# print(result1)
#
# print(result2)
#
# print(result3)

#n, m, value = int(input('введите количество строк')), int(input('введите количество столбцов')), int(input('введите число'))
def get_matrix(n, m, value):
#    n, m, value = int(input('введите количество строк')), int(input('введите количество столбцов')), int(input('введите число'))
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
res = get_matrix(int(input('введите количество строк')), int(input('введите количество столбцов')), int(input('введите число')))
print('zour matrix in a Row :', res)
print('Your matrix in readable case :')
for i in res:
     print(i)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('задача из дз: ', result1)
print('задача из дз: ', result2)
print('задача из дз: ', result3)


