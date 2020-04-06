"""
    When you are coding a function that recieves a mutable parameter, you should carefully consider
    whether the caller expects the argument passed to be changed.

    For example, if your function recieves a dict and needs to modify it while processing it,
    should this side effect be visible outside the function or not? Acutally it depends on the context. It's really
    a matter of aligning the expectation of the coder of the function and that of the caller.
    Following example of TwilightBus tries to show this.
"""

class TwilightBus:
    """
        A bus model that makes passengers vanish
    """
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers # this assignment makes self.passengers an alias of passengers, which in turn is an alias for parameter passed.
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue','Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)