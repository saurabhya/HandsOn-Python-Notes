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

    '''
        The hash table uses a standard Python list to store its elements.
        Let's set the size of the hash table to 256 elements to start with.
        Later we will look at the strategies for how to grow thw hash table as we begin
        filling it up.
    '''
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv%self.size
    '''
        To store the elements in the hash table ,we will be using put() function.
        and retrieve them using get() function.
    '''

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        '''
            Once we kow the value of the key, It will be easy to dtore the elements at the key value.
            Hence, we need to find an empty slot we start at the slot that corresponds to the hash value of the key.
            If that slot is empty, we insert our item there.

            However, if the slot is not empty and the key of the item is not the same as our current key,
            then we have a collision.
            One way of resolving this kind of collision is to find slot from the position of the collision;
            this collision resolution process is called open addressing. We can do this by linearly looking
            for the next available slo by adding 1 to the preiou hash value where we get the collision.
            This systematic way of visiting each slot is a linear way of resolving collisions and is called
            Linear probing.
        '''
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1)%self.size

        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
    '''
        To retrieve values from the hash table , the value stored corresponding to the key would be returned.
        Here, we will see the implementation of the retrieval method - get()

        First we compute the hash value of the key then we look in the table for the key at computed hash value
        if key item matches the stored key value at that location, the corresponding value is retrieved.
        If that doesn't matches, we add 1 to the sum of the ordinal values of all the charcater
    '''
    def get(self, key):
        h = self._hash(key) # compute hash for the given key
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+1)% self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)
'''
    Using the put() and get() methods doesn't look very convenient to use. However, we would have preffered
    our hashtable as a list, as it would be easier to use.

    This can be easily done with special methods, __setitem__() and __getitem__().
'''

ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")

for key in("good","better","best","worst", "ad","ga"):
    print(ht.get(key))

print("The no. of total elements is : {}".format(ht.count))

'''
    Here we hae only used linear proing to deal with collisons but this is not the best solution.
    There areother strategies like chaining that we must look into.
'''