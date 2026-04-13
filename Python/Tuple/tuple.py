
# TUPLE :
# A tuple is a collection of items in ()bracket
# Ordered (keeps the order)
# Immutable (cannot be changed after creation)
# Allows duplicate values

# Creating a Tuple
t = (10, 20, 30, 40)
print(t)


# You can also create without parentheses:
t = 10, 20, 30
print(t)


# Single Element Tuple
# ⚠️ Important: You must use a comma
t = (5,)   # Correct
t = (5)    # Not a tuple, it's an int

print( "------------- END TUPLE CREATION ----------------------")

# ❌ TUPLE IS IMMUTABLE
t = (10, 20, 30)
t[0] = 100   # ❌ Error (cannot change)


print( "------------- END TUPLE IMMUTABLE ----------------------")


# 🔹 Tuple Packing & Unpacking
# Packing (define) : 
t = (1, 2, 3)

# Unpacking :
a, b, c = t
print(a, b, c)  # 1 2 3


# another example : tuple unpacking with * (star expression)
a, *b = (1, 2, 3)

print(a)  # 1
print(b)  # [2, 3]


print("--------------END TUPLE PACKING AND UNPACKING ------------------")


# 1. POSITIONAL METHOD

# A. Accessing Elements (Indexing)
t = (10, 20, 30, 40)

print(t[0])  # 10
print(t[1])  # 20
print(t[-1])  # 40
print(t[-2])  # 30

# B. Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])  # [20, 30, 40]
print(t[:3])  # [10, 20, 30]
print(t[1:])  # [20, 30, 40, 50]
print(t[::2])  # [10, 30, 50] # steps is used
print(t[::-1])  # [50, 40, 30, 20, 10]


print("--------------END POSITIONAL METHOD------------------")


# Tuples have only 2 main methods:

# A. 1. count(): Counts occurrences
t = (1, 2, 2, 3, 2)
print(t.count(2))  # 3


# 2. index(): Find the position of element
t = (10, 20, 30)
print(t.index(20))  # 1



# Other Useful Functions
t = (10, 20, 30, 40)

print(len(t))   # 4
print(min(t))   # 10
print(max(t))   # 40
print(sum(t))   # 100

print("--------------END TUPLE METHOD------------------")







