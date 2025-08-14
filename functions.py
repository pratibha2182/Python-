'''
A function is a block of code that runs only when you call it.
It helps you:

Avoid repeating code

Make your program organized

Reuse logic

'''


'''
# defining and calling function
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function
'''

'''
# functions with parameteres
def greet_user(name):
    print(f"Hello {name}, welcome to Python!")
name = input("Enter a name: ")
greet_user(name)
'''

'''
# function with return values
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
'''

'''
# default parameteres
def greet(name="Guest"):
    print(f"Hello {name}")

greet()          # Hello Guest
greet("Pratibha") # Hello Pratibha
'''

'''
# multiple return values
def calc(a, b):
    return a+b, a-b, a*b

sum_, diff, prod = calc(10, 5)
print(sum_, diff, prod)
'''

'''
# funtions with loops
def even_numbers(limit):
    for i in range(2, limit+1, 2):
        print(i)

even_numbers(10)
'''

'''
# function inside functions
def outer():
    def inner():
        print("Inner function running")
    inner()
outer()
'''


'''
# Q1: Create a function that prints "Hello, Python!" every time it is called.
def greet():
    print("Hello, welcome to Python!")
greet() 
'''

'''
# Q2: Create a function that takes a name as a parameter and greets the user.
def greet_user(name):
    print(f"Hello {name}, welcome to Python!")
name = input("Enter a name: ")
greet_user(name)
'''

'''
# Q3: Write a function that adds two numbers and returns the result.
def add (a , b):
    return a + b
print(add(5, 7))
'''

'''
# Q4: Write a function that takes a number and returns True if it is even, False otherwise.
def number (num):
    if (num % 2 == 0):
        return("True")
    else: 
        return("False")

print(number(10))
print(number(1))
'''

'''
# Q5: Write a function that prints the multiplication table of a given number.
def table (num):
    for i in range(1,10+1):
        print(f"{num} X {i} = {num*i}")
print(table(2))
'''

'''
# Q6: Write a function that takes a list of numbers and returns the sum.
def sum (numbers):
    final = 0
    for abc in numbers:
        final += abc
    return final
print(sum([1,2,3,4,5,6,7,8,9,10]))
'''

'''

# Q7: Write a function that takes a list of numbers and returns the largest number.
def largeNum ( numbers):
    largeNum = numbers[0]
    for num in numbers:
        if num > largeNum:
            largeNum = num
    return largeNum
print(largeNum([2,4,6,7,98,6,5,]))
'''

'''
# Q8: Create a function that counts vowels in a given string.
def vowel(s):
    vowels = "AEIOUaeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(vowel("HELLO world"))
'''

'''
# Q9: Write a function that checks if a string is a palindrome (same forward & backward).
def palidorme(s):
    return s == s[::-1]
print(palidorme("NITIN"))
'''

'''
# Q10: Write a function that calculates the factorial of a given number.
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
print(factorial(5))
'''

'''
# Q11: Write a function that takes a list and returns a new list with unique elements only.
def uniqueList(lst):
    return(set(lst))
print(uniqueList([2,1,2,3,4,3,2,1]))
'''

'''
# Q12: Write a function that takes a list of integers and returns the second largest number.
def largestNumber(lst):
    uniqueNumber = list(set(lst))
    uniqueNumber.sort(reverse=True) #decending order
    if len(uniqueNumber) >= 2: # aleast 2 number should be there in a list 
        return uniqueNumber[1]
    else:
        return None
print(largestNumber([1,1,3,34,56,7,5,2]))
'''

'''
# Q13: Write a function that takes a string and returns a dictionary with character frequencies.
def frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char,0) + 1 
        #Looks up the current count of char in the dictionary.
        # If the character is not found, it returns 0 (default value).
        # + 1 → Adds 1 to the current count.
        # freq[char] = ... → Updates the dictionary with the new count.
    return freq
print(frequency("Hello")) 
'''

'''
# Q14: Write a function that generates a Fibonacci series of n terms.
def fibo(n):
    series = []
    a , b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print(fibo(7))
'''

# Q15: Create a function that takes marks as input and returns the grade:
#      >=90 → A, >=75 → B, >=50 → C, else → Fail
def grade(marks):
    if (marks >= 90):
        return("A")
    elif (marks >= 75):
        return("B")
    elif (marks >= 50):
        return("C")
    else:
        return("Fail")
marks = int(input("Enter your marks: "))
print(f"Your grades are {grade(marks)}")
