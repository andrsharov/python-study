num1_str = input()
num2_str = input()

num1_zero = f"{num1_str:0>3}"
num2_zero = f"{num2_str:0>3}"

result = str()
for i in range(0, 3, 1):
    result += str(int(num1_zero[i]) + int(num2_zero[i]))[-1:]

print(result)