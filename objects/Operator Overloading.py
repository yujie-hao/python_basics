# link: https://www.programiz.com/python-programming/operator-overloading


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # compare the magnitude of the point
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = Point(1, 2)
p2 = Point(2, 3)
# print(p1 + p2) # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

print(p1)
print(str(p1))
print(format(p2))

print(p1 + p2)
print(p1 < p2)
