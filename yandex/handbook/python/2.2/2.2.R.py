a = int(input())
b = int(input())
c = int(input())

s_sorted = sorted([a, b, c])

s_min = s_sorted[0]
s_mid = s_sorted[1]
s_max = s_sorted[2]

if s_max ** 2 == s_min ** 2 + s_mid ** 2:
    print("100%")
elif s_max ** 2 > s_min ** 2 + s_mid ** 2:
    print("велика")
else:
    print("крайне мала")