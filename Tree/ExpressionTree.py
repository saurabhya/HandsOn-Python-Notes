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



################################################################################3
class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.data)
    


expr = "4 5 + 5 3 - *".split()
stack = Stack()

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    stack.push(node)

def calc(node):
    if node.data is "+":
        return calc(node.left) + calc(node.right)
    elif node.data is "-":
        return calc(node.left) - calc(node.right)
    elif node.data is "*":
        return calc(node.left) * calc(node.right)
    elif node.data is "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data

root = stack.pop()
result = calc(root)
print(result)