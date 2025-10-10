# Base Class
class Shape:
    def calculate_area(self):
        print("Area calculation not implemented for generic shape.")

# A child class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Area of Rectangle is: {area}")


# Creating an instance of Rectangle and calling the method
rect = Rectangle(10, 8)
rect.calculate_area()



        
