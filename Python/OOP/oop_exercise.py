# EXERCISE 1: CREATING CLASSES

# Create a class Car with following details:
# Attributes: brand, model, color. Default value of color should be blue.
# Methods: display_info, start_engine, stop_engine.
# 	display_info should return Brand: {brand}, Model: {model}, Color: {color}.
# 	start_engine should return "Engine of {self.brand} {self.model} started".
# 	stop_engine should return "Engine of {self.brand} {self.model} stopped".
# Create two objects of Car class
# 	car_1 with brand Toyota, model Corolla and color Red.
# 	car_2 with brand Honda, model Civic.
# Call display_info, start_engine and stop_engine for both objects and display the output.


class Car:
    def __init__(self, brand, model, color="blue"):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}"

    def start_engine(self):
        return f"Engine of {self.brand} {self.model} started"

    def stop_engine(self):
        return f"Engine of {self.brand} {self.model} stopped"


# Creating two objects
car_1 = Car("Toyota", "Corolla", "Red")
car_2 = Car("Honda", "Civic")

print(car_1.display_info())
print(car_1.start_engine())
print(car_1.stop_engine())


# EXERCISE 2: INHERITANCE

# Create a class Employee that has:
# 	attributes: name, dob, age, salary, skill_sets.
# Create class Developer inheriting Employee that has:
# 	Additional  attribute: github_link, is_fullstack.
# 	method: display_profile that returns {name} has skills: s1, s2. Git: {github_link}.
# Create class HR inheriting Employee that has:
# 	Additional  attribute: is_manager, onboard_rate.
# 	method: display_profile that displays {name} has skills: s1, s2. Onboard rate: {rate}.
# 5 developers and 2 HR joined the company. Create objects for them with random attribute.
# Create list developers_list with all developer objects and list hr_list with all HR objects.
# Loop through developers_list to display developer's name with both Python and Git skill.


class Employee:
    def __init__(self, name, dob, age, salary, skill_sets):
        self.name = name
        self.dob = dob
        self.age = age
        self.salary = salary
        self.skill_sets = skill_sets


class Developer(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, github_link, is_fullstack):
        super().__init__(name, dob, age, salary, skill_sets)
        self.github_link = github_link
        self.is_fullstack = is_fullstack

    def display_profile(self):
        skill_str = ", ".join(self.skill_sets)
        return f"{self.name} has skills:{skill_str}. And his Github link: {self.github_link}"


class HR(Employee):
    def __init__(self, name, dob, age, salary, skill_sets, is_manager, onboard_rate):
        super().__init__(name, dob, age, salary, skill_sets)
        self.is_manager = is_manager
        self.onboard_rate = onboard_rate

    def display_profile(self):
        skill_str = ", ".join(self.skill_sets)
        return f"{self.name} has skills: {skill_str}. And his onboard rate:{self.onboard_rate}"


dev1 = Developer(
    "Ram",
    "2000-01-01",
    26,
    50000,
    ["Python", "React", "Django"],
    "https://github.com/ram",
    True,
)
dev2 = Developer(
    "Sita",
    "1998-05-10",
    28,
    60000,
    ["JavaScript", "Node.js", "Express"],
    "https://github.com/sita",
    False,
)
dev3 = Developer(
    "Hari",
    "1995-09-15",
    31,
    70000,
    ["Python", "Spring Boot", "Git"],
    "https://github.com/hari",
    True,
)
dev4 = Developer(
    "Maya",
    "1999-03-20",
    27,
    55000,
    ["Python", "Flask", "Vue.js"],
    "https://github.com/maya",
    False,
)
dev5 = Developer(
    "Anil",
    "1997-12-05",
    29,
    65000,
    ["C#", ".NET", "Angular"],
    "https://github.com/anil",
    True,
)


hr1 = HR("Kiran", "1992-06-10", 31, 45000, ["Recruitment", "Training"], True, 85)
hr2 = HR("Suman", "1995-11-20", 28, 40000, ["Payroll", "Employee Relations"], False, 70)

developer_list = [dev1, dev2, dev3, dev4, dev5]
hr_list = [hr1, hr2]

found = False
for developer in developer_list:
    if "Python" in developer.skill_sets and "Git" in developer.skill_sets:
        print(f"{developer.name} is the developer with both Python and Git skills.")
        found = True

