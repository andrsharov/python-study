def mean():
    summa = 0
    count = 0
    while True:
        x = yield
        if x is None:
            return summa / count
        summa += x
        count += 1


def get_value(gen):
    try:
        next(gen)
    except StopIteration as e:
        return e.value


m1 = mean()
next(m1)
m2 = mean()
next(m2)
for x in range(10):
    if x % 2 == 0:
        m1.send(x)
    else:
        m2.send(x)

print(get_value(m1))
print(get_value(m2))
