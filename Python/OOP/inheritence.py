class People:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        result = 2026 - self.birth_year
        return result

    def __repr__(self):
        return f"{self.name} is of age {self.age}"

    def is_adult(self):
        user_age = self.age
        if user_age > 18:
            return True
        else:
            return False


p1 = People("Rabindra", 1990)
p2 = People("Ram", 2010)

print(p1)
print(p2)

print(p1.is_adult())
print(p2.is_adult())


# Single Inheritance: Student class inherits from People class
class Student(People):

    # Constructor of Student class with additional attributes
    def __init__(
        self, name, birth_year, course_enrolled, mobile_number, fee_paid, email
    ):
        # Call the constructor of the parent class (People)
        # This initializes inherited attributes: name and birth_year
        super().__init__(name, birth_year)

        # Initializing additional attributes specific to Student
        self.course_enrolled = course_enrolled  # Course the student is enrolled in
        self.mobile_number = mobile_number  # Student's contact number
        self.fee_paid = fee_paid  # Fee payment status (True/False)
        self.email = email


# Creating an instance (object) of Student class
s1 = Student("Ram", 1999, "Python", 987654, True, "tester@gmail.com")

# Accessing inherited attributes and methods
print(s1.name)  # Inherited attribute from People class
print(s1.age)  # Inherited property (method with @property)
print(s1.is_adult())  # Inherited method from People class


class Player(People):
    def __init__(self, name, birth_year, club, country):
        super().__init__(name, birth_year)
        self.club = club
        self.country = country

    def shoot(self):
        return f"{self.name} is shooting."


pl1 = Player("Messi", 1996, "Barcelona", "Argentina")
pl2 = Player("Ronaldo", 2010, "Realmadrid", "Portugal")

print(pl1)
print(pl2)

print(pl1.shoot())
print(pl2.shoot())
