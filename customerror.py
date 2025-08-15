'''
A custom error (also called a user-defined exception) is an error type you create yourself when the built-in exceptions don’t fully describe your specific problem.
You define it by creating a class that inherits from Exception (or another built-in exception) and then raising it when needed.

Why use custom errors?
Makes debugging easier with meaningful names.
Allows you to handle specific errors differently.
Keeps code clean instead of relying on generic ValueError or RuntimeError.

can make new error and can be use yiu shuold use class error name and code 


a = int(input("Enter value betwwen 1 to 5:"))
if (a>1  or a<5):
    raise ValueError("Value should be in between 1 to 5")

'''

class underAgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise underAgeError("You must be 18 year old to vote.")
    print("Granted")
except ValueError:
    print("enter vaild age.")
except underAgeError as e:
    print(f"Error {e}")
print("end")