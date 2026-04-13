# A dictionary is a collection of data stored in key–value pairs
# Key Features
# Unordered (in older versions; now maintains insertion order)
# Mutable (you can change values)
# Keys must be unique & keys must be immutable (string, integer, float, tuple), list and set can be the key as they are mutable
# Values can be any data type

# CREATING DICTIONARY
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}


# 🔹 ACCESSING VALUES
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}

print(d["name"])  # Ram
print(d.get("age"))  # 20

# 👉 Difference:
# d["key"] → error if key not found
# d.get("key") → returns None (safe)

print("-----------------END DICTIONARIES CREATION AND ACCESS----------------------")


# ADDING VALUES
# A. ADDING VALUES
d = {"name": "Ram"}
# Add new key
d["age"] = 20
print(d)


# B. UPDATING EXISTING VALUES
d["name"] = "Shyam"
print(d)

print("-----------------END DICTIONARIES ADDING  AND UPDATE VALUES----------------------")


# 🔹 Removing Elements
# 1. pop() :
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
d.pop("age") # remove age


# 2. del
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
del d["name"] # remove name


# 3. clear()
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
d.clear()  # removes everything

print("-----------------END DICTIONARIES REMOVES ----------------------")


# 🔹 DICTIONARY METHODS

# 1. keys()
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
print(d.keys())  # OUTPUT: # dict_keys(['name', 'age', 'city'])


# 2. values()
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
print(d.values()) # OUTPUT: dict_values(['Ram', 20, 'Kathmandu'])



# 3. items()
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
print(d.items()) # OUTPUT: # dict_values(['Ram', 20, 'Kathmandu'])



# 4. len():
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
print(len(d))



 # 5. Copy() : 
#  🔹 1. Using = (Not a real copy ❌)
d1 = {"name": "Ram", "age": 20}
d2 = d1
d2["age"] = 25

print(d1)  # {'name': 'Ram', 'age': 25}
print(d2)  # {'name': 'Ram', 'age': 25}

# 👉 Both variables point to the same dictionary



# 🔹 2. Using .copy() (Shallow Copy ✅)
d1 = {"name": "Ram", "age": 20}
d2 = d1.copy()
d2["age"] = 25

print(d1)  # {'name': 'Ram', 'age': 20}
print(d2)  # {'name': 'Ram', 'age': 25}

# 👉 Creates a new dictionary


# 6. Membership
d1 = {"name": "Ram", "age": 20}
print("name" in d )
print("gender" in d)


print("-----------------END DICTIONARIES METHODS ----------------------")


# 🔹 Looping Through Dictionary

d = {"name": "Ram", "age": 20}

# Loop keys
for key in d:
    print(key)

# Loop values
for value in d.values():
    print(value)

# Loop both
for key, value in d.items():
    print(key, value)


print("-----------------END DICTIONARIES LOOP ----------------------")


# 🔹 Nested Dictionary
d = {
    "student1": {"name": "Ram", "age": 20},
    "student2": {"name": "Shyam", "age": 22}
}

print(d["student1"]["name"])  # Ram


# LOOP THE NESTED DICTIONARIES

for student, details in d.items():
    print(f"{student}:")
    
    for key, value in details.items():
        print(f"  {key} -> {value}")
        
"""
OUTPUT:
student1:
  name -> Ram
  age -> 20
student2:
  name -> Shyam
  age -> 22
"""


print("-----------------END NESTED DICTIONARIES  ----------------------")


# 🔹 Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 🔹 Check if Key Exists
d = {"name": "Ram", "age": 20, "city": "Kathmandu"}
print("name" in d)   # True
print("salary" in d) # False




