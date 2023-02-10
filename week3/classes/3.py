class Square:
    def __init__(self, length = 0):
        self.length = length


class Shape(Square):
    def area(self):
        print(self.length * self.length)
        

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        
class Shape2(Rectangle):
    def area(self):
        print(self.l * self.w)
    
x = Shape(7)
x.area()
y = Shape2(5, 7)
y.area()