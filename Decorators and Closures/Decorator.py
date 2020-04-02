"""
    Function decorators let us "mark" funtions i the source code to enhance their behavior in some way.
    This is poerful stuff, but mastering it requires understanding closures.

    Aside from their application in decorators, closures are also essential for effective asynchronous programming
    with callbacks, and for coding in a functional style whenever it makes sense.


    A decorator is a callback that takes another function as argument(the decorated function). The decorator may
    perform some processing with the decorated function, and returns it or replaces it with another function
    or callable object.

    In other words, assuming an existing decorator named decorate, this code:

    @decorate
    def target():
        print('running target()')

    has the same effect as writing this:

    def target():
        print('running target()')

    target= decorate(target)


    The end result is the same: at the end of either of these snippets, the target name does not necessarily refer to the
    origial target function, but to whatever function is returned by decorator(target)
"""

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()
print(target) # Inspection reveals that target is now a reference to inner.

"""
    Strictly speaking, decorators are just syntactic sugar. As we just saw, you can always aimply call a decorator like
    any regular callable, passing another function. Sometimes that is actually convenient, especially when doing
    metaprogramming - changing program behavior at runtime.


    A key feature of decorators is that they run right after the decorated function is defined. That is usually
    at import time.
"""

registry = []

def register(func):
    print('running register(%s)'%func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1')

@register
def f2():
    print('running f2')

@register
def f3():
    print('running f3')

def main():
    print('runing main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()


"""
    Note that register runs before any other function in the module. When register is called, it receives as an
    argument the function object being decorated.


"""