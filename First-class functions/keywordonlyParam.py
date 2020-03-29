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
        return '<%s%s />'%(name, attr_str)
