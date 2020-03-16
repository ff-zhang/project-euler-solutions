"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def find_prime_factors(num, primes):
    factors = {}

    for prime in primes:
        while num % prime == 0:
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1
            
            num /= prime
    
    return factors

factors = [x+1 for x in range(20)]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

gcm = {k: 0 for k in primes}
for factor in factors:
    prime_factors = find_prime_factors(factor, primes)
    for key, value in prime_factors.items():
        if gcm[key] < value:
            gcm[key] = value

final = 1
for key, value in gcm.items():
    final *= key ** value

print(final)