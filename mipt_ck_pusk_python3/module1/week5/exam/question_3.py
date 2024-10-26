class Point3D:
    def __init__(self, x: int, y: int, z: int):
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

    def cos_to(self, other_object):
        # Найдем вектор по координатам точек:
        vector_ab = (self.p2.x - self.p1.x, self.p2.y - self.p1.y, self.p2.z - self.p1.z)
        vector_cd = (other_object.p2.x - other_object.p1.x, other_object.p2.y - other_object.p1.y, other_object.p2.z - other_object.p1.z)
        # Найдем скалярное произведение векторов:
        scalar_multiplication = vector_ab[0] * vector_cd[0] + vector_ab[1] * vector_cd[1] + vector_ab[2] * vector_cd[2]
        # Найдем длину (модуль) вектора:
        module_ab = (vector_ab[0] ** 2 + vector_ab[1] ** 2 + vector_ab[2] ** 2) ** 0.5
        module_cd = (vector_cd[0] ** 2 + vector_cd[1] ** 2 + vector_cd[2] ** 2) ** 0.5
        # Найдем угол между векторами:
        cos_a = scalar_multiplication / (module_ab * module_cd)
        return abs(cos_a)

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
s1 = Segment3D(Point3D(0, 0, 0), Point3D(1, 2, 3))
s2 = Segment3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
print(s1.cos_to(s2))