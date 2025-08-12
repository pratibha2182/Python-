'''
Lists are mutable sequences — unlike strings, you can change them.
'''

'''
print("creating list")
fruits = ["apple","banana","orange"]
print(fruits)

print("\naccessing string")
print(fruits[0])
print(fruits[-1])

print("\nchanging items")
fruits[2] = "orange"
print(fruits)

print("\nadding items at end ")
fruits.append("mango")
print(fruits)

print("\nadding items at betwen or on any index ")
fruits.insert(2,"blueberry")
print(fruits)

print("\nremoving items")
fruits.remove("orange")
print(fruits)

print("\nremoving items using index number")
fruits.pop(2)
print(fruits)


numbers = [10, 40, 20, 30,  60, 50, 70, 80, 90, 100]
print("slicing lists")
print(numbers[1:5])
print(numbers[::-1])

print("\nSorting number in order")
numbers.sort()  # arrange in order automatically 
print(numbers)

print("\nReverse sting using inbuild reverse keyword")
numbers.reverse()
print(numbers)

print("\nknow length of string")
print(len(numbers))

'''

'''
fruits = ["apple", "banana", "cherry", "mango"]
numbers = [10, 20, 30, 40, 50, 60, 70]

# Q1: Access the first and last fruit in the list.
print(fruits[0])
print(fruits[-1])

# # Q2: Change "banana" to "orange".
fruits[1] = "orange"
print(fruits)

# Q3: Add "grape" at the end of the list.
fruits.append("grape")
print(fruits)

# Q4: Insert "kiwi" at position 2.
fruits.insert(2,"kiwi")
print(fruits)

# Q5: Remove "mango" from the list.
fruits.remove("mango")
print(fruits)

# Q6: Remove the element at index 3 and print it.
popped = fruits.pop(3)   # Removes by index
print(popped) 
print(fruits)

# Q7: Slice numbers to get [20, 30, 40].
print(numbers[1:4])

# Q8: Get every second number from the numbers list.
print(numbers[::2])

# Q9: Reverse the numbers list using slicing.
print(numbers[::-1])

# Q10: Sort the numbers list in ascending order, then reverse it.
# numbers.sort(reverse=True) decendig order 
numbers.sort()
print(numbers)
print(numbers[::-1])

'''