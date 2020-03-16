"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a ^ 2 + b ^ 2 = c ^ 2
For example, 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

triplet = ()

r = 0
while not triplet:
    # Dickson's method for generating Pythagorean triples
    # r ** 2 = 2 * s * t
    # a = r + s, b = r + t, c = r + s + t

    factors = []
    r1 = r ** 2 / 2
    for s in range(1, int(sqrt(r1)) + 1):
        if r1 % s == 0:
            factors.append((s, int(r1 / s)))

    for factor in factors:
        a, b, c = r + factor[0], r + factor[1], r + factor[0] + factor[1]
        if a + b + c == 1000:
            triplet = (a, b, c)

    r += 2

print(triplet[0] * triplet[1] * triplet[2])
