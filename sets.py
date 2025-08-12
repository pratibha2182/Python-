'''
A set in Python is:

An unordered collection of items (no index).

Mutable (you can add/remove items).

No duplicate values allowed.
'''

'''
# creating sets
fruits = {"apple", "banana","cherry"}
numbers = set([1, 2, 3, 4, 5])
empty = {} #dict
empty1 = set()
print(type(fruits))
print(type(numbers))
print(type(empty))
print(type(empty1))
'''

'''
# remove duplicate
data = {1,2,3,4,5,3,2,1}
print(data)  #will automatically remove duplicate number or data 
'''

'''
# adding or removing data
mySet = {1 ,2, 3, 4}
mySet.add(5)  #for single addition
print(mySet)

mySet.remove(3) # for single removale error will be there if not fount
print(mySet)

mySet.discard(9) # for single removale no error will be there if not fount
print(mySet)

mySet.update([6, 7, 8]) # for multiple addition
print(mySet)
'''

'''
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

# union will do or operation will give all element ignoring dulicate
print(a.union(b))

# intersection will do and operation will give only the same element
print(a.intersection(b))

# difference will a - b 
print(a.difference(b))
print(b.difference(a))

# symmetric difference will remove same elemt from both and give output
print(a.symmetric_difference(b))
'''


'''
# membersip in or not in
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # True
print("cherry" not in fruits)  # True
'''

'''
# frozen set
fs = frozenset([1, 2, 3])
# fs.add(4)   # AttributeError: 'frozenset' object has no attribute 'add'
'''


'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Q1: Add 9 to set A.
A.add(9)
print(A)

# Q2: Add multiple elements 10 and 11 to set A.
A.update([10, 11])
print(A)

# Q3: Remove 3 from set A.
A.remove(3)
print(A)

# Q4: Remove 20 from set A without causing an error.
A.discard(20)
print(A)

# Q5: Find the union of A and B.
print(A.union(B))

# Q6: Find the intersection of A and B.
print(A.intersection(B))

# Q7: Find the elements that are in A but not in B.
print(A.difference(B))

# Q8: Find the symmetric difference between A and B.
print(B.symmetric_difference(A))

# Q9: Check if 5 is present in set B.
print(5 in B)

# Q10: Convert list [1, 2, 2, 3, 3, 3] into a set and print it.
lst = [1, 2, 2, 3, 3, 3]
s = set(lst)
print(s)
'''
