"""
    Let's start with classmethod, to define a method that operats on the class and not on instances.
    classmethod changes the way the method is called, so it recieves the calss itself as the first argument,
    instead of an instance. Its most common use use is for alternatives constructors, like frombytes.

    In constrast, the staticmethod decorator changes a method so that it recieves no special first argument.
    In essence, a static method is just like a plain function that happens to live in a class body, instead of
    being at the module level.

"""

class Demo:
    @classmethod
    def klasmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klasmeth())
print(Demo.klasmeth('Spam'))
"""
    No matter how you envoke it, Demo.klassmeth receives the Demo class as the first argument.
"""

print(Demo.statmeth())
print(Demo.statmeth('Spam'))