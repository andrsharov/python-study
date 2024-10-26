n = int(input())
lst =[list(map(int, input().split())) for _ in range(n)]
print(*map(lambda x: x[0], sorted(lst, key=lambda x: x[1], reverse=True)), sep='\n')