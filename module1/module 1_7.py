# #Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

# Примечания:
#
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students ={'Jony', 'Bilbo', 'Steave', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average1 = sum(grades[0]) / len(grades[0])
average2 = sum(grades[1]) / len(grades[1])
average3 = sum(grades[2]) / len(grades[2])
average4 = sum(grades[3]) / len(grades[3])
average5 = sum(grades[4]) / len(grades[4])
average_grades = (average1 , average2, average3, average4, average5)
print(average_grades)
my_dict = dict(zip(sorted_students , average_grades)) # zip - собирает пары элементов
print(my_dict)
