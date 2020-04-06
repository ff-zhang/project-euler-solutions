"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from itertools import chain

abundant_nums = []

for num in range(1, 28124):
    factors = chain.from_iterable([[i, num//i] for i in range(1, int(num ** 0.5) + 1) if num % i == 0])
    proper_factors = sum(set(factors)) - num

    if proper_factors > num:
        abundant_nums.append(num)

nums = [True for i in range(28124)]

for abundant_num1 in abundant_nums:
    for abundant_num2 in abundant_nums:
        try:
            nums[abundant_num1 + abundant_num2] = False
        except IndexError:
            pass

total = 0

for i, not_abundant_sum in enumerate(nums):
    if not_abundant_sum:
        total += i

print(total)