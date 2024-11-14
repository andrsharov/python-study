class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.first = 0
        self.second = 1

    def __iter__(self):
        # Можно реализовать и получение итератора, и сам итератор в одном классе,
        # но можно было бы сделать и два отдельных класса
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        if self.first > self.limit:
            raise StopIteration
        return self.first


for x in Fibonacci(100):
    print(x, end=' ')
