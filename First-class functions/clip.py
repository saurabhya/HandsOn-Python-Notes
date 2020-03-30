'''
    Within a function object, the __default__ attribute holds a tuple with default values positional and keyword
    arguments. The defaults for keyword only arguments appear in __kwdefaults__. The names of the arguments, however,
    are found within the __code__ attribute, which is a reference to a code object with many attributes of its own.
'''

def clip(text, max_len = 80):
    '''
        Return text clipped at the last space before or after max_len
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_before = text.rfind(' ', max_len)
            if space_before >= 0:
                end = space_before
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()


# >>> from clip import clip
# >>> clip.__defaults__
# (80,)
# >>> clip.__code__
# <code object clip at 0x00000212FE5D89C0, file "C:\Users\Saurabh\Documents\GitHub\HandsOn-Python-Notes\First-class functions\clip.py", line 7>
# >>> clip.__code__.co_varnames
# ('text', 'max_len', 'end', 'space_before')
# >>> clip.__code__.co_argcount
# 2