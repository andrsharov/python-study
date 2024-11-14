from time import perf_counter

class timeit:
    def __init__(self, process_name):
        self.name = process_name

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f'{self.name}: {perf_counter() - self.start:0.3f} sec')

with timeit('Возведение в квадрат миллиона чисел'):
    # вызван метод __enter__
    for i in range(1000000):
        i = i ** 2
    # вызван метод __exit__
