"""
    When parsing a decorator in source code, Python takes the decorated function and passes it as the first argument
    to the decorator function. So how do you make a decorator accept other arguments?
    The answerr is: make a decorator factory that takes those arguments and returns a decorator, which is then applied
    to the function to be decorated.
"""

registry = []

def register(func):
    print('running register(%s)'%func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

print('running main()')
print('regisrty->', registry)

f1()

"""
    Above is the implementation of a simple decorator that we saw earlier in decorator.py
"""

print("\n\nTHIS THE NEW IMPLEMENTATION\n")
"""
    In order to make it easy to enable or disable the function registration performed by register, we'll make it accept
    an optional active parameter which, if False, skips registering the decorated function.
    Conceptually, the new register function is not a decorator but a decorator factory. When called, it returns
    the actual decorator that will be applied to the target function.
"""

registry = set()

def register(active = True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'%(active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register(active = True)
def f2():
    print('running f2()')

def f3():
    print('running f3()')

f1()
f2()
print('registry ->', registry)