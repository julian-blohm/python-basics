
from math import pi


class Shape:
    # create shape with type and list of arguments
    def __init__(self, shape_type, **keywordargs):
        self.shape_type = shape_type
        # depending on shape, other arguments are needed
        if self.shape_type == "rectangle":
            self.width = keywordargs["width"]
            self.height = keywordargs["height"]
        elif self.shape_type == "circle":
            self.radius = keywordargs["radius"]
        elif self.shape_type == "square":
            self.side = keywordargs["side"]
        

    # calculate area of shape
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
        elif self.shape_type == "square":
            return self.side ** 2
        
rectangle = Shape("rectangle", width=10, height=5)
print(f"Rectangle Area = {rectangle.calculate_area()}")

circle = Shape("circle", radius=5)
print(f"Circle Area = {circle.calculate_area()}")

square = Shape("square", side=5)
print(f"Square area = {square.calculate_area()}")


# bad ocp because if we want to have another shape, we would need another elif with arguments
# we would need it in both method, init and calculate shape method see line 15-16, 25-26, 34-35
# so the class shape is open for modification 
# one solution would be to create a base class for shape and concrete classes for implementation then
