
'''
local variable is that variable which id define wihin a function and is only accessible within that function it is created when function is call and destroy when function return value

Global varibale is a varible that is defined ouside the function and can be accessible within any function and outside the function to in the whole program  
'''

x = 10 #global
print(x)
def myFunc():
    global x
    x = 3 # will change the x value in the function
    y = 5 #local
    print(y) 
    print(x)
    print("x will run as it is a global variable which is changed")
myFunc()
print (x)
# print(y)
# NameError: name 'y' is not defined
#will give error as y is inside the function