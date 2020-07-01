'''
    A queue can be implemented using a doubly linked list, and insertion
    and deletion operations on this data structure, and that has a
    time complexity of  O(1).
'''

class Node(object):
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        current = self.head
        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

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


