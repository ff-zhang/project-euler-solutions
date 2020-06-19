"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def is_pandigital(num):
    nums = [i for i in range(1, len(str(num)) + 1)]
    test = sorted([int(s) for s in str(num)])

    if nums == test:
        return True
    
    return False

result = set()

for i in range(1, 987654321):
    for j in range(1, 987654321):
        test_num = int(str(i) + str(j) + str(i * j))
        if is_pandigital(test_num):
            result.add(i * j)

print(sum(result))