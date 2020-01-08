#Dictionary
## Indexed by keys(Any immutable type/Hashable type)
## Hashable  : integer, float, string, boolean, tuple
## If you store using a key that is already in use, the old value associated with that key is forgotten.
## When you assign a value to an already existing dictionary key,it replaces the existing value.

## Important Link
# https://realpython.com/python-dicts/
# https://realpython.com/iterate-through-dictionary-python/

##create a dictionary
tel = {'jack': 4089, 'sape': 4139}
tel['guido']= 4127
print(tel)

MLB_team = {
'Colorado' : 'Rockies',
'Boston'   : 'Red Sox',
'Minnesota': 'Twins',
'Milwaukee': 'Brewers',
'Seattle'  : 'Mariners'
}

MLB_team = dict([
('Colorado', 'Rockies'),
('Boston', 'Red Sox')])

MLB_team = dict(Minnesota='Twins',Milwaukee='Brewers')
MLB_team['Seattle'] = 'Seahawks'
MLB_team['Kansas City'] = 'Royals'

##delete an item
del tel['jack']
print(tel)

## returns only keys or values
tel.keys()
tel.values()

## dict() constructor
print(dict([('youjung',2213),('min',2425),('eli',5599)]))
# returns {'sape': 4139, 'jack': 4098, 'guido': 4127}
dict(sape=4139, guido=4127, jack=4098)
# returns {'sape': 4139, 'jack': 4098, 'guido': 4127}

## dict comprehensions
## can be used to create dictionaries from arbitrary key and value expressions:
print({x:x**2 for x in (2,4,6)})
# returns {2: 4, 4: 16, 6: 36}

# Building a Dictionary Incrementally
person = {}
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
## {'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna',
##'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}
print(person['children'][-1]) ## 'Joey'
print(person['pets']['cat']) ## Sox

# Operators and Built-in Functions
print('Milwaukee' in MLB_team)
print('Toronto' not in MLB_team)
print(len(MLB_team))

# Built-in Dictionary Methods
d = {'a': 10, 'b': 20, 'c': 30}
d.clear() ## Clears a dictionary.
## d.get(<key>[, <default>]):  Returns the value for a key if it exists in the dictionary.
## If <key> is not found and the optional <default> argument is specified,
## that value is returned instead of None
print(d.get('z', -1)) ## returns -1

## d.items():
list(d.items()) ## Returns a list of key-value pairs in a dictionary. ## [('a', 10), ('b', 20), ('c', 30)]
list(d.keys()) ## Returns a list of keys in a dictionary. ## ['a', 'b', 'c']
list(d.values()) ##Returns a list of values in a dictionary. ## [10, 20, 30]

## !!!!  The .items(), .keys(), and .values() methods actually return something called
# a view object. A dictionary view object is more or less like a window on the keys and
# values. !!!!

## d.pop(<key>[, <default>]) Removes a key from a dictionary, if it is present, and
# returns its value.
d = {'a': 10, 'b': 20, 'c': 30}
d.pop('b') ## returns 20

# If <key> is not in d, and the optional <default> argument is specified, then that
# value is returned, and no exception is raised:
d.pop('z', -1) ## returns -1

## d.popitem() Removes a random key-value pair from a dictionary.
print(d.popitem()) ## ('c', 30)

## d.update(<obj>) Merges a dictionary with another dictionary or with
# an iterable of key-value pairs.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1) ## {'a': 10, 'b': 200, 'c': 30, 'd': 400}
