'''
I the following program we are going to see the power of implementing just two special methods, __getitem__
and __len__.
'''
import collections

Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

'''
    The first thing to note is the use of collections.namedtuple to construct a simple class to represent
    individual cards. Since Python 2.6, namedtuple can be used to build classes of objects that are just
    bundles of attributes with no custom methods, like a database record.
'''

beer_card = Card('7', 'diamonds')
print(beer_card)

'''
    But the point here is FrenchDeck class, like any standard Python collection, a deck responds to the
    len() function by returning the number of cards in it.

'''

deck = FrenchDeck()
print(len(deck))

'''
    Reading specific cards from the deck - say, the first or the last should be as easy as deck[0]
    or deck[-1], and this is what the __getitem__ method provides.
'''
print(deck[0])
print(deck[-1])

'''
    Should we create a method to pick a random card? No need.
    Python already has a function to get a random item from a sequence: random.choice.

'''

from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

'''
Because __getiten__ delegates to the [] operator of self._cards, our deck automatically
supports slicing. Here's how we look at the top three cards from a brand new deck,
and then pick just the aces by starting on index 12 and skipping 1 cards at a time.
'''

print(deck[:3])
print(deck[12::13])

'''
Just by implementing the __getitem__ special method, our deck is also iteratable.
'''

for card in deck[:4]:
    print(card)

'''
A common system of ranking cards is by rank(with aces being highest), then by suit in the order of
spades, then hearts, diamonds, and clubs.
Here is a function that ranks cards by that rule, returing 0 for the 2 of clubs and 51 for the ace of spades.
'''
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print(card)

'''
    Although FrenchDeck implicitly inherits from objject, its functionality is not inherited, but comes from
    levaraging the data model and composition. By implementing the special methods __len__ and __getitem__,
    our FrenchDeck behaves like a standard Python sequence, allowing it to benefit from core language fetaures.
'''