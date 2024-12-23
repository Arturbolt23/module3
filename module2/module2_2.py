first = int(input('введите первое число :'))
second = int(input('введите второ число : '))
third = int(input('введите третье число :'))
if first == second == third:
    print("совпадений: ", 3)
elif (first == second and first != third) or (second == third and second != first) or (first != second and first == third) :
    print("совпадений :", 2)
else:
    print("совпадений :", 0)