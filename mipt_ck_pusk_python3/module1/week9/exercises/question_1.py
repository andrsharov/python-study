import math

nums = input()
nums_list = nums.split()
nums_integer = list(map(int, nums_list))

print(math.gcd(*nums_integer))