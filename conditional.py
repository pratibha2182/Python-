'''
# if statement 
x = 15;
if (x < 10):
    print("x is greater than 5")
'''


'''
# if..else statement
x = 5;
if (x > 10):
    print("x is greater than 10")
else:
    print("Not")
'''


'''
# if..elif..else
marks = 85
if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
else:
    print("C grade")
'''


'''
# nested if
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

'''


# Q1: Take a number from the user. 
#     If it is positive, print "Positive".
#     If it is negative, print "Negative".
#     If it is zero, print "Zero".
'''
num = int(input("Enter a number: "))
if (num > 0):
    print("Positive number")
elif (num < 0):
    print("Negetive number")
else:
    print("Zero")
'''


# Q2: Ask the user for their age.
#     If age >= 18, print "You can vote".
#     Else, print "You cannot vote".
'''
age = int(input("Enter your age: "))
if (age >= 18):
    print("You can vote.")
else:
    print("You can't vote")
'''


# Q3: Take a number as input and check:
#     - If divisible by 3, print "Fizz"
#     - If divisible by 5, print "Buzz"
#     - If divisible by both, print "FizzBuzz"
#     - Else, print the number itself.
'''
num = int(input("Enter a number: "))
if (num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
elif (num % 5 == 0):
    print("Buzz")
elif (num % 3 == 0):
    print("Fizz")
else:
    print("Not divisible by 5 or 3 ")
'''


# Q4: Ask the user for marks.
#     - >=90 → "A grade"
#     - >=75 → "B grade"
#     - >=50 → "C grade"
#     - Else → "Fail"
'''
marks = int(input("Enter marks"))
if (marks >= 90):
    print("A")
elif (marks >= 75):
    print("B")
elif (marks >= 50):
    print("C")
else:
    print("Fail")
'''


# Q5: Nested if:
#     Ask for a number.
#     If it is even, check if it is also greater than 10.
#         If yes, print "Even and >10"
#         Else, print "Even and <=10"
#     Else, print "Odd number"
'''
num = int(input("Enter a number: "))
if (num % 2 == 0):
    if (num > 10):
        print("Even and > 10")
    else:
        print("Even and < 10")
else:
    print("Odd")
'''


# Q6: Write a program to check whether a given year is a leap year.
#     (Leap year if divisible by 4, not divisible by 100 unless divisible by 400)
'''
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''


# Q7: You have three numbers. Print the largest one.
'''
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))
if (num1 > num2 and num1 > num3):
    print(f"{num1} is greater then {num2} and {num3}")
elif (num2 > num1 and num2 > num3):
    print(f"{num2} is greater then {num1} and {num3}")
else:
    print(f"{num3} is greater then {num1} and {num2}")
'''


# Q8: Take a character as input. Check if it’s a vowel or consonant.
'''
letter = str(input("Enter a letter: "))
if len(letter) == 1 and letter.isalpha():
    if letter in ['a','e','i','o','u']:
        print("Vowel")
    else:
        print("consonant")
else:
    print("Enter only single digit letter.")
'''


# Q9: Password Strength Checker
'''
password = input("Enter Password: ")
if (len(password) > 8 and any(ch.isdigit() for ch in password) 
    and any(ch in "#$@!%&*" for ch in password)):
    print("Strong Password")
else:
    print("Weak Password")
'''


# Q10: Discount Calculator
'''
amount = float(input("Enter amount: "))
if amount > 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
final_price = amount - discount
print(f"Final amount is: {final_price}")
'''

# Q11: Grade + Attendance
marks = float(input("Enter marks: "))
attendence = float(input("Enter your present attdence: "))
if attendence < 75:
    print("Low attdence! Improve you attendence")
elif (marks >= 90):
    print("A")
elif (marks >= 75):
    print("B")
elif (marks >= 50):
    print("C")
else:
    print("Fail")


# Q12: ATM Withdrawal


# Q13: Triangle Type Checker


# Q14: Login System


# Q15: Number to Words
