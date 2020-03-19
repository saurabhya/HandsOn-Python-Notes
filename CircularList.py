class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.count += 1

    def delete(self, data):
        '''
        Delete function for a circular list has a unique problem,
        we cannot traverse the list untill current reaches to None
        because there is no None pointer in circular list.

        We thus need to find a way to control the while loop. We 
        cannot check whether current has reached head, because then
        it will never check for the last node. But we can use prev,
        it lags behind current by one node. However there is a special case.
        The very first loop iteration, current and prev will point to the 
        same node, namely the head node.
        '''
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            if current.data == data :
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                     prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            val = current.data
            prev = current
            current = current.next
            yield val
    
    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False
