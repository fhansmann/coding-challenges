class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, null):
        Shape.__init__(self) #also: super().__init__()
        self.length = null

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
