"""
    In context of object-oriented programming, a protocol is an informal interface, defined only
    in documentation and not in code. For example, the seuence protocol in Python entails just the
    __len__ and __getitem__ methods. Any class Spam that implements those methods with the standard
    signature and semantics can be used anywhere a sequence is exected.
    Whether Spam is a subclass of this or that is irrelevant; all that
    matters is that it provides the necesary methods.
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards(position)

    """
        The FrenchDeck here takes advantage of many Python facilities because
        it implements the sequence protocol, even if that is not declared aywhere
        in the code. We say it is a sequence because it behaves like one,
        and that is what matters. This became known as Duck typing.

        Because protocols are informal and unenforced, you can often get away
        with just implementing just part of a protocol, if you know the specific
        context where a class will be used.
    """