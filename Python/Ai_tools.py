# command +i for Ai Generate Code: Github copilot
# black formatter
# command shift p : for black formatter

num_values = ["1", "2", "3"]
int_values = list(map(int, num_values))
print(num_values)
print(int_values)

# command shift p: create virtual
# to activate venv (virtual Environment )
# to deactivate


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    else:
        return n * factorial(n - 1)


# Example usage
print(factorial(5))  # Output: 120
