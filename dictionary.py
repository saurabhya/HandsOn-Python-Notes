# Initializing a dctionary, we can do so by just using {}, the syntax for defining a dictionary.
# There are other methods too such as declaring a variable as a dictionary and then adding items to the dictionary.
d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6
}
print(d)

# dict.__getitem__
print(d.__getitem__)
# dict.items()
print(d.items())
# dict.values()
print(d.values())

# Printing the sorted verison of the dictionary, sorting on the basis of dict.__getitem__
print(sorted(list(d), key=d.__getitem__))

d2 = {
    'one': 'uno',
    'two': 'deux',
    'three': 'trois',
    'four': 'quatre',
    'five': 'cinq',
    'six': 'six'
}
print(sorted(d2, key=d.__getitem__))
print([d2[i] for i in sorted(d2, key=d.__getitem__)])

# We can of course define our own custom method that we canuse in key argument

def corder(a):
    return a[len(a)-1]

print(sorted(d2.values(), key=corder))