class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return f'Vector({-self.x}, {-self.y})'

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __abs__(self):
        if isinstance(self, Vector):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        else:
            return NotImplemented

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно

v = Vector(1, 2)
print(-v)
print(v - Vector(0, 1))
print(v / 2 )
print(abs(v))
#print(v - 'abc')  #TypeError: unsupported operand type(s) for -: 'Vector' and 'str'
#print(v / 'abc') #TypeError: unsupported operand type(s) for /: 'Vector' and 'str'
#print(v / v)  #TypeError: unsupported operand type(s) for /: 'Vector' and 'Vector'