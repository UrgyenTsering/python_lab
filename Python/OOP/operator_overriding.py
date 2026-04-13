
# OPERATOR OVERRIDING = giving special meaning to operators (+, -, <, etc.) for your own class objects
# Normally: (+) use for adding numbers which is already defined by python
# 3 + 5 = 8

# But for objects, python didn't have decided + operator to add two objects and point. 
# So, with operator overriding, we can add two different objects:
# p1 + p2   # for objects


# 🔹 Why do we need it?
# 👉 So objects can behave like numbers
# Example:
  # Add two points
  # Compare two objects
  # Subtract custom objects
  
""" 
🔥 Difference from normal operators
Case	      Behavior
Normal	    Python decides behavior
Overridden	YOU decide behavior
"""
  

# BASIC EXAMPLE:
class Point:
    def __init__(self, x, y):
        # Constructor: initializes object with x and y coordinates
        self.x = x
        self.y = y

    # 🔹 Operator Overriding for + 
    def __add__(self, other):
        """
        This method is called when we use: p1 + p2

        self  → first object (p1)
        other → second object (p2)

        It returns a NEW Point object with:
        (x1 + x2, y1 + y2)
        """
        return Point(self.x + other.x, self.y + other.y)

    # 🔹 String representation of object
    def __str__(self):
        """
        This method is called when we use: print(object)

        It defines how the object should be displayed
        """
        return f"({self.x}, {self.y})"


# 🔹 Create two Point objects
p1 = Point(3, 4)   # Point with x=3, y=4
p2 = Point(1, 2)   # Point with x=1, y=2


# 🔹 Add two objects using + operator
# Internally: p1 + p2 → p1.__add__(p2)
p3 = p1 + p2


# 🔹 Print result
# Internally: print(p3) → p3.__str__()
print(p3)




# Implementation of 3D Vector with Addition, Subtraction, and Comparison
class Vector3D:
    def __init__(self, x, y, z):
        # Store x, y, z coordinates
        self.x = x
        self.y = y
        self.z = z

    # 🔹 How object is printed
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # 🔹 + operator (vector addition)
    def __add__(self, other):
        # Add corresponding values
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # 🔹 - operator (vector subtraction)
    def __sub__(self, other):
        return Vector3D(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # 🔹 < operator (compare based on magnitude)
    def __lt__(self, other):
        # magnitude = √(x² + y² + z²)
        mag1 = (self.x**2 + self.y**2 + self.z**2) ** 0.5
        mag2 = (other.x**2 + other.y**2 + other.z**2) ** 0.5
        return mag1 < mag2


# 🔹 Create objects
vec_1 = Vector3D(5, -1, 3)
vec_2 = Vector3D(4, 5, 6)

# 🔹 Print vectors
print(vec_1)   # calls __str__
print(vec_2)

# 🔹 Operator overloading in action
print(vec_1 + vec_2)  # calls __add__
print(vec_1 < vec_2)  # calls __lt__
print(vec_1 - vec_2)  # calls __sub__