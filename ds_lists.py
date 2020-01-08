# Lists
## 1. Lists are ordered.
## 2. Lists can contain any arbitrary objects.
## 3. List elements can be accessed by index.
## 4. Lists can be nested to arbitrary depth.
## 5. Lists are mutable
## 6. Lists are dynamic.

a = ['foo', 'bar', 'baz', 'qux']
print(a)

## 2. Lists can contain any arbitrary objects.
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
### Lists can even contain complex objects, like functions, classes, and modules
### No limit on the list size as long as memory is allowed.
### a given object can appear in a list multiple times

## 3. List elements can be accessed by index.
#####  0      1      2      3       4      5
#####  -6    -5      -4     -3     -2      -1
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
### slice
print(a[0:6:2]) ##['foo', 'baz', 'quux']
print(a[6:0:-2]) ## ['corge', 'qux', 'bar']
a=[1,2,7,8]
## How to make [1, 2, 3, 4, 5, 6, 7, 8]
a[2:2] = [3,4,5,6]
print(a)

## reverse order
print(a[::-1])

## in and not in operators
print('qux' in a) ## True
print('thud' not in a) ## True

## concatenate (+) and replication (*) operators:
print(a + ['grault', 'garply']) ## ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
print( a * 2) ## ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'foo', 'bar', 'baz','qux', 'quux', 'corge']

len(a) ## 6
min(a) ## bar
max(a) ## qux


## 4. Lists can be nested to arbitrary depth.
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

## 5. Lists are mutable
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a) ## ['foo', 1.1, 2.2, 3.3, 4.4, 5.5, 'quux', 'corge']

a = [1, 2, 3]
a[1:2] = [2.1, 2.2, 2.3]
print(a) ## [1, 2.1, 2.2, 2.3, 3]

a = [1, 2, 3]
a[1] = [2.1, 2.2, 2.3]
print(a) ##[1, [2.1, 2.2, 2.3], 3]

###Prepending or Appending Items to a List
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a += ['grault', 'garply'] ## ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
a = [10, 20] + a ## [10, 20, 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']

### Methods That Modify a List
### list methods modify the target list in place. They do not return a new list:
s = 'foobar'
s.upper() ##FOOBAR

a=['a', 'b']
a.append(123) ## O(1)
## Appends an object to a list.
## ['a', 'b', 123]
a.extend([1,2,3])  ## O(k) k is the value of a parameter or # of parameter in the list
## Extends a list with the objects from an iterable.
## ['a', 'b',123, 1, 2, 3]
a.insert(3,3.141592) ## O(n)
## (<index>, <obj>) inserts object <obj> into list a at the specified <index>
## ['a', 'b',123, 1, 2, 3]
a.index('bar') ## O(1)
## provides you index number of the item
a.remove(3.141592) ## O(1)
## Removes an object from a list.
a.pop() ## O(1)
##Removes an element from a list. index is optional parameter.
## remove() does not retrun the item value, while pop() returns the value to be deleted
## For remove(), you need to enter the value of Object vs. Pop() you will need index
a.sort() ## O(nlogn)
a.reverse() ## O(nlogN)
a.len() ## O(1)

del a[0]