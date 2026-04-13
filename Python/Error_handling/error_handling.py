
# BASIC STRUCTURE OF ERROR HANDLING
try:
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2
except ValueError:
    # Handle invalid input (not a number)
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Cannot divide by zero!")
else:
    # Runs if no error occurred
    print(f"The result of {num1} divided by {num2} is {result}")
finally:
    # Always runs
    print("Calculation attempt finished.")
    
    

# ADD A GENERIC ERROR HANDLER USING EXCEPT EXCEPTION AS e
try:
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2
except ValueError:
    # Handle invalid input (not a number)
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Cannot divide by zero!")
except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occurred:", e)
else:
    # Runs if no error occurred
    print(f"The result of {num1} divided by {num2} is {result}")
finally:
    # Always runs
    print("Calculation attempt finished.")
    
    
# ASSERTION
# An assertion is a way to check if a condition is true while your program is running.
# If the condition is True → program continues
# If the condition is False → program stops with an error
# 👉 It is mainly used for debugging and catching mistakes early.


# SYNTAX
# assert condition, "Error message"

# SIMPLE EXAMPLE
x = 10
assert x > 0, "x should be positive"

print("Program continues...")

# OUTPUT: Program continues...

# If condition is False
x = -5
assert x > 0, "x should be positive"
print("Program continues...")

# OUTPUT: x should be positive


# EXAMPLE 2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Assertion to prevent division by zero
assert num2 != 0, "Second number must not be zero!"

result = num1 / num2
print("Result:", result)


# Important Tip:
# Use assert for developer mistakes (logic errors)
# Use try-except for user input errors



# RAISING GENERIC EXCEPTIONS
# Manually raising errors when condition is not matched in the program.
# It is used when:
# You detect something is wrong
# You want to stop execution and show an error 

# Basic Example
num = int(input("Enter a number: "))

if num < 0:
    raise Exception("Number cannot be negative!")

print("Valid number:", num)

# OUTPUT:  If user enters -5, program raises an error. 'Number cannot be negative!'


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        raise Exception("Cannot divide by zero!")

    result = num1 / num2
    print("Result:", result)

except Exception as e:
    print("Error:", e)