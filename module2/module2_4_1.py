numbers = list(range(100))
primes = []
not_primes = []
for i in numbers:
    if i <= 1:
        continue
    if i <= 3:
        primes.append(i)
        i += 1
        continue
    is_prime = True
    for g in range(2, i):
        if i % g == 0:
            not_primes.append(i)
            is_true = False
            break
    else:
         primes.append(i)
print('простые числа :' ,primes)
print('составные числа : ',not_primes)