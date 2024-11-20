calls = 0

def count_call():
    global calls
    calls += 1
    print(calls)
    return

def string_info():
    string = input('введите любое слово ')
    string_0 = len(string)
    string_1 = string.upper()
    string_2 = string.lower()
    tuple_ = (string_0, string_1, string_2)
    print(tuple_)
    count_call()

a = string_info()
#def is_contains(string, list_to_search):
def is_contains():
    string = input('введите любое слово ').lower()
#    string = string.lower()
    list_to_search = input('введите список слов которые надо искать ').lower()
#    list_to_search_list = [word.lower() for word in list_to_search]
    list_to_search_list = list_to_search.lower().split()
    for word in list_to_search_list:
        if word in string:
            print(True)
            count_call()
            return
    print(False)
    count_call()
b = is_contains()



print(calls)