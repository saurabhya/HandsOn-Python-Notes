"""
    Optinal parameters with default values are a great feature of Python fuction definition, allowing our APIs to evolve
    while remaining backward compatible. However, you should avoid mutable objects as default values for parameters.

    To illustrate this, we take the Bus class and change its __init__ method to create HautedBus. Here we tried to
    be clever and instead of having a default value of passengers = None, we have passengers =[], thus avoiding the
    if in the rpevious __init__. This "cleverness" gets us into trouble.
"""

class HauntedBus:
    """
        A bus model haunted by ghost passengers
    """
    def __init__(self, passengers =[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# Following shows the eerie behavior of the HauntedBus.
bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

# So far, so good: no surprises with bus1.
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
# Bus2 starts empty, so the default empty list is assigned to self.passengers.
bus3 = HauntedBus()
print(bus3.passengers)
# The default is no longer empty
bus3.pick("Dave")
print(bus2.passengers)
# same as bus3

print(bus2.passengers == bus3.passengers)
print(bus2.passengers is bus3.passengers)

# What about bus1
print(bus1.passengers)

"""
    The problem is that Bus instances don't get an initialpassenger list end up sharinng the same passenger list among
    themselves.
    Such bugs may be subtle. When HauntedBus is instantiated with passengers, it works as expected. Strange things
    happen only a HauntedBus start empty, because then self.passengers becomes an alias for the default value of the
    passengers parameter.
"""