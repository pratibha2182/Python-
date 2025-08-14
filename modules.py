'''
A module in Python is simply a file containing Python code (functions, variables, classes) that you can reuse in other programs.

Why use modules?
Code reusability – write once, use many times.
Organized code – split large programs into smaller, logical files.
Easy collaboration – different people can work on different modules

Built-in Modules : Python comes with many ready-made modules.
'''

'''
# using math 
import math
print(math.sqrt(4))
print(math.pi)
'''


'''
# using random
import random
print(random.randint(1, 10))  # will give auto generate number btween 1 and 10 
print(random.choice([1,10]))  # will give auto generate number btween values provided in the
print(random.sample(range(10),6))  # will give list of 6 value in range of 1 to 10 
fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits)
print("Shuffled list:", fruits)

'''

'''
# using datetime
import datetime
today = datetime.date.today()
print("Today date: ", today)

now = datetime.datetime.now()
print("Current time: ", now.strftime("%H:%M:%S"))
'''

'''
# using os
import os
print(os.getcwd())  #current directory
os.mkdir("Hello")  # create folder
print(os.listdir())  # list files/folders
'''

'''
# using sys
import sys
print(sys.version)  #give version
print(sys.argv) #gives the workspace where you are working
# sys.exit("Exiting now")
'''

'''
# json.dumps()
# Dumps = Dump String
# Converts Python objects (dict, list, tuple, etc.) into a JSON-formatted string.
# Used when sending data over a network or saving to a file as JSON text.
import json
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Analysis"]
}

# json_string = json.dumps(data)
# print(json_string)
output: {"name": "Alice", "age": 25, "skills": ["Python", "Data Analysis"]}

'''


'''
json.dump()
Dump = write JSON directly into a file.

Useful for saving Python objects as JSON without manually handling file write.
# import json

# data = {"name": "Bob", "age": 30}

# with open("data.json", "w") as file:
#     json.dump(data, file)

# json_data = '{"name": "Charlie", "age": 28}'
# python_obj = json.loads(json_data)

# print(python_obj)
# print(python_obj["name"])

output: new data.json file with 
{"name": "Bob", "age": 30}

'''


'''
# json.loads()
# Loads = Load from String.
# Converts a JSON-formatted string into a Python object.
# Used when receiving JSON data from an API.
import json

json_data = '{"name": "Charlie", "age": 28}'
python_obj = json.loads(json_data)

print(python_obj)
print(python_obj["name"])

output: {'name': 'Charlie', 'age': 28}
Charlie
'''

'''
# json.load()
# Load = read JSON from a file and convert it to a Python object.
json.load()
Load = read JSON from a file and convert it to a Python object.
import json

with open("data.json", "r") as file:
    python_data = json.load(file)

print(python_data)

if data.json contains:
{"name": "Bob", "age": 30}

gives output:
{'name': 'Bob', 'age': 30}
if not empty
'''