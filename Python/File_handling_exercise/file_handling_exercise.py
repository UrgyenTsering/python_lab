# Exercise 1: Text Files

# Create a text file python.txt on your desktop and write short essay about python on it.

# File path (Desktop)
python_file_path = "/Users/urgyentsering/Desktop/python.txt"

# Essay content
essay = """Python is a popular and powerful programming language known for its simplicity and readability.
It is widely used in web development, data science, artificial intelligence, and automation.
Python has a large standard library and supports multiple programming paradigms.
Because of its easy syntax, it is a great language for beginners to learn programming.
Overall, Python continues to grow in popularity and is one of the most in-demand languages today.
"""

# Create and write to the file
with open(python_file_path, "w") as file_obj:
    file_obj.write(essay)

print("File created and essay written successfully!")

# # Open this file python.txt. Add text I will learn Error Handling Next at end
text = "I will learn Error Handling Next"
with open(python_file_path, "a") as file_obj:
    file_obj.write(text)

print("File is opened and text is  added at end successfully!")

# # Create a new file java.txt. Copy the content of python.txt to java.txt but replacing the text python with java.

# # File paths
python_file_path = "/Users/urgyentsering/Desktop/python.txt"
java_file_path = "/Users/urgyentsering/Desktop/java.txt"

# Read content from python.txt
with open(python_file_path, "r") as file_obj:
    content = file_obj.read()

# replace text
updated_content = content.replace("Python", "Java").replace("python", "java")

# Write to java.txt
with open(java_file_path, "w") as file_obj:
    file_obj.write(updated_content)

print("Java.txt. file is opened and text is  added at end successfully!")


# Calculate and display the size of python.txt and java.txt in KB. (Hint: use os module & AI)

import os

# File paths
python_file_path = "/Users/urgyentsering/Desktop/python.txt"
java_file_path = "/Users/urgyentsering/Desktop/java.txt"

# Get file sizes in bytes
python_size_bytes = os.path.getsize(python_file_path)
java_size_bytes = os.path.getsize(java_file_path)

# Convert bytes to KB (1 KB = 1024 bytes)
python_size_kb = python_size_bytes / 1024
java_size_kb = java_size_bytes / 1024

# Display results
print(f"Size of python.txt: {python_size_kb:.2f} KB")
print(f"Size of java.txt: {java_size_kb:.2f} KB")


# Read file nobel_prize_speech.txt and display most repeated word on it.

with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/nobel_prize_speech.txt",
    "r",
) as file_obj:
    content = file_obj.read()

# Convert text to lowercase
content = content.lower()


# Remove punctuation using list comprehension and String method
import string

content = "".join(
    [ch for ch in content if ch not in string.punctuation] # List comprehension keeps only characters that are not punctuation. (string.punctuation) This is a string containing all common punctuation marks. ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'f', 'u', 'n']
)  
# ''.join() will take all elements of list and combine into one string using ''(space separator)

# Split text or single string ready by read() into list of words
words = content.split()

# Count word frequencies using a dictionary
# word_count = {} # empty dic to store the word and its occurrence
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# dictionary comprehension
word_count = {word: words.count(word) for word in words}  # words.count(word) → counts how many times each word appears in the list. 

# Find the most repeated word
most_common_word = max(word_count, key=word_count.get)
print(
    f"The most repeated word is '{most_common_word}' with {word_count[most_common_word]} occurrences."
)




# Exercise 2: CSV Files
# Create a csv file std_1.csv with columns: Name, Age, Grade. Add 5 records to it using list of list.

#  list of list
import csv

header = ["Name", "Age", "Grade"]
student_info = [
    ["Urgyen", 19, 11],
    ["Kancha", 16, 10],
    ["Karma", 14, 7],
    ["Pema", 16, 10],
    ["Sunil", 18, 12],
]

with open("std_1.csv", "w", newline="") as file_obj:
    csv_writer = csv.writer(file_obj)
    csv_writer.writerow(header)
    csv_writer.writerows(student_info)


# Create a csv file std2.csv with columns: Name, Age, Grade. Add 5 records to it using list of dict.

# list of dict
import csv

header = ["Name", "Age", "Grade"]
student_info = [
    {"Name": "Urgyen", "Age": 19, "Grade": 11},
    {"Name": "Kancha", "Age": 16, "Grade": 10},
    {"Name": "Karma", "Age": 14, "Grade": 7},
    {"Name": "Pema", "Age": 16, "Grade": 10},
    {"Name": "Sunil", "Age": 18, "Grade": 12},
]

