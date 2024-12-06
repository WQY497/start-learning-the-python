import math

count = 0
for i in range(1, 1001):
    sqrt_str = str(math.sqrt(i))
    # Check if the string has at least 4 characters
    if len(sqrt_str) > 3 and sqrt_str[3] == '8':
        count += 1

print(count)
