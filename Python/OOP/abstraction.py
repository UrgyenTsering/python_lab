from abc import ABC, abstractmethod


# Abstract Base Class (cannot be instantiated directly)
class Shape(ABC):

    # Abstract method (must be implemented by child classes)
    @abstractmethod
    def perimeter(self):
        pass


# Rectangle class inherits from Shape
class Rectangle(Shape):

    # Constructor to initialize rectangle dimensions
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Method to calculate area of rectangle
    def area(self):
        return self.length * self.breadth

    # Implementation of abstract method from Shape
    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Creating object of Rectangle class
r1 = Rectangle(10, 5)

# Calling methods
print(r1.area())  # Output: 50
print(r1.perimeter())  # Correct way to call method
