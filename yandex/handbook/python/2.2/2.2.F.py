y = int(input())
if y % 400 == 0:
    n = "YES"
elif y % 100 == 0:
    n = "NO"
elif y % 4 == 0:
    n = "YES"
else:
    n = "NO"
print(n)