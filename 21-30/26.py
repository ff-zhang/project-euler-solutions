"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
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

primes = find_primes(1000)
primes.remove(2)
primes.remove(5)

result = (0, 0)
for p in primes:
    # 10 ^ k = 1 (mod p)
    k = 1
    while 10 ** k % p != 1:
        k += 1

    if k > result[1]:
        result = (p, k)

print(result)