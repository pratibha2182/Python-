'''
A dictionary is:
Unordered, Key–Value pairs, Mutable, Keys must be immutable (string, int, tuple, etc.), Values can be any data type
'''

'''
# direct creating dictonary
myDict = {"name": "Pratibha", "age": 22, "gender": "Female"}
print(myDict)
print(type(myDict))

# using dict method
dictMy = dict(name = "Pratibha", age= 22, gender="Female")
print(dictMy)
print(type(dictMy))

empty = {}
print(type(empty))
'''


'''
# accessing dictionary values
human = {"name": "Pratibha", "age": 22, "gender": "Female", "district": "Valsad"}
print(human["name"])
print(human.get("name"))
print(human["age"])
print(human.get("age"))
print(human["gender"])
print(human.get("gender"))
'''


'''
# adding and updating
human["age"] = 23  #updating
print(human["age"])
print(human.get("age"))  
human["district"] = "Valsad"  #adding
print(human["district"])
print(human.get("district"))
'''

'''
# removing
human.pop("age")  #remove age key and return value
print(human)
human.popitem()  # remove valsad last interted
print(human)
del human["name"]  #delete name key 
print(human)
human.clear()  #empty the whole human dict
print(human)
'''

'''
looping thorugh dictionary
person = {"name": "John", "age": 25, "city": "New York"}

for key in person:
    print(key)  #only name age and city key

for value in person.values():
    print(value)  #only john 25 new york values

for key, value in person.items():
    print(key, ":" , value)  #both key+value
'''


'''
# nested dictionary
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])
print(students["student1"]["age"])

print(students["student2"]["name"])
print(students["student2"]["age"])
'''


'''
# Dictionary Methods
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  
print(my_dict.values())
print(my_dict.items())
'''


'''
A dictionary comprehension in Python is a concise way to create dictionaries using a single line of code

# squares
squares = {x: x**2 for x in range(6)}
print(squares)

# cubes
cubes = {x: x**3 for x in range(10) if x % 2 == 0}
print("Even cubes: ", cubes)

# discount 
prices = {"apple": 50, "banana": 20, "cherry": 75}
discount = {item: price*0.8 for item, price in prices.items()}  #90% of items prices
print(discount)
'''

# Q1: Create a dictionary with keys: name, age, country and assign your details.
dict = {"name": "Pratibha", "age": 22, "country" : "India"}
print(dict)
# Q2: Given this dictionary:
student = {"name": "Alice", "age": 20, "marks": 85}
#  - Update the marks to 90
student["marks"] = 90
#  - Add a new key "grade" with value "A"
student["grade"] = "A"
#  - Print updated dictionary
print(student)

# Q3: Access the value of "marks" without causing an error if the key doesn't exist.
print(student.get("mark"))

# Q4: Remove the "age" key from the dictionary.
student.pop("age")
print(student)

# Q5: Loop through the dictionary and print each key and value in format: Key -> value
for key, value in student.items():
    print(key, "=>", value)

# Q6: Create a nested dictionary for two employees with name, age, and salary. Access and print the salary of the second employee.
employee = {
    "employee1" : {"name":"karan" , "age":27},
    "employee2" : {"name":"rahul" , "age":23}
}
print(employee["employee2"]["age"])

# Q7: Merge these two dictionaries:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# dict1.update(dict2) #merging use update
# print(dict1)

merged = {**dict1, **dict2}
print(merged)

# Q8: Using dictionary comprehension, create a dictionary where the keys are numbers 1 to 5 and values are their cubes.
cubess = {x: x**3 for x in range(1, 6)}
print(cubess)

# Q9: Check if key "country" exists in a dictionary.
if "country" in dict:
    print("Yes")
else:
    print("No")

# Q10: Convert this list into a dictionary where each item becomes a key with value True:
fruits = ["apple", "banana", "cherry"]
dict3 = {fruit: True for fruit in fruits}
print(dict3) 
