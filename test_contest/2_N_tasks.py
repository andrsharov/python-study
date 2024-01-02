N = -1
while not 0 <= N <= 100:
    print('Enter integer number N (0≤N≤100)')
    N = int(input())
if 10 <= N <= 20:
    print(N, " zadach")
elif N % 10 == 1:
    print(N, " zadacha")
elif N % 10 == 2:
    print(N, " zadachi")
elif N % 10 == 3:
    print(N, " zadachi")
elif N % 10 == 4:
    print(N, " zadachi")
else:
    print(N, " zadach")