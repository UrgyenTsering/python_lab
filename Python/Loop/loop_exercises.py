# Exercise 1: Loop Basics
# Display numbers from 1 to 10 using both for and while loops.
# FOR LOOP
for item in range(1, 11):
    print(item)

# WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i = i + 1
print("END")

# Assign num_tuple as (1, 4, 7, 12, 20). Using loop, find even numbers and their sum?
num_tuple = (1, 4, 7, 12, 20)
total = 0
for i in num_tuple:
    if i % 2 == 0:
        print(i)
        total += i
print(f"Total of even numbers:{total}")

# Assign num_set as {1, 3, 5, 7, 9}. Using loop, find odd numbers and their product
num_set = {1, 3, 5, 7, 9}
product = 1
for num in num_set:
    if num % 2 != 0:
        print(num)
        product *= num
print(f"Product of odd numbers:{product}")

# Ask user for number and display it's factorial using both for and while loops.
num = int(input("Enter a num:"))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("factorial:", factorial)


num = int(input("Enter a num:"))
i = 1
fac = 1
while i <= num:
    fac = fac * i
    i = i + 1
print("factorial:", fac)


# Assign list with numbers. Find the second largest number in it using for loop.
num_list = [1, 3, 5, 2, 12, 22, 32]
largest = float("-inf")
second_largest = float("-inf")

for num in num_list:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number is:", second_largest)


# Assign set as {1, 4, 5, 7, 8, 12}. Generate new list evaluated_data using for loop such that odd number is doubled and even number is tripled. If you encounter 4, skip evaluation for this and if you see 8, stop the loop.
data_set = {1, 4, 5, 7, 8, 12}
evaluated_data = []
for num in data_set:
    if num == 4:
        continue
    if num == 8:
        break
    if num % 2 == 0:
        evaluated_data.append(num * 3)
    else:
        evaluated_data.append(num * 2)

print(evaluated_data)

# Exercise 2: Using Loops

# Record of student is stored as {'9843': {'course': 'Python', 'name': 'Ram', 'present': False}, {'9844': {'course': 'Java', 'name': 'Shyam', 'present': True}}. Using loop, display name of student who are absent in Python class.
student_record = {
    "9843": {"course": "Python", "name": "Ram", "present": False},
    "9844": {"course": "Java", "name": "Shyam", "present": True},
}
# student_id is key and inner dictionary (details) is value here
for student_id, details in student_record.items():
    if details["course"] == "Python" and not details["present"]:
        print(details["name"])


# Store a fruits names in a list. Generate a new list from it such that if fruit name starts with a/A then it has to be converted to uppercase else it has to be converted to lowercase. Use both for loop and list comprehension.
fruits = ["Apple", "banana", "avocado", "Cherry", "apricot", "Mango"]
new_list = []
for fruit in fruits:
    if fruit.lower().startswith("a"):
        fruit_upper = fruit.upper()
        new_list.append(fruit_upper)
    else:
        fruit_lower = fruit.lower()
        new_list.append(fruit_lower)

print("New list using for loop:", new_list)


# List Comprehension
fruits = ["Apple", "banana", "avocado", "Cherry", "apricot", "Mango"]
new_fruit_list = [
    fruit.upper() if fruit.lower().startswith("a") else fruit.lower()
    for fruit in fruits
]

print(new_fruit_list)


# Write function to check if a number is prime or not. Using this function, generate list of first 20 prime numbers.
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


# Generate list of first 20 prime numbers
primes = []
num = 2
while len(primes) < 20:
    if is_prime(num):
        primes.append(num)
    num += 1
print("First 20 prime numbers:", primes)


# Write function that accepts string from user and returns a dictionary for occurrences of a character in it. Ex: apple => {'a': 1, 'p': 2, 'l': 1, 'e': 1}.
def dict_convertor(text):
    text_dict = {ch: text.count(ch) for ch in text}
    return text_dict


text = input("Enter a text:")
print(dict_convertor(text))


# Exercise 3: Loop Challenges
# Write function to take string as input and provide output with below condition: First letter of word always have to be capital If preceding letter occurs earlier in dictionary then letter has to be capital If preceding letter occurs later in dictionary then letter has to be small If preceding letter is same as current letter then no change in case. Example: applE is fruit => APple IS FRUiT A => 1st Letter(upper), 1st P => Preceding(A) occur earlier (upper), 2nd P => Preceding(P) same(no_change), L => Preceding(P) occurs later (small), e => Preceding(L) occurs later(small), I => 1st letter(upper) and so on. explain the question. expalin in simplest way


def string_case_convertor():
    sentence = input("Enter the sentence")
    words = sentence.split()
    result = []

    for word in words:
        new_word = word[0].upper()  # first letter always uppercase

        for i in range(1, len(word)):
            prev = word[i - 1].lower()
            curr = word[i]

            if prev < curr.lower():
                new_word += curr.upper()
            elif prev > curr.lower():
                new_word_ = curr.lower()
            else:
                new_word += curr  # no change
        result.append(new_word)
    return " ".join.result


print(string_case_convertor)
