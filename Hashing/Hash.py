'''
Hashing is aconcept in which, when we give data of an arbitrary size to a function, 
we get a small simplified value. This function is called a hash function. hashing uses 
a hash function that maps the given data to another range of data, so that a new range
of data can be used as an index in the hash table. More specifically, we will use 
hashing to convert strings into intergers. 
'''
def tryHash(s):
    hv = 0
    for ch in s:
        hv += ord(ch)
    return hv


for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, tryHash(item)))

print("\n")

'''
A perfect hashing function is the one by which we get a unique hash value for a given
string(it can be any data type). In practice, most of the hashing functions are imperfect
and face collisions. This ,eans that a hash function gives the same hash value to more than
one string; that is undesirable because a perfect hash function should return a unique hash 
value to a string. Normally, hashing functions need to be very fast, so trying to create a 
function that gives us a unique hash value for each string is normally nott possible.
Hence, we accept this fact and we know that we may get some collisions, that is , two
or more strings may have the same hash value. therefore, we try to find a strategy to 
resolve the collisions rather trying to find a perfect hashing function.  

For example:

'''

def myHash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv

for item in ('hello world', 'world hello', 'gello xorld'):
    print("{}: {}".format(item, myHash(item)))

'''
We can see that, this time, we get different hash values for these three strings.
Still, this is not a perfect hash. 
Let's try the strings, ad and ga
'''
for item in ('ad', 'ga'):
    print("{}: {}".format(item, myHash(item)))
'''
We still get the same hash values for two differernt strings. therefore, we need to 
devise a strategy for resolving such collisions.
'''