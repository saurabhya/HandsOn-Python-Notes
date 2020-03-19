class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        
        else:
            node.next = self.top
            self.top = node

        self.size += 1

    def pop(self):
        if self.top is None:
            print("List is Empty !!!")
            return None

        else:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

'''
Now let us look at an example application showing how we can 
use our stack implemetation. We are going to write a little 
function that will verify whether a statement contains 
brackets - (, [, { - is balanced, that is, whether the number 
of closng brackets matches the number of opening brackets. 
It will also ensure that one pair of brackets really is 
contained in one another. 

'''   

def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
            if last is '{' and ch is '}':
                continue
            elif last is '[' and ch is ']':
                continue

            elif last is '(' and ch is ')':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True
