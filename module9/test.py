# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# res = {x for x in my_numbers} # создание множества
# print(res)
#
# tey_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# res = {x: x**2 for x in my_numbers }
# print(res)

list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 6, 7, 8, 9]

ran = range(10, 20)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, mp, zp)

print(list(ran))
print(list(zp)) # создвние кортежа из двух списков
print(list(mp)) 
