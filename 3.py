"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

num = 600851475143
factor = 0

for i in range(3, int(math.sqrt(num / 2)) + 1, 2):
    while num % i == 0:
        factor = i
        num /= i

print(factor)