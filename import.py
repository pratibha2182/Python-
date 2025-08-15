'''
import is a process of loading code from a pyhton modules into the current file and allow to use the function and variable define in the modules in you current script, as well as any aditional module that can imported

# simple method for importing
import math
result = math.sqrt(22)
print(result)


# from method
from math import sqrt, pi
print(sqrt(2))
print(pi)


# from with *
from math import * #(not prefered)
print(sqrt(16))


# as keyword
import math as m 
print(m.sqrt(16))
'''

# dir keyword
import math
print(dir(math))