class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2) ** 0.5

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
p1 = Point3D(1, 2, 3)
p2 = Point3D(2.5, 1, -2)
print(p1.distance_to(p2))