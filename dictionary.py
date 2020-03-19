d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6
}
print(d)
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