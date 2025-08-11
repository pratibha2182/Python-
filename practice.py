'''
Q1: Greeting the User
Ask the user for their name and age, then print:

a = str(input("Enter your name: "))
b = int(input("Enter your age: "))
print(f"Hello, my name is {a} and i am {b} years old.")
'''

'''
Q2: Circle Area Calculator
Ask the user for the radius of a circle and print its area using the formula:
Area = 𝜋𝑟^2
(Use π = 3.1416)

 
pi = 3.1416
r = float(input("Enter a radius: "))
area = pi *( r * r)
print("Area of circle is: " , area)
'''

'''
Q3: Simple Interest Calculator
Ask the user for Principal, Rate of Interest, and Time in years, then calculate Simple Interest:

p = int(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter years: "))
si = p * r * t / 100
print("Simple instrest is: " , si)
'''

'''
Q4: Temperature Converter
Take temperature in Celsius from the user and convert it to Fahrenheit:

c = float(input("Enter temperature in celsius: "))
f = 9/5 * c + 32
print("Fahrenheit: " ,f)
'''

'''
Q5: Swap Two Numbers
Ask the user for two numbers and swap their values without using a third variable.

a = int(input("A: "))
b = int(input("B: "))
print("Method a")
c = a #will store a in c and get a empty
a = b # store b in a and b get empty
b = c # store c in b and get c empty  
print("A: ", a)
print("B: ", b)

print("Method 2")
a , b = b , a
print("A: ", a)
print("B: ", b)
'''

'''
Q6: Remainder Finder
Take two integers from the user and print the remainder when the first number is divided by the second.
'''
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = a % b
print("Remainer while dividing A with B is: " , c)