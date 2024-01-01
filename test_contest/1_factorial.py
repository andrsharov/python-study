N = -1
while not 0 <= N <= 100:
    print('Enter integer number N (0≤N≤100)')
    N = int(input())
fact = 1
for i in range(1, N+1):
    fact = fact * i

print("Factorial of ", N, " is :", fact)
