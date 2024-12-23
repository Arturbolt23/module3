immutable_var = (1, 2, 3, [4, 5, 6], True)
print(immutable_var)
print(type(immutable_var))
# кортеж не изменяемый, изменим в кортеже в списке один из элементов
immutable_var[3][1] = 77
print(immutable_var)
print(len(immutable_var))
print(immutable_var[3]) # вывели список из кортежа
print(immutable_var[::-1]) # развернул кортеж
a = immutable_var[3] # хочу развернуть список в кортеже
print(a[::-1]) # развернул, а как его запихнуть обратно в кортеж пока не понял
mutable_list = [10, 11, 12, 13, "name" , "age"]
mutable_list[0] = 100
mutable_list[4] = "surname name"
print(immutable_var)
print(mutable_list)

