n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

n1 = (k2 - m) * n / (k2 - k1)
n2 = n - n1

print(int(n1), int(n2))