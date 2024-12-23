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




