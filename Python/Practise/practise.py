# Assign list with numbers. Find the  largest number in it using for loop.
num_list = [4, 12, 7, 25, 9]
largest=num_list[0]
for num in num_list:
    if(num>largest):
        largest=num

print("The Largest number: ",largest)

# Assign list with numbers. Find the  smallest number in it using for loop.
num_list = [4, 12, 7, 25, 9]
smallest=num_list[0]
for num in num_list:
    if(num<smallest):
        smallest=num

print("The Largest number: ",smallest)

# Assign list with numbers. Find the second largest number in it using for loop.
num_list = [1, 3, 5, 2, 12, 22, 32]
largest=float('-inf')
second_largest=float('-inf')

for num in num_list:
    if(num>largest):
        second_largest=largest
        largest=num
    elif(num>second_largest and num!=largest):
        second_largest=num
        
print("Second largest number is:", second_largest)


# Record of student is stored as {'9843': {'course': 'Python', 'name': 'Ram', 'present': False}, {'9844': {'course': 'Java', 'name': 'Shyam', 'present': True}}. Using loop, display name of student who are absent in Python class.
student_record = {
    '9843': {'course': 'Python', 'name': 'Ram', 'present': False},
    '9844': {'course': 'Java', 'name': 'Shyam', 'present': True}
} 
# student_id is key and inner dictionary (details) is value here
for student_id, details in student_record.items():
    if (details['course']=='Python' and not details['present']):
        print(details['name'])


# Store a fruits names in a list. Generate a new list from it such that if fruit name starts with a/A then it has to be converted to uppercase else it has to be converted to lowercase. Use both for loop and list comprehension.
fruits = ['Apple', 'banana', 'avocado', 'Cherry', 'apricot', 'Mango']
new_list = []
for fruit in fruits:
    if fruit.lower().startswith('a' or 'A'):
        fruit_upper=fruit.upper()
        new_list.append(fruit_upper)
    else:
        fruit_lower=fruit.lower()
        new_list.append(fruit_lower)

print("New list using for loop:", new_list)


# List Comprehension
fruits = ['Apple', 'banana', 'avocado', 'Cherry', 'apricot', 'Mango']
new_fruit_list= [fruit.upper() if fruit.lower().startswith('a' or 'A') else fruit.lower() for fruit in fruits ]
print(new_fruit_list)


# Write function to check if a number is prime or not. Using this function, generate list of first 20 prime numbers.
def is_prime(n):
    count = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False

# Test
print(is_prime(7))   # True
print(is_prime(6))   # False


def prime_num(num):
    if(num<2):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return False
    return True

# Test
print(prime_num(3))  # True
print(prime_num(10)) # False


# Iterator and Generator
# Checking Prime Number and Generating
def is_prime(num):
    for i in range(2,num-1):
        if(num%i==0):
            return False
    return True

# Generator
def prime_generator(x,y):
    while x<y:
        if is_prime(x):
            yield x
        x=x+1
        
my_prime_generator=prime_generator(1,1000000)

while True:
    my_prime=next(my_prime_generator) 
    print(my_prime,end="..")
    



        