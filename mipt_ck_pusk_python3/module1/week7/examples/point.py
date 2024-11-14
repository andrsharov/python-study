class Point:
    """
    Точка на плоскости с координатами x и y
    """
    x: float
    y: float

    __frozen = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__frozen = True

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    # def __setattr__(self, attr, value):
    #     if not self.__frozen:
    #         super().__setattr__(attr, value)
    #     else:
    #         raise TypeError('Point object is immutable')



p = Point(1, 1)
points = {p: 10}
p.x += 1
print(points[p])
