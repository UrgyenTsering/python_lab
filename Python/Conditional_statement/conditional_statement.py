# CONDITIONAL STATEMENT :
# A conditional statement lets your program make decisions based on a condition (True or False).


# 🔹 1. if Statement :
# Executes code only if the condition is True.
age = 18

if age >= 18:
    print("You are an adult")

# OUTPUT: You are a adult


# 🔹 2. if-else Statement :
# Runs one block if condition is True, another if False.

age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# OUTPUT: You are a minor


# 🔹 3. if-elif-else Statement ( if ladder ) :
# 🔹 3. if-elif-else Statement

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

# OUTPUT: Grade: A


# 🔹 4. Nested if
# You can put if statements inside another if.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can vote")
    else:
        print("You need an ID to vote")
else:
    print("You are too young to vote")

# OUTPUT: You can vote
