my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
res = {x for x in my_numbers} # создание множества
print(res)

tey_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
res = {x: x**2 for x in my_numbers }
print(res)