with open("std2.csv", "w", newline="") as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=header)
    csv_writer.writeheader()
    csv_writer.writerows(student_info)


# Read file 2022-01-03.csv and display records as list of list.
# Converting csv data into list of list
import csv

with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/2022-01-03.csv",
    "r",
) as file_obj:
    csv_reader = csv.reader(file_obj)
    data_in_list = list(csv_reader)
    print(data_in_list)


# Read file 2022-01-03.csv and display records as list of dict.
# Converting csv data into list of dict
import csv

with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/2022-01-03.csv",
    "r",
) as file_obj:
    csv_reader = csv.DictReader(file_obj)
    data_in_list = list(csv_reader)
    print(data_in_list)


# Exercise 3: JSON File
# Store 5 students data in dict as {"9843": {"name": "Rabindra", "age": 30, "course": "Python"}, "9844": {"name": "Hari", "age": 25, "course": "Java"}....}. Save this data in file info.json.

# Note: Question pattern not matching
import json

data = {
    "9843": {"name": "Rabindra", "age": 30, "course": "Python"},
    "9844": {"name": "Hari", "age": 25, "course": "Java"},
}
with open("info.json", "w") as file_obj:
    json.dump(data, file_obj, indent=4)


# Load info.json file. Convert the data in list of dictionary like [{"phone": "9843", "name": "Rabindra", "age": 30, "course": "Python"}, ....]. Save coverted data in info.csv file.

import json

with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/info.json"
) as file_obj:
    data = json.load(file_obj)
    # print(data)

# Step 2: Convert to list of dictionaries
converted_data = []
for phone, details in data.items():
    row = {
        "phone": phone,
        "name": details["name"],
        "age": details["age"],
        "course": details["course"],
    }
    converted_data.append(row)

# Step 3: Write or Convert to CSV
with open("info.csv", "w", newline="") as file_obj:
    headers = ["phone", "name", "age", "course"]
    csv_writer = csv.DictWriter(file_obj, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(converted_data)

print("Conversion completed!")


# Read file election_result.json. Find name of winner, associated party and votes obtained

import json

# Step 1: Load JSON file
with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/election_result.json",
    "r",
) as file_obj:
    data = json.load(file_obj)
    # print(data)

# Step 2: Initialize variables
max_votes = 0
winner_name = ""
winner_party = ""

# # Step 3: Loop through data of each candidate and extract important data from dictionary
for item in data:
    name = item["CandidateName"]  # extracting candidate name from dic
    party = item["PoliticalPartyName"]
    votes = item["TotalVoteReceived"]

    # Step 4: Compare votes
    if votes > max_votes:
        max_votes = votes
        winner_name = name
        winner_party = party

# print DETAILS
print(
    f"The winner is {winner_name} of {winner_party} with maximum votes of {max_votes}"
)


# Read file election_result.json. Find total vote casted and average vote per candidate.

import json

# Step 1: Load JSON file
with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/election_result.json",
    "r",
) as file_obj:
    data = json.load(file_obj)
    # print(data)

total_vote_casted = 0
for item in data:
    candidate_name = item["CandidateName"]
    total_vote_received_per_candidate = item["TotalVoteReceived"]
    print(f"{candidate_name}")
    total_vote_casted = total_vote_casted + total_vote_received_per_candidate

average_vote_per_candidate = total_vote_casted / len(item)

print(f"Total Vote Casted:{total_vote_casted}")
print(f"Average Vote Casted:{average_vote_per_candidate}")


# Convert the file election_result.json in csv format and save it as election_result.csv.
import json

# Step 1: Load JSON file
with open(
    "/Users/urgyentsering/Desktop/Data Science/Python/File_handling_exercise/election_result.json",
    "r",
) as file_obj:
    data = json.load(file_obj)
# print(data)

# Step 2: Get headers from keys of first dictionary
headers = data[0].keys() # pick keys from the fist list of dictionary which is data[0]

# step 3: converting into or creating a CSV file
import csv

# NOTE: SON data is a list of dictionaries, but csv.writer works best with lists of values.Easier approach: use csv.DictWriter, which writes dictionaries directly.
with open("election_result.csv", "w", newline="") as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=headers)
    csv_writer.writeheader()  # Write header row
    csv_writer.writerows(data)  # Write data rows

print("CSV file created successfully!")
