#object_name = ClassName(arguments_if_any)

class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x  
        self.corner_y = corner_y 

    def find_center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

rect1 = Rectangle(10, 20, 0, 0)

center = rect1.find_center()
print(f"Center of the rectangle: ({center[0]}, {center[1]})")
print(f"Area of the rectangle: {rect1.area()}")
print(f"Perimeter of the rectangle: {rect1.perimeter()}")
