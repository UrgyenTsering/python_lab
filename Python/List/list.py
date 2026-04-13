# A list is a collection of items stored in order.
my_list = [1, 2, 3, 4]
print(my_list)
print("--------------------------------")

# LIST METHOD

# 1. POSITIONAL:
# A. list indexing: selecting one or single element from list

# Element:   10   20   30   40   50
# Index:      0    1    2    3    4

l = [10, 20, 30, 40]
print(l[0])  # 10
print(l[1])  # 20
print(l[-1])  # 40
print(l[-2])  # 30


# A. Slicing: grouping elements using start, end, and step

# Element:   10   20   30   40   50
# Index:      0    1    2    3    4

l = [10, 20, 30, 40, 50]

print(l[1:4])  # [20, 30, 40]
print(l[:3])  # [10, 20, 30]
print(l[1:])  # [20, 30, 40, 50]
print(l[::2])  # [10, 30, 50] # steps is used
print(l[::-1])  # [50, 40, 30, 20, 10]
print(
    l[-4:-1]
)  # [20, 30, 40] # negative slicing: negative index is count from backside. start (-ve index) is include but end (-ve index) is excluded

print("-------------END POSITION-------------------")


# 2. GENERIC

# A. REPETITION : Repetition is the process of repeating a LIST multiple times using the * operator.

l = [1, 2]
print(l * 3)  # OUTPUT: [1, 2, 1, 2, 1, 2]


# B. CONCATENATION : combining two list into one

a = [1, 2]
b = [3, 4]

print(a + b)  # [1, 2, 3, 4]


# C. MEMBERSHIP (IN, NOT IN)
# Checks if element exists in list

l = [10, 20, 30]

print(20 in l)  # True
print(50 not in l)  # True

print("-------------END GENERIC-------------------")


# 3. MODIFICATION METHODS

# A. append() – Add element at the end
l = [1, 2]
l.append(3)
print(l)  # [1, 2, 3]


# B. pop() – Remove last element (or by index) and return it
l = [1, 2, 3]
x = l.pop()
print(x)  # 3
print(l)  # [1, 2]


# C. insert() – Add element at a specific index
l = [1, 2, 3]
l.insert(1, 99)
print(l)  # [1, 99, 2, 3]


# D. remove() – Remove first occurrence of a value
l = [1, 2, 3, 2]
l.remove(2)
print(l)  # [1, 3, 2]


# E. clear() – Remove first occurrence of a value
l = [1, 2, 3]
l.clear()
print(l)  # []


# F. del() – Delete element by index or entire list
l = [1, 2, 3]
del l[1]
print(l)  # [1, 3]

del l  # deletes entire list

# G. sort() – Sort elements ascending by default
l = [3, 1, 2]
l.sort()
print(l)  # [1, 2, 3]


# H. reverse() – Reverse order of elements
l = [1, 2, 3]
l.reverse()
print(l)  # [3, 2, 1]

# I. extend() – Add multiple elements from another list
l = [1, 2]
l.extend([3, 4])
print(l)  # [1, 2, 3, 4]

# Concatenation (+) – Combine two lists (creates new list)
a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]

print("-------------END MODIFICATION-------------------")

# 4. NUMERIC
# A. sum(): Calculates the total sum of all elements in an iterable (like a list or tuple).

numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)  # Output: 100


# Using start
total = sum(numbers, 50)
print(total)  # Output: 150


# B. min(): Returns the smallest element in an iterable.
numbers = [10, 20, 30, 5, 15]
print(min(numbers))  # Output: 5

# C. max(): Returns the largest element in an iterable.
numbers = [10, 20, 30, 5, 15]
print(max(numbers))  # Output: 30

# D. len() : Returns the number of items in an object (list, string, tuple, dictionary, etc.).
numbers = [10, 20, 30, 40]
print(len(numbers))  # Output: 4

text = "Python"
print(len(text))  # Output: 6

# E. count() : Counts how many times a specific value appears in a list, tuple, or string.

numbers = [10, 20, 30, 20, 20, 40]
print(numbers.count(20))  # Output: 3

text = "banana"
print(text.count("a"))  # Output: 3

print("-------------END NUMERIC METHOD-------------------")


# COPYING LIST
# 1. Using = (Not a real copy)
list1 = [1, 2, 3, 4]
list2 = list1  # This does NOT create a new list

list2.append(5)
print(list1)  # Output: [1, 2, 3, 4, 5]
print(list2)  # Output: [1, 2, 3, 4, 5]

# Here, list2 is just another reference to list1. Changing one affects the other.


# 2. Using list.copy() (Shallow copy) :
list1 = [1, 2, 3, 4]
list2 = list1.copy()  # Creates a new list

list2.append(5)
print(list1)  # Output: [1, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4, 5]

print("-------------END COPY METHOD-------------------")


# ZIP FUNCTION : Used to combine two or more iterables (like lists, tuples, etc.) element-wise into a single iterable of tuple

names = ["Rabindra", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))  # [("Rabindra", 25), ("Bob", 30), ("Charlie", 35)]

numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]
numbers_3 = [7, 8]
zipped_numbers = zip(numbers_1, numbers_2, numbers_3)
print(list(zipped_numbers)) # [(1, 4, 7), (2, 5, 8)] (stops at shortest iterable length)