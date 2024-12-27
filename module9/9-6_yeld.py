def all_variants(text):
    length = len(text)
    for start in range(length):  # Начальная позиция
        for end in range(start + 1, length + 1):  # Конечная позиция
            yield text[start:end]  # Возвращаем подстроку

a = all_variants("abc")

for i in a:
    print(i)
