import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x)
        print(self.y)
    def move(self, tox, toy):
        self.x = tox
        self.y = toy
    def dist(self, secondPoint):
        d = (self.x-secondPoint.x) ** 2 + (self.y-secondPoint.y) ** 2  
        print(math.sqrt(d))

x = Point(1, 1)
y = Point(2, 2)
x.show()

x.dist(y)

x.move(2, 2)

x.dist(y)
