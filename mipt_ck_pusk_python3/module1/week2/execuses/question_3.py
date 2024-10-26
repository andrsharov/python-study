n = int(input())

sum_square = 1
for i in range(2, n+1, 1):
    sum_square = sum_square + i ** 2

print(sum_square)