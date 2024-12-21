def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


for x in fib():
    if x > 1_000_000:
        break
    print(x)
