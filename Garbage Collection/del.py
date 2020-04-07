"""
    The del statement deletes names, not objects. An object may be garbage collected as result of a del command, but only if the
    variable deleted holds the last reference to the object, or if the object becomes unreachable. rebindinga a variable may
    also cause the number of references to an object to reach zero, causing its destrucion.

    To demonstrate the end of an object's life, following we are going to use weakref.finalize to register a callback function
    to be called when an object is destroyed.
"""
import weakref

s1 = {1,2,3}
s2 = s1 # s1 and s2 are aliases to the same set

def bye():  # This function must not be a bound method of the object about to be destroyed or otherwise hold a reference to it.
    print("Gone with the wind...")

ender = weakref.finalize(s1, bye) # register the bye callback on the object referred by s1.
print(ender.alive) # .alive attribute is True before the finalize object is called.

del s1 # del does not delete an object just a reference to it.
print(ender.alive)
s2 ='spam'
print(ender.alive)

"""
    Weak Refernces
        The presence of weak references is what keeps an object alive in memory. When the reference count of an object
        reaches 0, the garbage collector disposes of it. But sometimes it is useful to have a reference to an object that
        does not keep it around longer than necessary. A common use case is cache.

        Weak refernces of an object do not increase its reference count. The object that is target of a reference is called
        the referent. therefore we say that a weak reference does not prevent the referent from being garbage collected.

        weak references are useful in caching applications because you don't want the cached objects to be kept alive
        just because they are referenced by the cache.

        Following code shows how a weakref.ref instance can be called to reach its referent. If the object is alive, calling
        the weak reference returns it, otherwise None is returned.
"""
print("\nDemonstration of Weak reference")



import weakref
a_set = {0,1}
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2,3,4}
print(wref())