l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("YES")
else:
    print("NO")