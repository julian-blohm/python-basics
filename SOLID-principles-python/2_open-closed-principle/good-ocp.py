
from math import pi
from abc import ABC, abstractmethod

# shape class inherits from abc package
class Shape(ABC):
    # create shape with type - no more keywordarguments
    def __init__(self, shape_type):
        self.shape_type = shape_type
        # no more logic to check what kind of shape type and defining keywordarguments

        

    # calculate area of shape is now abstract with decorator
    @abstractmethod
    def calculate_area(self):
        # if else statements no more needed here and will be done in concrete class
        pass

# Concrete classes inheriting from shape class
# rectangle has now the keywordarguments width and height        
class Rectangle(Shape):
    #constructor
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    # calculate method
    def calculate_area(self):
        return self.width * self.height
    
# similar to rectangle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
    
    def calculate_area(self):
        return pi * self.radius**2

# similar to rectangle
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# now using concrete classes
rectangle = Rectangle(width=10, height=5)
print(f"Rectangle Area = {rectangle.calculate_area()}")

circle = Circle(radius=5)
print(f"Circle Area = {circle.calculate_area()}")

square = Square(side=5)
print(f"Square area = {square.calculate_area()}")


# now, adding new shapes does not influence the whole shape class but derives from it
# internal implementation does not need to be modified
