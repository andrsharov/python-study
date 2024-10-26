start_sum = float(input())
final_sum = float(input())
percent_sum = float(input())

subtotal = start_sum
i = int(0)

while subtotal < final_sum:
    subtotal = subtotal + subtotal * ( percent_sum / 100)
    i = i + 1

print(i)