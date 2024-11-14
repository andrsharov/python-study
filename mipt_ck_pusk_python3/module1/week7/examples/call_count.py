from functools import cache


class call_count:
    def __init__(self, function):
        self.function = function
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.function(*args, **kwargs)


@call_count
@cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(30)
print(fibonacci.count)
