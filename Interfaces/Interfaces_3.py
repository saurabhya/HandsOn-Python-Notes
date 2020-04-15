"""
    Preiously, issubclass(EmlParsernew, UpdatedInformalPasrerInterface) returned True,
    even though IpdatedInformalParserInterface did not appear in the EmlparserNew MRO.
    That's because UpdatedInformaParserInterface is virtual base class of EmlParserNew.

    The key difference between these and standard subclass is that virtual subclasses use
    the .__subclasscheck__() dunder method to impliitely check if a class is a virtual
    subclass of the superclass. Additionaly, virtual base classes don't appear in
    the subclass MRO.

    Let's look at the following:
"""

class PersonMeta(type):
    """A person Metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck____(cls, subclass):
        return (hasattr(subclass,'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))

class PersonSuper:
    """A person Superclass"""
    def name(self) -> str:
        pass
    def age(self) -> int:
        pass

def Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass"""
    pass

"""
    here, we have the setup for creating your virtual base classes
    1. The meta class PersonMeta
    2. The base class PersonSuper
    3. The Python interface Person

    Nw, that the setup for creating virtual base classes is done you'll
    define two concrete classes, Employee and Friend. The Employee class
    inherits from PersonSuper, while Friend implicitly inherits from Person.
"""

class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__ """
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person sice
    both required methods exist."""
    def name(self):
        pass
    def age(self):
        pass

"""
    Although Friend does not explicitely inherit from Person, it implements .name() and .age(),
    So Person becomes a virtual base class of Friend. When you run issubclass(Friend, Person)
    it should return True, meaning that Friend is a subclass of Person.
"""