'''
    The call operator(i.e.()) may be applied to other objects beyond user-defined functions. To determine
    whether an object is callable, use the callable() built-in function. The Python Data Model documentation
    lists seven callable types.

    User Defined Callable Types
        Not only are Python functions real objects, but arbitrary Python objects may also be made to behave
        like functions. Implementing __call__ instance method is all it takes.
'''

import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

'''
    __init__ accepts any iterable; building a local copy prevents unexpected side effects
    on any list passed as an argument.

    shuffle is guaranteed to work because self._items is a list

    shortcut to bingo.pick(): bingo()
'''
bingo = BingoCage(range(3))

print(bingo.pick())
print(bingo())

print(callable(bingo))

'''
    A class implementing __call__ is an easy way ro create function-like objects that have
    some internal state that must be kept across invocations, like the remaining items in the BingoCage.

'''