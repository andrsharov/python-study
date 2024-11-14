class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c

f = Quadratic(1, 2, -1)
