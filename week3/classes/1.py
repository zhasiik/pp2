class ex:
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = str(input())
    def prints(self):
        print(self.str.upper())
x = ex()
x.getString()
x.prints()  