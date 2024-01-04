N = -1
while not 1 <= N <= 100:
    A = -1
    B = -1
    while not 1 <= B < A <= 100:
        print('Enter 3 integer numbers N, A, B:  1≤B<A≤100 and 1≤N≤100, separates by space, exp.:  "10 3 2"')
        str_NAB = str(input())
        list_NAB = str_NAB.split()
        count_NAB = len(list_NAB)
        if count_NAB == 3:
            N = int(list_NAB[0])
            A = int(list_NAB[1])
            B = int(list_NAB[2])
        else:
            continue
line = 0
i = 1
while True:
    line += A
    if line >= N:
        break
    line -= B
    if line >= N:
        break
    i += 1

print(i)

#days = int(N/(A - B))
#print(days)
