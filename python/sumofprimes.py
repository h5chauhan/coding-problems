#Sum of Primes
import math
def is_prime(num):
    if num <= 1:
        return False
    else if num <= 3:
        return True

    _sqrt = math.floor(math.sqrt(num))
    n = 2
    while n < _sqrt:
