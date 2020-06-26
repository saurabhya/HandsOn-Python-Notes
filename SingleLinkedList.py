'''
    In Python, you don't manipulate pointers directly, unlike in some other languages, such as C or Pascal.
    This has led some people to believe that pointers aren't used in Python.
    nothing is further from the truth.

    For example:

    s = set()
    here s is more a reference than a variable: set is an object created in the memory
    and a pointer(reference) is given to s. s points to the set object in the memory.
'''
# Class Node

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
    # The first operation that we need to perform is to append items to the list.
    # This operation is sometimes called insert operation. Here we get a chance
    # to hide away the node class. The user of our list class should really
    # never have to interact with Node objects. These are purely for internal use.
    def append(self, data):
        '''
            There is a big problem with append method i.e. maintaining only a single
            pointer for the start of the list may cause running time of the insertion
            to be O(n) where n is the length of the list. For lists where n is very large,
            It presents a huge issue.

            What can be the solution for that ?

            We can maintain an additional pointer for the end of the list that will help
            to reduce the running time of insertion from O(n) to O(1).
        '''
        # Encapsulate data in a Node
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node

    '''
        def __repr__(self):
            res = []
            current = self.tail
            while current:
                res.append(current.data)
                res.append('->')
                current = current.next

            return "".join(res)

        Above function uses magic function __repr__ to showcase list traversal.
        But if you notice in the above list traversal, where we are exposing the node class to
        the client/user. however, it is desirable that the client node should not interact with
        the node object. We need to use node.data to get the contents of the node and node.next
        to get the next node. We can access the data by creating a method that returns a generator.
    '''
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    '''
        Next operation we have to consider in the list is deletion.
        When we want to delete a node that is between two other nodes, all we have to do is we
        make the previous node point to the successor of its next node that is to be deleted.
        Following is the proposed solution.
    '''
    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    '''
        We may also need a way to check whether a list conains an item. This method is
        fairly easy to implement thanks to iter() method we previously wrote. Each pass
        of the loop compares the current data to the data being searched. If a match is
        found, True is returned, or else False is returned:
    '''
    def search(self, data):
        for node in self.iter():
            if data == node :
                return True

        return False


    '''
        Clearing a list?

        We may need to clear a list quickly; there is a very simple way to do it.
        We can clear a list by simply clearing the pointer head and tail by
        setting them to None.

    '''
    def clear(self):
        self.tail = None
        self.head = None


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
for word in words.iter():
    print(word)
