def calculate_data_structure(data):
    sum_ = 0
    count = 0

    if isinstance(data, (list, set, tuple)):
        for item in data:
            s, c, _ = calculate_data_structure(item)
            sum_ += s
            count += c
    elif isinstance(data, str):
        count += len(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            k_sum_, k_count, _ = calculate_data_structure(key)
            v_sum_, v_count, _ = calculate_data_structure(value)
            sum_ += k_sum_ + v_sum_
            count += k_count + v_count
    elif isinstance(data, (int, float)):
        sum_ += data

    total_sum = count + sum_
    return sum_, count, total_sum

# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции
sum_, count, tota = calculate_data_structure(data_structure)
print('Число символов в строках:', count)
print('Сумма чисел:', sum_)
print('Общая сумма всех элементов:', tota)
