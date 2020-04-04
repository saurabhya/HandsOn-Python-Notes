"""
    imagine we are creating a tool to debuf web applications. We want to to be able to generate HTML deisplays for
    different types of Python objects.
    We could start with a function like this.
"""
import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

print(htmlize({1,2,3}))
print(htmlize(1))
print(htmlize("Hello"))
"""
    That will work for any Python type, but now we want to extend it to generate custom displays for some types.

    str: replace embedded newline characters with '<br>\n' and use <p> tags instead of <pre>.
    int: show the number in decimal and hexadecimal.
    list: output an HTML list, formatting each item according to its type.



    Because we don't have method or function overloading ion Python that we can create functions with same name for
    different data type. A common solution in Python would be to turn htmlize into dispatch fucntion, with a chain of
    if/elif/elif calling specialized functions like htmlize_str, htmlizre_int etc. This is not extensible by users
    of our module, and is unwieldy: over time, the htmlize dispatcher would become too big, and the coupling between it
    and the specialized functions would be very tight.

    The new functools.sigledispatch decorator in Python 3.4 allows each mdule to contribute to overall solution, and
    lets you easily provide a specialized function even for classes that you can't edit. If you decorate a plain function
    with @singledispatch, it becomes a generic function: a group of functions to perform the sameoperation in different
    ways, depending on the type of the first argument.
"""

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>'+inner+'</li>\n</ul>'


print(htmlize((1,2,3)))
print(htmlize(1))
print(htmlize("Hello"))

"""
    When possible, register the specialized functions to handle ABCs(abstract classes) such as numbers.Integral and
    abc.Mutablesequence instead of concrete implentations like int ans list. This allows your code to support a greater
    variety of compatible types. For example a Python extension can provide alternatives to the int type with fixed
    bit length as subclasses of numbers.Integral

    A notable quality of the singlediapatch mechanism is that you can register specialized function anywhere in the system,
    in any module. If you later add a module with a new user defined type, you can easily provide a new custom function
    to handle that type. And you can write custom functions for classes that you did not write and can't change.
"""