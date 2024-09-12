#Consider the variable x valued between 1 and 1000 (inclusive, integers). How many times does the square-root of x contain 8 as the third digit, no rounding and ignoring the decimal point—i.e. the third digit of 12.495 is 4.
import math

count = 0
for i in range(1, 1001):
    sqrt_str = str(math.sqrt(i))
    # Check if the string has at least 4 characters
    if len(sqrt_str) > 3 and sqrt_str[3] == '8':
        count += 1
print(count)

