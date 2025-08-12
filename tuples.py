'''
A tuple is an ordered collection of items in Python that is immutable — meaning you cannot change, add, or remove elements after it’s created.

They are like lists, but safer when you don’t want data to change.
'''


'''
a = (1,2,3)
t2 = 1,2,3,4
b = ()
c = (10,) #if coma will be there it will be tuple
d = (10) # otherwise int
print(type(a))
print(type(t2))
print(type(b))
print(type(c))
print(type(d))
'''


'''
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[-1])

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])   
print(numbers[::-1]) 
'''


'''
data = (1, 2, 3)
data[0] = 10 #TypeError: 'tuple' object does not support item assignment
'''


'''
# tuple packing
human = ("pratibha", 22, "Female")

# tuple unpacking
name, age, gender = human
print(name)
print(age)
print(gender)

# tuple method it have only two method
data = (1,3, 2, 4, 5, 3, 3)
print(data.count(3))
print(data.index(3))

nested_t = (1, (2, 3),(4, 5, 6))
print(nested_t)
print(nested_t[0])
print(nested_t[1])
print(nested_t[2])

print(nested_t[0])  #0 is for backet 1 at start 
print(nested_t[1][0]) #1 is for backet 2 at center
print(nested_t[2][1])   #2 is for backet 3 at last 
'''

'''
# Use these tuples for reference:
fruits = ("apple", "banana", "cherry", "mango")
numbers = (10, 20, 30, 10, 20, 20, 30, 20, 40, 40, 50, 60, 70)
nested_tuple = (1, (2, 3), (4, 5, 6))

print("\nQ1: Access \"banana\" from the fruits tuple.")
print(fruits[1])

print("\nQ2: Access the last element \"mango\" using negative indexing.")
print(fruits[-1])

print("\nQ3: Slice the numbers tuple to get (20, 30, 40).")
print(numbers[1:4])

print("\nQ4: Reverse the numbers tuple using slicing.")
print(numbers[::-1])

print("\nQ5: Unpack fruits into 4 variables and print them.")
red, yellow, darkred, orangeyellow = fruits
print(red)
print(yellow)
print(darkred)
print(orangeyellow)

print("\nQ6: From nested_tuple, access only 3 and 5.")
print(nested_tuple[1][1])
print(nested_tuple[2][1])

print("\nQ7: Count how many times 20 appears") 
num = numbers.count(20)
print(num)

print("\nQ8: Find the index of 40 in numbers.")
print(numbers.index(40))

print("\nQ9: Create a tuple without using parentheses and print its type.")
digit = 1,2,3,4,5,6
print(type(digit))

print("\nQ10: Check if \"apple\" exists in fruits.")
print("kiwi" in fruits)
'''
