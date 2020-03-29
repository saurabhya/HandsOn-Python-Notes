'''
    One of the best featurs o fPython functions is the extrememly flexible parameter handling
    mechanism, enhanced with keyword-only arguments in Python3. Closely related are the use
    of * and ** to "explode" iterables and mappings into separate arguments when we call a function.
'''

def tag(name, *content, cls = None, **attrs):
    """
        Generates one or more HTML tags
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"'%(attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %(name, attr_str, c, name) for c in content)
    else:
        return '<%s%s/>'%(name, attr_str)

print(tag('br'))
print(tag('p','hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id = 23))

print(tag('p', 'hello', 'world', cls='sidebar'))

print(tag(content = 'testing', name = "img"))

my_tag = {'name' : 'img',
            'title' : 'Sunset Boulevard',
            'src' : "sunset.jpg",
            'cls' : 'framed'}

print(tag(**my_tag))


'''
    Keyword - only arguments are a new feature in Python3. In the above example, the cls parameter can only
    be given as a keyword argument - it will never capture unnamed positional arguments. To specify keyword-only
    arguments when defining a function, name them after the argument prefixed with *. If you don't want to support
    variable positional arguments but still want keyword arguments, put a * by itself in the signature like:
        def f(a, *, b):
            return a, b
    Now that keyboard-only arguments do not need to have a default value: they can be mandatory, like b in the
    above example.
'''