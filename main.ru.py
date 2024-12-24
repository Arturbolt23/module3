#print('Hi, PyCharm')
#
# x = 43
#
# y = 32
#
# print(x * y)
#
# print("End line")
# def test(a = 2, b = True):
#     print(a, b)
#*************************************************#
# import random
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     while len(tickets) > 2:
#         win = random.choice(tickets)
#         print(win)
#         tickets.remove(win)
#     print('pre-last winner ticket :', tickets[1])
#     print('not_worked:', tickets[0])
# lottery()
#***********************************************8#

#****************************************************#
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
#
# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
#
# print(total)
# ******************************************************
# num = 42
# def some(n):
#     n = n + 10
#     print(n)
#
#  some(55)
# *********************************************************
'''сортировка по длинне элементов в списке'''
# words = ["banana", "apple", "cherry", "date"]
# sorted_words = sorted(words, key=lambda x: len(x))
# sorted_words_2 = sorted(words, key=len)
# print(sorted_words)
# print(sorted_words_2)
#**********************************************************
# import dis
#
# def some_func(a, b):
#     return a + b
#
# dis.dis(some_func)


#
# def example_function(a, b):
#     return a + b
#
# # Дизассемблирование функции
# dis.dis(example_function)
# работа с фалами и дирректориями

# import os
#
# print(os.listdir())
# print(os.getcwd())
# if os.path.exists('module8'):
#     os.chdir('module8')
# else:
#     os.mkdir('module8')
#     os.chdir('module8')
# print(os.getcwd())