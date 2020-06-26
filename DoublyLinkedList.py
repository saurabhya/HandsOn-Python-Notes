'''
The Python code to create a doubly linked list node includes its initializing
methods, the prev pointer, the next pointer, and the data instance variables.
When a node is newly created, all these variables default to None.

'''

class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        self.data  = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    # we are adopting a new convention here: we are naming head to the
    # beginning of the list and tail as the end of the list.

    def append(self, data):
        ''' Append an item to the list'''
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.count += 1

    def delete(self, data):
        '''Delete a node from the list'''
        current = self.head
        node_deleted = False
        if current is None:
            # list is empty
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1
        elif node_deleted == False:
            print("Item Not found !!!")

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False
