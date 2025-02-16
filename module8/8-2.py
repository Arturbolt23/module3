def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    if not isinstance(numbers, (list, tuple)):
        return None

    for num in numbers:
        try:
            if isinstance(num, (int, float)):
                result += num
            else:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num}')

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        print("В numbers записан некорректный тип данных")
        return None

    result, incorrect_data = personal_sum(numbers)

    if result is not None and incorrect_data == 0:
        try:
            return result / len(numbers)
        except ZeroDivisionError:
            return 0
    else:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')



