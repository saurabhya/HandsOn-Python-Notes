'''
    A priority queue is a data structure which is similar to the queue and stack data structures that stores data along
    with priority associated with it. In the priority queue, the item with the highest priority is served first.
    Priority queues are often implemented using heap, since it is very efficient for this purpose; however, it can be implemented using
    other data structures. It is a modified queue that returns the items in the order of highest priority, whereas the queue
    returns the items in the order they were added.

    A heap is a data structure that satisfies a heap property. A heap property states that there must be a certain relationship
    between a parent node and its child nodes. This property must apply throughout the entire heap.
    In a min heap, the relationship between parent and children is that the value at the parent must always be less than
    or equal to its children. As a consequence of this, the lowest element in the heap must be the root.
    In max heap, on the other hand, the parent is greater than or equal to its children. It follows from this that the largest value
    makes up root node.

    The heaps are binary trees, and although we are going to use a binary tree, we will actually use a list to represent it.
    For the ease of implementation we will be ignoring index 0.
    In heap, you can retrieve the hildren of any node at the n index very easily. The left child id located at 2n, and the
    right child is located at 2n+1. This will always hold true.

    Now we will see the implementation of min heap.
'''

class Heap:
    def __init__(self):
        self.heap = [0] # We initialize our heap list with 0 to represent the dummy first element.
        self.size = 0

    '''
        Inserting an item in the min heap works in two steps. First, we add the new element to the end of the list and
        increase the size by 1. then we need to arrange the new element up in the heap tree, to organise all the nodes in such a way that
        it satisfies the heap property.
    '''
    def arrange(self, k):
        while k//2 > 0:
            if self.heap[k]< self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k = k//2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    '''
        The pop operation operation removes an element from the heap. The reason for removing an element from the min-heap is,
        first , to find out the index of the item to be deleted, and then organise the heap so that it satisfies the heap property.
        however, it is more common to pop off the minimum value from the min heap, and as per the property of the min-heap,
        we can get the minimum value from its root value. Therefore to obtain minimum value, we remove the root node and
        re-organise all the nodes of the heap. We also decrement the size of the heap by one.

        however, once the root has been popped off, we need a new root node. For this, we just take the last item from the list and make
        the new root node. However, the selected node may not be the lowest element in the heap, so we need to reorganise the nodes
        of the heap.
    '''
    def minindex(self, k):
        if k*2+1 > self.size:
            return k*2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k*2
        else:
            return k*2+1

    def sink(self, k):
        while k*2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

h = Heap()

for i in (4,8,7,2,9,10,5,1,3,6):
    h.insert(i)

print(h.heap)

for i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)

'''
    Seletion algorithm fall under a class of algorithms that seek to answer the problem of finding the ith smallest element in the list.
    When a list is sorted in ascending order, the first element in the list will be the smallest item in the list. The second
    element in the list will be be the second smallest element in the list. The last element in the list will be the least-smallest
    element in the list.

    In creating the heap data structure, we have come understand that a call to the pop method will return the smallest element
    in the min-heap. The first element to pop off a min heap is the smallest element in the list. Similarly, the seventh element to be
    popped off the min heap will be the seventh-smallest element in the list.
'''

