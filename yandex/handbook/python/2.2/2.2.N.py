n = input()
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

n_list = sorted([n1, n2, n3])

if n_list[0] != 0:
    r_min = str(n_list[0]) + str(n_list[1])
    r_max = str(n_list[2]) + str(n_list[1])
elif n_list[1] != 0:
    r_min = str(n_list[1]) + '0'
    r_max = str(n_list[2]) + str(n_list[1])
else:
    r_min = str(n_list[2]) + '0'
    r_max = str(n_list[2]) + '0'

print(r_min, r_max)