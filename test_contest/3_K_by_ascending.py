K = -1
N = -2
while not 1 <= K <= N <= 100:
    count_NK = -1
    while count_NK != 2:
        print('Enter integer number N (0≤N≤100) and K (1≤K≤N) separate by space, exp.:  "5 4"')
        str_NK = str(input())
        list_NK = str_NK.split()
        count_NK = len(list_NK)
        if count_NK == 2:
            N = int(list_NK[0])
            K = int(list_NK[1])
count_NUM = -1
while not count_NUM == N:
    print('Enter ', N, ' integer numbers separated by spaces, exp.:  "1 2 3 4 5"')
    str_NUM = str(input())
    list_NUM = str_NUM.split()
    count_NUM = len(list_NUM)

print(list_NUM[K-1])
