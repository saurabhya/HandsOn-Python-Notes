s1 = {'ab',3,4,(5,6)}
s2 = {'ab',7,(7,6)}
print(s1-s2) # sets allows '-' operation
# Intersection as weel as union is also allowed for sets
print(s1.intersection(s2))
print(s1.union(s2))