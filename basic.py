import time

print("This program is to review the basic python code and started on " + time.ctime())

"""
Comments
"""
# This is a one-line Python comment - code blocks are so useful.
"""
This type of comment is used to document the purpose of functions and classes. 
"""


"""
Declaration/ Initialization
"""
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
print(answer)


"""
Data Types
"""
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None

print(boolean, "is of type", type(boolean))
print(number, "is of type", type(number))
print("\""+ string +"\"", "is of type", type(string))
print(list, "is of type", type(list))
print(tuple, "is of type", type(tuple))
print(dictionary, "is of type", type(dictionary))


"""
Simple Logging
"""
print("Printed!")


"""
Conditionals
"""
cake="cake"
if cake == "delicious":
    print("Conditionals: Yes please!")
elif cake == "okay":
    print("Conditionals: I'll have a small piece.")
else:
    print("Conditionals: No, thank you.")


"""
Loops
"""
for item in list:
    print("Loop for: "+ str(item))


number=10
total=0
values=[1,2,3,4,5,6,7,8,9,10,11,12,13]
i=0
while (total < number):
    total += values[i]
    i += 2
    print("Loop while: total %d, value %d" % (total, values[i]))



"""
Functions
"""
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print(q, r)


"""
Classes
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1