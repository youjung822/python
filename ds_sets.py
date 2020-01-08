# A set is
## an unordered collection with
## no duplicate elements.
## Set objects also support mathematical operations
## like union, intersection, difference, and symmetric difference.

### Important link!!
# https://realpython.com/python-sets/#modifying-a-set

#Create a set
basket = ['apple','orange','apple','pear','orange','banana']
fruit = set(basket)
print(fruit)

# in - to see an item is in the set O(1)
print('oragne' in fruit)  #True
print('crabgrass' in fruit) #False

a = set('abracadabra')
b = set('alacazam')
print(a) #set(['a', 'r', 'b', 'c', 'd'])
print(b) #set(['a,l,c, z, m'])

## Mathematical operations
print(a-b) ## letters in a but not in b
# result : set(['r', 'd', 'b'])
print(a|b) ## letters in either a or b
# result : set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
print(a & b) ##letters in both a and b
# result : set(['a', 'c'])
print(a ^ b) ##letters in a or b but not both
# result: set(['r', 'd', 'b', 'm', 'z', 'l'])

a={x for x in 'adracadabra' if x not in 'abc'}
print(a) ## set(['r', 'd'])

# Modify a set by union.
# Meaning add to x1 any elements in x2 that x1 does not already have:
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2
print(x1)
x1.update({'corge','graply'})
print(x1)

# Modify a set by intersection.
# meaning retaining only elements found in both x1 and x2:
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
print(x1) ##{'foo', 'baz'}
x1.intersection_update(['baz', 'qux']) ## {'baz'}
print(x1)

# Modify a set by difference.
# update x1, removing elements found in x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
print(x1) ##{'bar'}
x1.difference_update(['foo', 'bar', 'qux'])
print(x1) ## set()


# Modify a set by symmetric difference.
# update x1, retaining elements found in either x1 or x2, but not both:
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 ^= x2
print(x1) ## 'bar', 'qux'
x1.symmetric_difference_update({'qux','corge'})
print(x1) ##'bar','corge'

x1.add('qux')
x1.remove('foo') # remove the item
x1.discard('max') # The difference of discard() with remove() if <elem> is not in x, this method quietly does nothing instead of raising an exception
x1.pop() # randomly pop an item and remove the item from the set. Exception occur when no item to be pop/
x1.clear() # removes all items from x1

