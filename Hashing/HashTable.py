'''
A hash table is data structure where elements are accessed by keyword rather 
than an index number, unlike in lists and arrays. In this data structure, the data 
items are stored as key/value pairs similar to dictionaries.
A hash table uses a hashing function in prder to find an index position
where an element should be stored and retrieved. This gives us fast
lookups since we are using an index number that corresponds to the hash 
value of the key.

Each position in the hash table is often called a slot or bucket and can 
store an element. So, each data item in the form of (key, value) pairs would
be stored in the hash table at a position that is decided by the hash value 
of the data.

To implement the hash table, we start by creating a class to hold hash table 
items. These need to have a key and a value since hash table is 
a {key, value} store.
'''

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '{'+str(self.key)+' : '+str(self.value)+'}'

'''
This gives us a very simple way to store items. Next we strat working 
on the hash table class itself.

'''

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        