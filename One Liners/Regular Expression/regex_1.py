"""
    The Dot Regex:
    First, we need to know how to match an arbitrary character by
    using the dot regex, the . character. The dot regex matches any
    character (including whitespace characters). You can use it to
    indicate that you don’t care which character matches, as long
    as exactly one matches:

"""


import re
text = '''A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography.
'''
print(re.findall('b...k', text))
# ['block', 'block', 'block']

"""
    The Asterisk Regex:
    Second, say we want to match text that begins and ends with
    the character 'y' and an arbitrary number of characters in
    between. How do you accomplish this? You can do by this
    using the asterisk regex, the * character. Unlike the dot regex,
    the asterisk regex can’t stand on its own; it modifies the
    meaning of another regex. Consider the following example:
"""
print(re.findall('y.*y', text))
# ['yptography']

"""
    The Zero-or-one Regex:
    Third, we need to know how to match zero or one characters
    by using the zero-or-one regex, the ? character. Just like the
    asterisk operator, the question mark modifies another regex, as
    you can see in the following example:
"""
print(re.findall('blocks?', text))
# ['block', 'block', 'blocks']

"""
    Equipped with these three tools—the dot regex ., the
    asterisk regex *, and the zero-or-one regex ?—you’re now able
    to comprehend the next one-liner solution
"""
txt = '<div>hello world</div>'
print(re.findall('<.*>', txt))
# ['<div>hello world</div>']
print(re.findall('<.*?>', txt))
# ['<div>', '</div>']
