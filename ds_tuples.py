#Tuples
## 1. Immutable
## Pretty much the same as list except..
### 1) Program execution is faster when manipulating a tuple
### than it is for the equivalent list. (This is probably not going
### to be noticeable when the list or tuple is small.)
### 2) Sometimes you don’t want data to be modified. If the values
### in the collection are meant to remain constant for the life
### of the program, using a tuple instead of a list guards against accidental modification.
### 3) There is another Python data type that you will encounter shortly called
### a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.

'''
Definition
'''
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

## When you create a tuple with one item,
t = (2)
print(type(t)) ## int type

t = (2,)## This is right way to initiate singleton tuple
print(type(t))  ##<class 'tuple'>

##Packing and unpacking
t = 1, 2, 3
print(t) ## (1, 2, 3)
x1, x2, x3 = t
print(x1, x2, x3) ## (1, 2, 3)

## Tuples may be nested
u= t,(1,2,3,4,5)
print(u)

##Swapping values
a = 'foo'
b = 'bar'
a, b = b, a
print(a, b) ## ('bar', 'foo')
## Tuples are immutable
# t[0]= 8989
## TypeError: 'tuple' object does not support item assignment

#But they can hold mutable objects
v=([1,2,3],[3,2,1])
print(v)