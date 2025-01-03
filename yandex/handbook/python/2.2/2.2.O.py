n1 = input()
n2 = input()

c1 = int(n1[0])
c2 = int(n1[1])
c3 = int(n2[0])
c4 = int(n2[1])

n_list = sorted([c1, c2, c3, c4])

n_max = str(n_list[3])
n_min = str(n_list[0])
n_mid = str((n_list[1] + n_list[2]) % 10)

print(n_max, n_mid, n_min, sep='')