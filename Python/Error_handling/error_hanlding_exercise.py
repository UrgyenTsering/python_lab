# EXERCISE 1: ERROR HANDLING


# Write a function that takes a string and returns number of lowercase characters in it. Ensure TypeError is handled.
def name_handler():
    try:
        name = input("Enter Your Name: ")

        count = 0
        for ch in name:
            if ch.islower():
                count += 1

        return count

    except TypeError:
        return "Input must be a string!"


# Function call
result = name_handler()
print("Number of lowercase characters:", result)

print("Program run successfully")


# Write a function that takes mass in kg and volume in cubic meter and returns density. Ensure ZeroDivisionError and TypeError is handled.
def find_density(mass, volume):
    try:
        destiny = mass / volume
        return f" The density of mass {mass} kg and volume {volume} m^3 is {destiny} kg/m^3 "

    except ZeroDivisionError:
        return "The value of volume should not be Zero!"

    except TypeError:
        return "Error: Please enter numeric values (int or float)."


# Example usage
print(find_density(10, 2))  # सही case → 5.0
print(find_density(10, 0))  # ZeroDivisionError
print(find_density("10", 2))  # TypeError


# Write a function get_name that accepts a dictionary and returns the value of key name. Ensure KeyError is handled.

student_info = {"name": "John", "age": 20}


def get_name(student_info):
    try:
        return student_info["name"]
    except KeyError:
        return "Key 'name' not found in the dictionary."


# Testing
print(get_name(student_info))  # Output: John
print(
    get_name({"age": 20, "city": "NY"})
)  # Output: Key 'name' not found in the dictionary.


# Write a function get_third_element that accepts a list and returns the third element. Ensure IndexError is handled.

player_list = ["Ronaldo", "Messi", "Nyemar", "Debruyne", "Halland"]


def get_third_element(player_list):
    try:
        return player_list[2]

    except IndexError:
        return "There are only two elements in the list"


# Testing
print(get_third_element(player_list))  # Output: Nyemar
print(
    get_third_element(["Ronaldo", "Messi"])
)  # Output: The list has less than three elements.


# EXERCISE 2: RAISING ERROR

# Write a function can_drink that takes age and checks if user can drink. If user is 18+, return True else return False. Note: You need to raise TypeError if age is not integer value, ValueError if age is below 0, AssertionError if age is above 100.


def can_drink(age):
    if type(age) is not int:
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 100:
        raise AssertionError("Age cannot be greater than 100.")
    if age >= 18:
        return True


# Testing
print(can_drink(43.2))  # Age must be an integer.
print(can_drink(-43))  # Age cannot be negative.
print(can_drink(143))  # Age cannot be greater than 100.
print(can_drink(20))  # True
print(can_drink(15))  # False


# Create a function get_age that calculates and returns age on passing DOB. [Hint: You can get current_date from datetime library]. Note: You need to raise appropriate exception if DOB is in invalid format, if DOB is in future. age that is returned by function has to be integer.

from datetime import datetime, date


def get_age(dob):
    try:
        # Step 1: Convert string DOB to date object
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()

    except ValueError:
        # Invalid format
        raise ValueError("Invalid DOB format. Use YYYY-MM-DD")

    # Step 2: Get today's date
    today = date.today()

    # Step 3: Check if DOB is in the future
    if birth_date > today:
        raise ValueError("DOB cannot be in the future")

    # Step 4: Calculate age
    age = today.year - birth_date.year

    # Step 5: Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age = age - 1

    # Step 6: Return age as integer
    return age


# Example usage
print(get_age("2000-10-10"))  # Output depends on current date


# # Exercise 3: Implementation
# # You have employee record details in file employee_info.csv. Your company is hosting a party and needs to plan drink logistics. Write a program that reads the employee_info.csv file, calculates each employee's age using the previously defined function, and determines whether the employee is eligible to drink. Then generate a JSON file named drink_logistic.json in the format {"hard_drink": 5, "soft_drink": 5}, based on the number of employees who can drink and those who cannot.

import csv
import json
from datetime import datetime


# Step 1: Function to calculate age
def get_age(dob_year):
    current_year = datetime.now().year
    if dob_year > current_year:
        raise ValueError("DOB cannot be in the future")
    return current_year - dob_year


# Step 2: Initialize counters
hard_drink = 0
soft_drink = 0

# Step 3: Read CSV file
with open("employee_info.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dob = int(row["DOB"])

        # Step 4: Calculate age
        age = get_age(dob)

        # Step 5: Check eligibility
        if age >= 18:
            hard_drink += 1
        else:
            soft_drink += 1

# Step 6: Create result dictionary
result = {"hard_drink": hard_drink, "soft_drink": soft_drink}

# Step 7: Write to JSON file
with open("drink_logistic.json", "w") as file:
    json.dump(result, file, indent=4)

print("Drink logistics file created successfully!")
