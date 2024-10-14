num = input()
num_int = int(num)
num_str = str(num_int)
num_digits = [int(num_str[i]) for i in range(len(num_str))]

num_zeros = []

for j in range(len(num_str)):
    if num_digits[j] == 0:
        num_zeros.append(num_digits[j])

while 0 in num_digits: num_digits.remove(0)

num_digits.sort()
num_result = []
num_result.append(num_digits.pop(0))
num_result.extend(num_zeros)
num_result.extend(num_digits)
num_result_str = ''
for i in range(len(num_result)):
    num_result_str += str(num_result[i])
num_result = int(num_result_str)
print(num_result_str)
