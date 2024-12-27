
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print('не простое и не составное')
        else:
            for  i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print('Составное')
                    return result
            print('простое')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    a = 0
    for i in args:
        a += i
    return a

print(sum_three(2, 3, 6))