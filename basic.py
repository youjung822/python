## Important link
### https://realpython.com/python-data-types/

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

# Integer
## No limit on the size
## 0B Binary(2), 0o Octal(8), 0x Hexa(16)
print(0o10) ## 8
print(0x10) ## 16

# Floating point numbers
## link to read about Floating points
## https://docs.python.org/3.6/tutorial/floatingpoint.html
number = 1.1
type(4.2) ## <class 'float'>

# Complex Numbers
## Complex numbers are specified as <real part>+<imaginary part>j

# String
## sequences of character data
## size can be as many characters as you wish
string = "Strings can be declared with single or double quotes."
## using single of double quotes within the string, use the other quote.
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')
## escape sequence
### \' literal single quote
### \" literal double quote
### \newline literal new line
### \\ literal backslash

# Boolean
boolean = True

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
Built in functions
"""
# Math
## 1. abs()  returns an absolute value
number1 = -24
print("Absolute value: "+str(abs(number1)))
## 2. divmod()	Returns quotient and remainder of integer division
x,y=divmod(8,3) ## x is quotient and y is remainder
## 3. max()	Returns the largest of the given arguments or items in an iterable
## 4. min()	Returns the smallest of the given arguments or items in an iterable
## 5. pow()	Raises a number to a power
x = pow(4, 3) ## 4*4*4
x = pow(4, 3, 5) ## (4*4*4)%5
## 6. round()	Rounds a floating-point value
## 6-1. math.floor(4.78) drop ### returns 4
## 6-1. math.ceil(4.39) ceiling ### returns 4
## 7. sum()	Sums the items of an iterable

# Type conversion
## 1. ascii()	Returns a string containing a printable representation of an object
## 2. bin()	Converts an integer to a binary string
bin(5) ## 0b101
print("bin() returns a binary value of integer: "+ str(bin(number1)))
# If prefix /"0b/" is desired or not, you can use either of the following ways.
print("Integer format to binary: "+format(14, '#b'))
print("Integer format to binary wo 0b characters: "+format(14, 'b'))
## 3. bool() Converts an argument to a Boolean value
### below considered "False"
### constants defined to be false: None and False.
### zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
### empty sequences and collections: '', (), [], {}, set(), range(0)
test = []
print(test,'is',bool(test)) # False
test = [0]
print(test,'is',bool(test)) # True
test = 0.0
print(test,'is',bool(test)) # False
test =-209.98
print(test,'is',bool(test)) # False
test = None
print(test,'is',bool(test)) #False
test = True
print(test,'is',bool(test)) #True
test = 'Easy string'
print(test,'is',bool(test)) # True
## 4. chr()	Returns string representation of character given by integer argument
## 5. complex()	Returns a complex number constructed from arguments
## 6. float()	Returns a floating-point object constructed from a number or string
## 7. hex()	Converts an integer to a hexadecimal string
## 8. int()	Returns an integer object constructed from a number or string
## 9. oct()	Converts an integer to an octal string
## 10. ord()	Returns integer representation of a character
## 11. repr()	Returns a string containing a printable representation of an object
## 12. str()	Returns a string version of an object
## 13. type()	Returns the type of an object or creates a new type object

# Iterables and Iterators
## 1. all()	Returns True if all elements of an iterable are true
## 2. any()	Returns True if any elements of an iterable are true
## 3. enumerate()	Returns a list of tuples containing indices and values from an iterable
l1 = ["eat","sleep","repeat"]
obj1 = enumerate(l1)
print(list(enumerate(l1))) ## [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
s1 = "geek"
obj2 = enumerate(s1)
# changing start index to 2 from 0
print list(enumerate(s1,2))  ## [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
## 4. filter()	Filters elements from an iterable
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list) ## [5, 7, 97, 77, 23, 73, 61]

## 5. iter()	Returns an iterator object
## 6. len()	Returns the length of an object
## 7. map()	Applies a function to every item of an iterable
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list) ## [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

## 8. next()	Retrieves the next item from an iterator
## 9. range()	Generates a range of integer values
## 10. reversed()	Returns a reverse iterator
## 11. slice()	Returns a slice object
## 12. sorted()	Returns a sorted list from an iterable
## 13. zip()	Creates an iterator that aggregates elements from iterables

# Composite Data Type
## 1. bytearray()	Creates and returns an object of the bytearray class
## 2. bytes()	Creates and returns a bytes object (similar to bytearray, but immutable)
## 3. dict()	Creates a dict object
## 4. frozenset()	Creates a frozenset object
## 5. list()	Constructs a list object
## 6. object()	Returns a new featureless object
## 7. set()	Creates a set object
## 8. tuple()	Creates a tuple object

# Classes, Attributes, and Inheritance
## 1. classmethod()	Returns a class method for a function
## 2. delattr()	Deletes an attribute from an object
## 3. getattr()	Returns the value of a named attribute of an object
## 4. hasattr()	Returns True if an object has a given attribute
## 5. isinstance()	Determines whether an object is an instance of a given class
## 6. issubclass()	Determines whether a class is a subclass of a given class
## 7. property()	Returns a property value of a class
## 8. setattr()	Sets the value of a named attribute of an object
## 9. super()	Returns a proxy object that delegates method calls to a parent or sibling class

# Input/Output
## 1. format()	Converts a value to a formatted representation
## 2. input()	Reads input from the console
## 3. open()	Opens a file and returns a file object
## 4. print()	Prints to a text stream or the console

# Variables, References, and Scope
## 1. dir()	Returns a list of names in current local scope or a list of object attributes
## 2. globals()	Returns a dictionary representing the current global symbol table
## 3. id()	Returns the identity of an object
## 4. locals()	Updates and returns a dictionary representing current local symbol table
## 5. vars()	Returns __dict__ attribute for a module, class, or object

# Miscellaneous
## 1. callable()	Returns True if object appears callable
## 2. compile()	Compiles source into a code or AST object
## 3. eval()	Evaluates a Python expression
## 4. exec()	Implements dynamic execution of Python code
## 5. hash()	Returns the hash value of an object
## 6. help()	Invokes the built-in help system
## 7. memoryview()	Returns a memory view object
## 8. staticmethod()	Returns a static method for a function
## 9. __import__()	Invoked by the import statement

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