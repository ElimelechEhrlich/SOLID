from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shapetype):
        self.shapetype = shapetype

    @abstractmethod
    def area(self):
        pass    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def area(self):
        return f'{self.shapetype} area of radius {self.radius} is: {self.radius * 3.14  * 2}'
    

class Square(Shape):
    def __init__(self, sidelength):
        super().__init__('Square')
        self.sidelength = sidelength

    def area(self):
        return f'{self.shapetype} area of sides length - {self.sidelength} is: {self.sidelength ** 2}'

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Rectangle')
        self.width = width
        self.height = height

    def area(self):
        return f'{self.shapetype} area of width {self.width} and height {self.height} is: {self.width * self.height}'

b = Circle(5)
c = Square(5)
a = Rectangle(10, 5)

s : Shape = [a,b,c]
for i in s:
    print (i.area())