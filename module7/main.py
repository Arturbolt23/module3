# '''
# переводим строку в список ASCII
# '''
# a = input('введите ваше предложение') # ASCII
# print(ord('h'))
# q = chr(40) # вывод элемента по номеру
# print(q)
# chars = []
# for i in a:
#     chars.append(ord(i))
# print(chars)
# # собираем обратно в строку
#
# s = ''
# for i in chars:
#     s += chr(i)
# print(s)
#
# '''
# переводим в битовую систему? 16 ричная
# '''
# # a = 'Hello' # ASCII
# chars = []
# for i in a:
#     chars.append(hex(ord(i)))
# print(chars)

# str = '+'.join(chars)
# print(str)
#
# # собираем обратно
# res = str.split('+')
# print(res)
#
#
'''список кодировки 128 элементов'''
from os import mkdir, chdir

# # for i in range(128):
# #     print(chr(i))
#
#
# # for i in range(1040, 1200):
# #     print(chr(i))



# bb = b'\x48' # декодирование одного элемента
# print(bb.decode())
'''
открытие файлов
'''
from pprint import pprint

name = ('sample2.txt')
file = open(name, 'r') # r, w, a
# file = open(name, 'w') # r, w, a
# file.write('\n Boss')
print(file.tell()) # посмотреть курскор где
pprint(file.read())
print(file.tell())
pprint(file.read())
pprint(file.seek(15))
pprint(file.read())# передвинуть курсор на позицию
file.close()

import os
print('текущая директория:', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('текущая директория:', os.getcwd())
# os.makedirs(r'third\fourth')
for i in os.walk('.'): # смотрим вложенность
    print(i)
print(os.listdir())
os.chdir(r'D:\pythonProject1\module7')
print('текущая директория:', os.getcwd())
# print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [ d for d in os.listdir() if os. path.isdir(d)]
print(dirs)
print(file)
# os.startfile(file[6]) # запустили файл по индексу
# print(os.stat(file[6])) # вывести информацию о файле
os.system('pip install random2')




