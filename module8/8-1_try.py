import os

a = input('введите первое значение:')
b = input('введите второе значение:')

def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        return str(a) + str(b)


try:
    a = float(a)
except ValueError:
    pass

try:
    b = float(b)
except ValueError:
    pass


print('итог работы функции - ',add_everything_up(a, b)) # выводим результат введенных пользователем значений

print('выводы из задания ниже')
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))