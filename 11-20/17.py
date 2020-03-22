"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def main(num):
    unique_names = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", 
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen","seventeen", "eighteen", "nineteen"
    ]

    unique_names = list(map(len, unique_names))
    unique_names.insert(0, 0)

    unique_tenth = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    unique_tenth = list(map(len, unique_tenth))

    len_str_num = 0

    hundreds, tens_ones = num // 100, num % 100

    if hundreds:
        if hundreds == 10:
            len_str_num += unique_names[1] + len("thousand")

        elif tens_ones != 0:
            len_str_num += unique_names[hundreds] + len("hundredand")

        else:
            len_str_num += unique_names[hundreds] + len("hundred")
    
    if tens_ones < 20:
        len_str_num += unique_names[tens_ones]

    else:
        tens, ones = tens_ones // 10 - 2, tens_ones % 10
        len_str_num += unique_tenth[tens] + unique_names[ones]
    
    return len_str_num

total = 0
for i in range(1000):
    total += main(i+1)

print(total)