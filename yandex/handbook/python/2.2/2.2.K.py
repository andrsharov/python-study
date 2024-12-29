num = input()
n3 = int(num[2])
n2 = int(num[1])
n1 = int(num[0])
n_min = min(n1, n2, n3)
n_max = max(n1, n2, n3)
if n_min == n1 and n_max == n2:
    n_mid = n3
elif n_min == n2 and n_max == n3:
    n_mid = n1
elif n_min == n3 and n_max == n1:
    n_mid = n2
elif n_min == n1 and n_max == n3:
    n_mid = n2
elif n_min == n2 and n_max == n1:
    n_mid = n3
elif n_min == n3 and n_max == n2:
    n_mid = n1

if n_min + n_max == 2 * n_mid:
    print("YES")
else:
    print("NO")