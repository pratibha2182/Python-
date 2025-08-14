'''
execption handlimg is process of responding to unwanted or unexepted event occure when the code is run by the computer. this deals with these event to avoid the program or system crashing without this process execption would disrupt the normal operation of a program


a = input("enter a number: ")
print(f"Table of {a}")
for i in range (1, 11):
    print(f"{int(a)} X {int(i)} = {int(a*i)}")
    #ValueError: invalid literal for int() with base 10: 'hello' 
    # if we use the string insted of integer and will not run the last print also
print("end of program")


# to avoid this error  try and except i use in the code 
a = input("enter a number: ")
print(f"Table of {a}")
try:
    for i in range (1, 11):
        print(f"{int(a)} X {int(i)} = {int(a*i)}")
except:
    print("Give only integer numbers not string")
print("end of program")

# output:
# enter a number: pu
# Table of pu
# Give only integer numbers not string
# end of program

'''



'''
finally clause
block is also a part of execption handling, when we handle execption using the try and except block, we can include a finaaly block at the end of the code. finally is alway executed so it is generally used for doing concluding task like closing fule resources or database 
finally will mostly work in the function which returns a value

def func():
    try:
        l = [1,2,4,6,5]
        i = int(input("index: "))
        print(l[i])
        return 1
    except:
        print("Error")
        return 0
    finally:
        print("I will always execute")  # will run every time 
        # print("I will always execute")will not run anytime 

x = func()
print(x)
'''
