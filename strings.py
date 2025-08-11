'''
A string in Python is a sequence of characters enclosed in single quotes ', double quotes ", or triple quotes.

Strings can contain letters, numbers, symbols, and even spaces.

Triple quotes are used for multi-line text or docstrings.
'''

'''
String indexing
 0  1  2  3  4  positive indexing
 H  E  L  L  O
-5 -4 -3 -2 -1 negetive indexing


print("String indexing")
word = "HelloWorld"
print(word[0]) # will give h as it is in 0 index at start
print(word[-1]) # will give d as it is in -1 index at end
'''


'''
String slicing
string[start:end:step]

start → index where slicing begins (inclusive)
end → index where slicing stops (exclusive)
step → how many characters to skip (default = 1)

Slice	Meaning
s[start:end] = From start to end-1
s[:end] = From beginning to end-1
s[start:] = From start to end of string
s[start:end:step] = From start to end-1, skipping step
s[::-1] = Reverse string

'''

# text = "Hello World"

'''
 0   1   2  3  4  5  6  7  8  9  10  positive indexing
 H   E   L  L  O  _  W  O  R  L  D
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 negetive indexing

print(text[0:5])   # (0 to 4)
print(text[6:11])  # (6 to 10)
print(text[:5])    # (start to 4)
print(text[6:])    # (6 to end)
print(text[::2])   #(run with giving step 2)
print(text[1::2])  #(start from 1 and skip every 1)
print(text[::-1])  #(start from last and count very 1 from back also used for reverse string)
print(text[::-2])  #(start from last and skip 1)
print(text[-5:])   
print(text[-11: -6])
print(text[0:20])  #it will not give out of bound error it will take what ever is avalible
'''

'''
letter = "Pythonprogramming"

Q1: Extract "Python" using slicing.
print(letter[0:6])


Q2: Extract "Programming" using slicing.
print(letter[6:])

Q3: Extract "thon" from the string.
print(letter[2:6])

Q4: Extract "gram" from "Programming".
print(letter[9:13])

Q5: Get the last 5 characters of the string.
print(letter[-5:])

Q6: Get every 2nd character from "PythonProgramming".
print(letter[::2])

Q7: Reverse the whole string using slicing.
print(letter[::-1])

Q8: Reverse only "Programming" part of the string (keep "Python" same).
print(letter[0:6] + letter[6:][::-1])
Pythongnimmargorp
print(letter[0:6][::-1] + letter[6:])
nohtyPprogramming
0-6 python and [6:] programing and [6:][::-1] reverse programing


Q9: Extract "Pto rgamn" (skip every alternate character).
print(letter[::2])

Q10: From "PythonProgramming", extract "gnimmargorP" (reverse only last part).
print(letter[0:6] + letter[6:][::-1])
'''

'''
# String Concatenation and repetition
a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
print(a * 3)         # HelloHelloHello
'''

'''
# string built in method
sentence  = "Hello everyone my name is pratibha"

# .upper
print(sentence.upper())

# .lower
print(sentence.lower())

# .title
print(sentence.title())

# .strip
print(sentence.strip())

# .replace(a,b)
print(sentence.replace("A", "a"))

# .split
print(sentence.split())

# .join
word = sentence.split()
result = " ".join(word)
print(word)
print(result)
'''


'''
# Escape character
\n = new line
\t tab space
"\"Hi\"" quote inside string

print("Hello\nWorld") 
print("Hello\tWorld")  
print("He said \"Hi\"") 

'''

'''
f-string (formatted sting)

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
'''

'''
String immutable
Immutable objects cannot be altered in place.
If you try to change them, Python will create a new string in memory instead of modifying the original.
# text ="Hello"
# text[0] = "y"  
# TypeError: 'str' object does not support item assignment

correctway
text = "Hello"
new_text = "Y" + text[1:]
#  text[1:] takes "ello", then "Y" is added to the front → "Yello".
print(new_text)  # Yello

a = "hello"
b = a
#here we have give a value to b and made b empty
a = "Hi"
print(a)
print(b)
'''





# tupple and list