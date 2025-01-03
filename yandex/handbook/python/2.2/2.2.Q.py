a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0 and b != 0:
    print(f"{-c / b:.2f}")
elif d < 0:
    print("No solution")
elif d == 0:
    x = -b / 2 * a
    print(f"{x:.2f}")
else:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    print(f"{min_x:.2f} {max_x:.2f}")