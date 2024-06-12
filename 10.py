#Sum of primes
import math
def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

res = 0
for i in range(1, 2000001):
    if is_prime(i):
        res += i

print(res)
