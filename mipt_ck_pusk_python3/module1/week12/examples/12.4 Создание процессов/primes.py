import math
import time

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

numbers = [
    10101010101011,
    87784138523761,
    99194853094755497,
    100001010101010101,
    229442531844556801,
    489133282872437279,
    909090909090909091,
    18446744073709551617,
]


def check(n):
    t0 = time.perf_counter()
    p = is_prime(n)
    t = time.perf_counter() - t0
    if p:
        print(f'{n} is prime, {t:.2f} sec.')
    else:
        print(f'{n} is not prime, {t:.2f} sec.')


start = time.perf_counter()
for n in numbers:
    check(n)
end = time.perf_counter()
print(f'check for {len(numbers)} numbers took {end-start:.2f} sec.')
