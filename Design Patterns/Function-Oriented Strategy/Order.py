"""
    Each concrete strategy in classic strategy is a class with a single method, discount.
    Furthermore, the strategy instances have no state. You could say they are a lot like plain functions,
    and you would be right. Now we will see another stratey, replacing the concrete strategies
    with simple functions and removing the Promo abstract class.
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

def fidelity_promo(order):
    """
        5% discount for customers with 1000 or more fidelity points
    """
    return order.total()*.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """
        10% discount fo reach LineItem with 20 or more units
    """
    discount = 0
    for item in order.cart:
        if ite.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """
        7% discount for orders with 10 or more distinct items
    """
    disctinct_items = {item.product for item in order.cart}
    if len(disctinct_items) >= 10:
        return order.total()*0.7
    return 0