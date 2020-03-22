"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

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

print(sum(find_primes(2000000)))
