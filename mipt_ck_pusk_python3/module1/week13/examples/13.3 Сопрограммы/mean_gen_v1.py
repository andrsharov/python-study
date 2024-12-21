def mean():
    summa = 0
    count = 0
    while True:
        mean = summa / count if count else None
        x = yield mean
        summa += x
        count += 1


m1 = mean()
next(m1)
m2 = mean()
next(m2)
for x in range(10):
    if x % 2 == 0:
        mean_even = m1.send(x)
    else:
        mean_odd = m2.send(x)

print(mean_even)
print(mean_odd)
