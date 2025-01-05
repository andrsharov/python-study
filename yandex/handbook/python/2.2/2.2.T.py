str1 = input()
str2 = input()
str3 = input()

if "зайка" in str1:
    str_1_len = len(str1)
else:
    str_1_len = 0

if "зайка" in str2:
    str_2_len = len(str2)
else:
    str_2_len = 0

if "зайка" in str3:
    str_3_len = len(str3)
else:
    str_3_len = 0

str_list = []

if str_1_len != 0:
    str_list.append(str1)
if str_2_len != 0:
    str_list.append(str2)
if str_3_len != 0:
    str_list.append(str3)

str_min = min(str_list)

if str_min == str1:
    print(str1, len(str1))
elif str_min == str2:
    print(str2, len(str2))
elif str_min == str3:
    print(str3, len(str3))