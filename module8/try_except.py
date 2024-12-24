
i = int(input('введите число'))

try:
    result = 10 * (i * 1)
except ZeroDivisionError as exc:
    print('нельзя делить на ноль')
else:
    print('работаем дальше, на ноль не делим')
finally:
    print('закончили программу')
