# 🔹 SET
# A set is a collection of:
# Unordered
# Unique elements (no duplicates)
# Mutable (you can add/remove items)
# 👉 Think of it like a bag of non-repeating values.


# 🔹 Creating a Set
s = {1, 2, 3, 4}
print(s)


# Using set():
s = set([1, 2, 3])  # This function will convert list into set
print(s)


# 🔹 No Duplicates Allowed
s = {1, 2, 3, 2, 4}
print(s)  # Output: {1, 3, 2 , 4 } remove the first ones occurrence and keep last one


# 🔹 Unordered Nature
s = {10, 20, 30}
print(s)  # Order may vary, so there is no index in set

print("------------------ END BASIC -------------------------")


# SET METHOD
# 1. 🔹 Adding Elements

# A. add()
s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}


# B. update() (add multiple values)
s = {1, 2}
s.update([3, 4, 5])
print(s)  # {1, 2, 3, 4, 5}


# 2. Removing Elements

# A. remove()
s = {1, 2, 3}
s.remove(2)

# ❌ Error if element not found


# B. discard()
s.discard(5)  # No error


# C. pop()
s = {1, 2, 3}
print(s.pop())  # Removes random element


# D. clear()
s.clear()  # Empties the set


print("------------------ END SET METHODS -------------------------")


# 🔹 SET OPERATIONS (Very Important 🔥)

# 1. Union (|)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # {1, 2, 3, 4, 5}


# 2. Intersection (&)

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # {3}


# 3. Difference (-)

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)  # {1, 2}


# 4. Symmetric Difference (^)

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)  # {1, 2, 4, 5} # EXCLUDE THE COMMON ONES

print("------------------ END SET OPERATIONS -------------------------")


# 🔹 SET METHODS

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print("------------------ END SET METHODS -------------------------")


# 🔹 MEMBERSHIP CHECK

s = {1, 2, 3}

print(2 in s)  # True
print(5 in s)  # False


# 🔹 ❌ Indexing Not Allowed
s = {1, 2, 3}
print(s[0])  # ❌ Error


# 🔹 Frozen Set (Immutable Set)
fs = frozenset([1, 2, 3])

# Cannot add/remove elements
