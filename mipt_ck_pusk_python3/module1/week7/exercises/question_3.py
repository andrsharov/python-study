class Minus:
    def __init__(self, value) -> None:
        self.value = value

    @property
    def zero(self):
        return Number(self.value - 0)

    @property
    def one(self):
        return Number(self.value - 1)

    @property
    def two(self):
        return Number(self.value - 2)

    @property
    def three(self):
        return Number(self.value - 3)

    @property
    def four(self):
        return Number(self.value - 4)

    @property
    def five(self):
        return Number(self.value - 5)

    @property
    def six(self):
        return Number(self.value - 6)

    @property
    def seven(self):
        return Number(self.value - 7)

    @property
    def eight(self):
        return Number(self.value - 8)

    @property
    def nine(self):
        return Number(self.value - 9)

class Plus:
    def __init__(self, value) -> None:
        self.value = value

    @property
    def zero(self):
        return Number(self.value + 0)

    @property
    def one(self):
        return Number(self.value + 1)

    @property
    def two(self):
        return Number(self.value + 2)

    @property
    def three(self):
        return Number(self.value + 3)

    @property
    def four(self):
        return Number(self.value + 4)

    @property
    def five(self):
        return Number(self.value + 5)

    @property
    def six(self):
        return Number(self.value + 6)

    @property
    def seven(self):
        return Number(self.value + 7)

    @property
    def eight(self):
        return Number(self.value + 8)

    @property
    def nine(self):
        return Number(self.value + 9)

class Times:
    def __init__(self, value) -> None:
        self.value = value

    @property
    def zero(self):
        return Number(self.value * 0)

    @property
    def one(self):
        return Number(self.value * 1)

    @property
    def two(self):
        return Number(self.value * 2)

    @property
    def three(self):
        return Number(self.value * 3)

    @property
    def four(self):
        return Number(self.value * 4)

    @property
    def five(self):
        return Number(self.value * 5)

    @property
    def six(self):
        return Number(self.value * 6)

    @property
    def seven(self):
        return Number(self.value * 7)

    @property
    def eight(self):
        return Number(self.value * 8)

    @property
    def nine(self):
        return Number(self.value * 9)

class Number:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)

    @property
    def minus(self):
        return Minus(self.value)

    @property
    def plus(self):
        return Plus(self.value)

    @property
    def times(self):
        return Times(self.value)

zero = Number(0)
one = Number(1)
two = Number(2)
three = Number(3)
four = Number(4)
five = Number(5)
six = Number(6)
seven = Number(7)
eight = Number(8)
nine = Number(9)

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
print(five)
print(five.plus.two)
print(five.plus.two.times.four)
print(nine.minus.three)
print(nine.times.nine.times.nine)
print(seven)
print(eight.minus.four)
print(one.plus.six)
print(two.times.three)