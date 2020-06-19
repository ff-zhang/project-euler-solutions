"""
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.""
"""
from math import sqrt

def find_primes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    primes = []

    for (i, is_prime) in enumerate(sieve):
        if is_prime:
            for j in range(2 * i, n, i):
                sieve[j] = False
            
            primes.append(i)
    
    return primes

def is_prime(n):
    if n <= 0:
        return False
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

a_options = [i for i in range(1, 1000, 2)]
b_options = find_primes(1000)

result = ([0, 0], 0)

for a in a_options:
    for b in b_options:
        # positive a and positive b
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1

        if n > result[1]:
            result = ([a, b], n)

        # negative a and positive b
        n = 0
        while is_prime(n**2 - a*n + b):
            n += 1
        
        if n > result[1]:
            result = ([-a, b], n)

print(result[0][0] * result[0][1])
