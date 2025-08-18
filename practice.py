'''
# Write a Python program to print "Hello, World!".
print("Hello, World")

# Create variables for your name, age, and city and print them in one line.
name = "Pratibha Singh"
age = 22
city = "Valsad, Gujarat" 
print(f"My name is {name}. I am {age} years old, and live in {city}.")

# What is the difference between = and == in Python?
print("= is only for checking that 2 number or varible looks same or not. And == will check the look and data type both.")

# Predict the output:
x = 5
y = 2
print(x**y)
print(x//y)

# Take input from user for their favourite color and print "Your favorite color is <color>".
color = input("Enter favourite color:")
print(f"Your favourite color is {color}")

# Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negetive")
else:
    print("Zero")

# WAP to check whether a given year is a leap year or not.
year = int(input("Enter a number: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not A Leap Year")

# Write a program to accept marks of a student and print the grade:
marks = int(input("Enter a number: "))
if marks >= 90:
    print("A")
elif marks > 70:
    print("B")
elif marks > 50:
    print("C")
else:
    print("Fail")

# Write a program to print numbers from 1 to 10 using a loop.
for i  in range (1, 11):
    print(f"number: {i}")

# Print the multiplication table of a number entered by the user.
num = int(input("Enter a number: "))
for i  in range (1, 11):        
    print(f"{num} X {i} = {num * i}")

# Print all even numbers between 1 to 50.
for i in range (1,51):
    if i % 2 == 0:
        print(i)

# Find the sum of digits of a given number (e.g., 123 → 6).
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10 # take digit which will contain remainder or last digit
    sum += digit # will add digit to last sum 
    num //= 10  # will remove last digit from the num and again will do the same do same again till get 0
print(sum)


# Print the factorial of a given number using a loop.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(fact)


# WAP to check whether a number is prime or not.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Print this pattern (for n=5):
# *
# **
# ***
# ****
# *****
num = int(input("Enter a number: "))
for i in range (1, num + 1):
    for j in range (i):
        print("8",end="")
    print()


# Reverse a string without using slicing ([::-1]).
s = input("name: ")
rev= " "
rev = " ".join(reversed(s))
print("1: ",rev)

rev1 =" "
for char in s:
    rev1 = char + rev1
print("2: " ,rev1)

rev2 = " "
i = len(s) - 1
while i >= 0:
    rev2 += s[i]
    i -= 1
print("3: ", rev2)

# Count the number of vowels in a string.
st = input("String: ")
vowel = "AEIOUaeiou"
count = 0
for char in st:
    if char in vowel:
        count += 1
print("Count is: ", count )
'''

# Check if a string is a palindrome (e.g., "madam").
pali = input("String: ")
rev = ""
for char in pali:
    rev = char + rev
print(rev)
if rev != pali:
    print("It is not palindrome")
else:
    print("It is palindrome")

# Write a program to count words in a sentence.

# WAP to replace all spaces in a string with -.

# 🔹 Lists
# Create a list of 5 numbers. Print the maximum and minimum.

# WAP to find the sum of elements in a list.

# Remove duplicates from a list.

# Write a program to sort a list without using sort() function.

# WAP to print only even elements from a list.

# 🔹 Functions
# Write a function to print "Welcome to Python!".

# Write a function that accepts two numbers and returns their sum.

# Write a function to find the factorial of a number.

# Write a function to check if a number is prime.

# Write a function to return the reverse of a string.

# Write a function that accepts a list and returns the largest element.

# WAP to create a function that checks whether a number is Armstrong (153 → 1³+5³+3³ = 153).

# Write a function to calculate the Fibonacci series up to n terms.

