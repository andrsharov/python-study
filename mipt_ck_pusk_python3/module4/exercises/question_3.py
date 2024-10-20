f_name = input()
f_obj = open(f_name, "r")
f_list = f_obj.read().split()
f_obj.close()
f_count = dict()
for i in f_list:
    if i in f_count:
        f_count[i] += 1
    else:
        f_count[i] = 1

words_sorted = sorted(f_count.items(), key=lambda x: x[0], reverse=False)

num_sorted = sorted(words_sorted, key=lambda num: num[1], reverse=True)

for k in range(len(num_sorted)):
    print(num_sorted[k][1], num_sorted[k][0])