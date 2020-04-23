"""
    Before Python 2.2, it was not possible to subclass built-in types such as
    list or dict. Since then, it can be done but there is a major caveat:
    the code of the built-ins(written in C) does not call
    special methods overridden by user defined classes.
"""

class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value]*2)

dd = DoppleDict({'one': 1}) # The __init__ method inherited from dict clearly ignored that
print(dd)                   # __setitem__ was overridden: the value of 'one' is not duplicated.

dd['two'] = 2 # The [] operator call our __setitem__ and works as expected
print(dd)

dd.update(three = 3) # The update method from dict does not use our version of __setitem__
print(dd)            # either: the value of 'three' was not duplicated.

print("\n")
"""
    The built-in behavior is a violation of a basic rule of object-oriented programming:
    the search for method should always start from the class of the target instance(self),
    even when the call happens inside a method implemented in a superclass.

    The problem is not limited to calls within an instance - whether self.get() calls
    self.__getitem__() - but also happens with overridden methods of the other classes
    that should be called by the built-in methods.
"""

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a = 'foo')
print(ad['a'])

d = {}
d.update(ad)
print(d['a']) # The dict.update method ignored our AnswerDict.__getitem__.
print(d)

"""
    However, if you subclass collections.UserDict instead of dict,
    the issues exposed in examples above are fixed.
"""