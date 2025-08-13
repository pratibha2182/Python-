# for loop 
'''
for i in range(6):
    print(i)
'''


# while loop
'''
i = 1
while (i < 5):
    print(i)
    i += 1
'''

# break and continue 
'''
for i in range (5):
    if i == 4:
        break
    print(i)
'''
'''
for i in range (6):
    if i == 3:
        continue
    print(i)
'''

# loop with else
'''
for i in range(1,10):
    if (i % 2 == 0):
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
'''


# Q1: Print numbers from 1 to 10 using a for loop.
'''
for i in range (1,11):
    print(i)
    i += 1
'''


# Q2: Print the multiplication table of a given number (e.g., 5 × 1 to 5 × 10).
'''
num = int(input("Enter a number:"))
for i in range (1,11):
    m = num * i 
    print(f"{num} X {i} = {m}")
    i += 1
'''


# Q3: Print all even numbers from 1 to 50.
# num = int(input("Enter a number:"))
'''
for i in range(1,51):
    if(i % 2 == 0):
        print(i)
        i += 1
'''


# Q4: Calculate the sum of first 10 natural numbers.
'''
sum = 0
for i in range (1,11):
    sum += i
    print(sum)
print(f"Sum of first 10 natural number is:{sum}")
'''


# Q5: Reverse a given string using a loop.
'''

word = input("Enter string:")
rev = ""
for ch in word:
    rev = ch + rev
    print(rev)
print(rev)
'''


# Q6: Count the number of vowels in a string.
'''

word = input("Enter string:").lower()
vowel = "aeiou"
count = 0
for ch in word: # check for all ch in words
    if ch in vowel:  # check if vowels are avaible in ch and count it 
        count += 1 # increse count by checking all ch in words
print(count)
'''


# Q7: Find the factorial of a given number.

# Q8: Print a pattern like:
# *
# **
# ***
# ****
# *****

# Q9: Print the Fibonacci series up to N terms.

# Q10: Find the sum of all numbers divisible by 3 or 5 below 100.

# Q11: Given a list of numbers, print only the prime numbers.

# Q12: Given a string, count how many times each character appears (without using Counter).

# Q13: Write a program to check if a number is an Armstrong number.

# Q14: Create a pyramid pattern of numbers:
# 1
# 12
# 123
# 1234
# 12345

# Q15: Print all pairs (i, j) such that i + j = 10, where i and j are between 1 and 10.
