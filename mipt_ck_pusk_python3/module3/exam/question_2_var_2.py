q = int(input())
d = dict()

for i in range(q):
     points_list = input().split()
     d[points_list[1]] = points_list[0]

keys = list(d.keys())
keys.sort(reverse=True)

for i in keys:
    print(d[i])