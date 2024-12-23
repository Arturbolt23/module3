my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
positive_list = []
while index < len(my_list):
    current = my_list[index]
    if current < 0:
        break
    if current > 0:
        positive_list.append(current)
    index += 1
print(positive_list)

