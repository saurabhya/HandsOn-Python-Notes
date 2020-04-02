"""
    A registration decorator is a good enhancement to the ecommerce promotional discount from design patterns and strategies
    In our previous strategy we had separate function definitions for different promo type and then promos list was used by
    best_promo function to determine the highestdiscount applicable. The repetition is problemetic because someone may add
    a new promotional strategy function and forget to manually add it to the promos list - in which case, best_promo will
    silently ignore the new strategy, introducing a subtle bug in the system.
"""

from collections import namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:        # the context
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total


    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f}  due: {:.2f}>'
        return fmt.format(self.total(), self.due())



promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """
        5% discount for customers with 1000 or more fidelity points
    """
    return order.tota;()*0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """
        10% discount for each LineItem with 20 or more units
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total()*.1
    return discount

@promotion
def large_order(order):
    """
        7% discount for orders with 10 or more distinct items
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """
        Select best discount available
    """
    return max(promo(order) for promo in promos)


