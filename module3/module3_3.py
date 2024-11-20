def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10, 55)
print_params(c=False)
print_params('string', 40, 675)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['str', True, 15]
values_dict = {'a': 'something', 'b': 555, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25.52, None]
print_params(*values_list_2, 42)