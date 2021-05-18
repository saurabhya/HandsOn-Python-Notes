'''
Arrays are continuous collection of similar objects. They work similar to list in python
but the major advantage that array posses is that it is much more efficient way of sorting data
that is of the same type. In the following example, we have created an integer array of the
digits from 0 to one million-1, and an identical list. Storing one million integers in an integer
array requires around 90% of the memory of an equivalent list.
'''
import array
import sys

ba = array.array('i', range(10**7))
bl = list(range(10**7))

print(100*sys.getsizeof(ba)/sys.getsizeof(bl))
