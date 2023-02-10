class Shape:
    def __init__(self, length = 0):
        self.length = length
        
class Square(Shape):
    def area(self):
        print(self.length * self.length)
    
x = Square(5)
x.area()
y = Square()
y.area()