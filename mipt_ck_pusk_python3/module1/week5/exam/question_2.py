class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2) ** 0.5

class Segment3D:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance_to(self.p2)

    def middle(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        z = (self.p1.z + self.p2.z) / 2
        return Point3D(x, y, z)

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
p1 = Point3D(1, 2, 3)
p2 = Point3D(2.5, 1, -2)
s = Segment3D(p1, p2)
print(s.length())
m = s.middle()
print(type(m) == Point3D)
print(m.x)
print(m.y)
print(m.z)