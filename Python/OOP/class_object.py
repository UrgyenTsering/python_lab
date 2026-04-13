
class Car:
    # Constructor method (__init__) is used to initialize the attributes of the class
    # It is automatically called when an object of the class is created
    def __init__(self, brand, model, color="blue"):
        # Assigning values to object attributes
        self.brand = brand      # Stores the brand of the car. self refers to the current object
        self.model = model      # Stores the model of the car
        self.color = color      # Stores the color (default is "blue" if not provided)


# Creating an object of the Car class
car_1 = Car("Toyota", "Corolla")

# Accessing and printing object attributes
print(car_1.brand)   # Output: Toyota
print(car_1.model)   # Output: Corolla
print(car_1.color)   # Output: blue (default value)

print("-----------------------------------")


# Create a class named People
# it should have two attribute name and birth year
# create two objects using this class
# Display their name and age using f-string

class People:
    # Constructor to initialize attributes of the People class
    def __init__(self, name, birth_year):
        self.name = name              # Stores the person's name
        self.birth_year = birth_year  # Stores the person's birth year


# This is a FUNCTION, not a method
# Reason: It is defined outside the class and does not use 'self'
def get_age(birth_year):
    # Calculate age using the current year (2026)
    age = 2026 - birth_year
    return age


# Creating objects (instances) of the People class
p1 = People("Rabindra", 1990)
p2 = People("Ram", 1995)


# Calling the external function by passing object attributes
print(f"{p1.name}:{get_age(p1.birth_year)}")  # Output: Rabindra:36
print(f"{p2.name}:{get_age(p2.birth_year)}")  # Output: Ram:31

print("-----------------------------------")




class People:
    # Constructor to initialize the attributes of the class
    def __init__(self, name, birth_year):
        self.name = name              # Stores the person's name
        self.birth_year = birth_year  # Stores the person's birth year

    # This is a METHOD (not a function) because it is defined inside the class
    # It CAN be used outside the class, but only through an object (e.g., p1.age)
    
    # @property decorator allows this method to be accessed like an attribute
    # So we use p1.age instead of p1.age()
    @property
    def age(self):
        # Calculate age based on the current year
        result = 2026 - self.birth_year
        return result

    # __repr__ method provides a string representation of the object
    # It is automatically called when the object is printed
    def __repr__(self):
        return f"{self.name} is of age {self.age}"

    # Method to check if the person is an adult
    def is_adult(self):
        user_age = self.age  # Accessing age property
        if user_age > 18:
            return True      # Returns True if age is greater than 18
        else:
            return False     # Returns False otherwise


# Creating objects (instances) of the People class
p1 = People("Rabindra", 1990)
p2 = People("Ram", 2010)


# Printing objects (calls __repr__ method automatically)
print(p1)  # Output: Rabindra is of age 36
print(p2)  # Output: Ram is of age 16


# Calling method to check adulthood
print(p1.is_adult())  # Output: True
print(p2.is_adult())  # Output: False

