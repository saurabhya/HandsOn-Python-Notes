'''
Queues can also be implemented using two stacks, We initially 
set two instance variable to create an empty queue upon initialization.
These are the stacks that will help us to implement a queue. 
The stack, in this case, are simply Python lists that allow us to 
call push and pop methods on them, which eventually sllow us
to get the functionality of enqueue and dequeue operations.

'''

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
        '''
        The inbound_stack is only used to store elements that are
        added to the queue. No other operation can be performed 
        on this stack.
        '''
    def enqueue(self, data):
        '''
        data is passed to the append method of the inbound_stack in
        the queue class. Further, the append method is used to mimic
        the push operation, which pushes items to the top of the stack
        
        '''
        self.inbound_stack.append(data)

    def dequeue(self):
        '''
        The dequeue operation is used to delete the elements from the
        queue in the order of items added. New elemets added to our 
        queue end up in the inbound_stack. We shall delete the elements
        from our queue only through the outbound_stack.
        '''
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()

             

queue = Queue()
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(9)
print(queue.inbound_stack)
queue.dequeue()
print(queue.inbound_stack)
print(queue.outbound_stack)
queue.dequeue()
print(queue.outbound_stack)