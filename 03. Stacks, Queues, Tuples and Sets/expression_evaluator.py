from math import floor
from functools import reduce


expression = input().split()

nums = []

for el in expression:
    if el == "*":
        result = reduce(lambda a, b: a*b, nums)
        nums.clear()
        nums.append(result)

    elif el == "+":
        result = reduce(lambda a, b: a+b, nums)
        nums.clear()
        nums.append(result)

    elif el == "-":
        result = reduce(lambda a, b: a-b, nums)
        nums.clear()
        nums.append(result)

    elif el == "/":
        result = reduce(lambda a, b: a/b, nums)
        nums.clear()
        nums.append(floor(result))

    else:
        nums.append(int(el))

print(*nums)
