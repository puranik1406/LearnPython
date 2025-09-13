class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    def __str__(self):
        return f"({self.i}, {self.j}, {self.k})"
    def __mul__(self, scalar):
        return Vector(self.i * scalar, self.j * scalar, self.k * scalar)
    def __rmul__(self, vector):
        return self.__mul__(vector)
    
v1 = Vector(3, 4, 5)
v2= Vector(6,8,10)

v3 = v1 + v2
print(v3)  # Output: Vector(9, 12, 15) 
v4 = v1 * 2
print(v4)  # Output: Vector(6, 8, 10)
v5 = v2 * v1
print(v5)  # Output: Vector(9, 12, 15)