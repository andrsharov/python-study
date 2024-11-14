class Lucas:

    def __init__(self, u0, u1, p, q, n):
        self.u0: int = u0
        self.u1: int = u1
        self.p: int = p
        self.q: int = q
        self.n: int = n
        self.counter: int  = 0
        self.result:list = [u0, u1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.u0
        elif self.counter == 1:
            self.counter += 1
            return self.u1
        elif self.counter < self.n:
            self.result.append(self.p * self.result[self.counter - 1] - self.q * self.result[self.counter - 2])
            self.counter += 1
            return self.result[self.counter - 1]
        else:
            raise StopIteration

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
print(list(Lucas(0, 1, 1, -1, 10)))
print(list(Lucas(0, 1, 1, 1, 10)))
print(list(Lucas(2, 1, 1, -1, 10)))