'''
    Queues can be implemented using various methods such as list,
    stack and node. We shall discuss the implementation od queues
    using all these methods one by one. Let's start by implementing
    a queue using Python's list class. This is to help us quickly
    learn about queues. The operations that can be performed on the
    queue are encapsulated in the ListQueue class.
'''

class ListQueue:
    def __init__(self):
        '''
            In the initialization method, __init__, the items
            instance variable is set to [] which means the queue
            is empty when created. The size of the queue is also
            set to zero.
        '''
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data) # Always insert items at index 0
        self.size += 1 # increment thesize of the queue by 1

    def dequeue(self):
        data = self.items.pop() # delete the top most item from the queue
        self.size -= 1 # decrement the size of the queue by 1
        return data

'''
    The enqueue operationis very inefficient due to one reason.
    The method has to first shift all the elements by one space.
    Imagine there are 1 million elements in a list which need to be
    shifted around any time a new element is being added to the queue.
    This will make the enqueue process very slow for large lists.
'''