if not found:
    print(" No developers has both Python and Git skills")

print(hr1.display_profile())


# Exercise 3: Method Overriding

# Create a class called Point that has:
# 	attributes: x_coordinate, y_coordinate.
# 	method: dist_from_origin calculated with formula: sqrt(x^2 + y^2).
# 	Operator: +, - that should add/subtract two point with logic (x1+x2, y1+y2).
# 	method: print should return P(x, y).
# 	Override: <, >, <=, >=, == and != that should use dist_from_origin to compare.
# Create two points p_1 with coordinates (3, 4) and p_2 with coordinates (1, 2).
# Use print(p_1), print(p_2) to display the points. Should give P(3, 4) and P(1, 2).
# Create a new point p_3 by adding p_1 and p_2. i.e p_3 = p_1 + p_2. Display p_3.
# Calculate distance of p_1 and p_2 from origin using dist_from_origin method.
# Compare p_1 and p_2 using overridden operators. i.e. p_1 > p_2, p_1 <= p_2 etc.

import math

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Method: distance from origin
    def dist_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Operator: +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Operator: -
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Print format: P(x, y)
    def __str__(self):
        return f"P({self.x}, {self.y})"

    # Comparison operators (based on distance)
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    def __ge__(self, other):
        return self.dist_from_origin() >= other.dist_from_origin()

    def __eq__(self, other):
        return self.dist_from_origin() == other.dist_from_origin()

    def __ne__(self, other):
        return self.dist_from_origin() != other.dist_from_origin()


# Create points
p_1 = Point(3, 4)
p_2 = Point(1, 2)

# Print points
print(p_1)
print(p_2)

# Add points
p_3 = p_1 + p_2
print("p_3 =", p_3)

# Distance from origin
print("Distance of p_1:", p_1.dist_from_origin())
print("Distance of p_2:", p_2.dist_from_origin())

# Comparisons
print("p_1 > p_2:", p_1 > p_2)
print("p_1 < p_2:", p_1 < p_2)
print("p_1 >= p_2:", p_1 >= p_2)
print("p_1 <= p_2:", p_1 <= p_2)
print("p_1 == p_2:", p_1 == p_2)
print("p_1 != p_2:", p_1 != p_2)

"""
OUTPUT: 
    P(3, 4)
    P(1, 2)
    p_3 = P(4, 6)
    Distance of p_1: 5.0
    Distance of p_2: 2.236...
    p_1 > p_2: True
    p_1 < p_2: False
    p_1 >= p_2: True
    p_1 <= p_2: False
    p_1 == p_2: False
    p_1 != p_2: True
"""


# Exercise 4: Encapsulation
# Create a class BankAccount that has:
# 	attributes: owner, __balance (private attribute with default value 0).
# 	methods: deposit, withdraw, get_balance, transfer.
# 		deposit to add amount to balance if it's is +ve.
# 		withdraw to subtract amount from balance if it's +ve and less than balance.
# 		get_balance to display current balance.
# 		transfer to transfer amount from one account to another.
# Create two bank accounts account_1 with owner Rabindra and account_2 with owner John.
# 	Deposit 1000 to account_1 and 500 to account_2.
# 	Withdraw 200 from account_1 and 100 from account_2.
# 	Transfer 200 from account_1 to account_2.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    # Get balance
    def get_balance(self):
        return self.__balance

    # Transfer money
    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount
        else:
            print("Transfer failed")

    # For printing
    def __str__(self):
        return f"{self.owner} has balance Rs {self.__balance}"


# 🔹 Create accounts
account_1 = BankAccount("Rabindra")
account_2 = BankAccount("John")

# 🔹 Deposit
account_1.deposit(1000)
account_2.deposit(500)

# 🔹 Withdraw
account_1.withdraw(200)
account_2.withdraw(100)

# 🔹 Transfer
account_1.transfer(200, account_2)

# 🔹 Display final balances
print(account_1)
print(account_2)

"""
Output:

After deposit: 
account_1 = 1000
account_2 = 500

After withdraw:
account_1 = 800
account_2 = 400


After transfer (200 from account_1 → account_2):
account_1 = 600
account_2 = 600

"""