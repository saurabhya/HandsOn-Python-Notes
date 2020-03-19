'''
Counter is a subclass of a dictionary where each dictionary key is a hashable object and the associated value
is an integer count of that object. There are three ways to initialixe a counter.
We can pass it any sequence object, a sictionary of key:value pairs, or a tuple of format
(object=value, ....), as in the following example:
'''
from collections import Counter
c1 = Counter('anysequence')
c2 = Counter({'a':1, 'c':1, 'e':3})
c3 = Counter(a=1, c=1, e=3)
#print(c1)
#print(c2)
#print(c3)
'''
We can also create an empty counter object and populate it by passing its 
update method on iterable or a dictionary.
'''
ct = Counter()
print(ct)
ct.update('abca')
print(ct)
ct.update({'a':3})
print(ct)

for item in ct:
    print('%s: %d' %(item, ct[item]))

'''
The most notable difference bwtween counter objects and dictionaries is 
that counter objects return a zero count formissing items rather than 
raising a key error. 
'''
print(ct['x'])
ct.update({'a':-2, 'b':-2, 'e':-1})
print(ct)
print(sorted(ct.elements()))

'''
Two other Counter methods worth mentioning are most_common() and subtract().
'''
print(ct.most_common(1))
print(ct.most_common(2))

ct.subtract({'a':1})
print(ct)