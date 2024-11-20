def calculate_structure_sum(data):
    total = 0

    # Проверяем каждый элемент внутри структуры
    if isinstance(data, (list, tuple, set)):
        # Если это список, кортеж или множество, обрабатываем каждый элемент
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict):
        # Если это словарь, обрабатываем ключи и значения
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)
    elif isinstance(data, str):
        # Если это строка, добавляем её длину
        total += len(data)
    elif isinstance(data, int):
        # Если это число, добавляем его значение
        total += data

    return total


# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции
result = calculate_structure_sum(data_structure)
print(result)