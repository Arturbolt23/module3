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
zp = zip(list_1, list_2) # создвние кортежа из двух списков
mp = map(str, list_1)   # какую функцию к чему берем


print(ran, mp, zp)

print(list(ran))
print(list(zp))
print(list(mp))

def fibonachi(n):
    res = []
    a, b = 0, 1
    for i in range(n):
        res.append(a)
        a, b = b, a + b
    return res
for value in fibonachi(15):

    print(value, end=' ')
