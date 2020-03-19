class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __repr__(self):
        return str(self.data)


'''
To test this class , we must first create four nodes - n1,n2,n3 and n4:

'''
n1 = Node("root node")
n2 = Node("Left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

'''
Next, we connect the nodes to each other according to the property
of a binary tree. We let n1 be the root node, with n2 and n3 as 
its children. Finally, we take n4 as the left child to n2.
'''
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


'''
The important operation that we can perform is traversal. To understand
traversing, let's traverse the left sub-tree of the binary tree.
We will start from the root node, print out the node, and move
down the tree to the next left node. we keep doing this until we 
have reached the end of the left sub-tree, like so:
'''    
'''
current = n1

while current:
    print(current.data)
    current = current.left_child
'''

'''
OUTPUT :

root node
Left child node
left grandchild node

'''

'''
Tree Traversal

    The method to visit all the nodes in a tree is called tree traversal.
    This can be done with either depth-first search(DFS) or breadth-first
    search(BFS).

    Depth-first traversal

        In depth first first traversal, we traverse the tree, starting from the root,
        and go deeper into the tree as much as possible on each child, and then continue 
        to traverse to the next sibling. We use the recursive approach for the tree traversal.
        There are three forms of depth-first traversal, namely in-order, pre-order, and post-order.
        
        In-order Traversal and infix notation

            In-order tree traversal works as follows. First of all, we check if the current node is null or empty. 
            If it is not empty, we traverse the tree. In in-order tree traversal, we follow these steps:
            1. We start traversing the left subtree and acall the inorder function recursively.
            2. Next, we visit the root node.
            3. Finally, we traverse the right sub-tree and call the inorder function recursively.
            
            so, in a nutshell, in in-order tree traversal, we visit the nodes in the tree in the order of
            (left sub-tree, root, roght sub-tree). 
'''
from collections import deque
class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)
    '''
    Pre-order traversal and prefix notation
        Pre-order tree traversal works as follows.
        
        First of all check if the current node is null or empty. If it is not
        empty, we traverse the tree. The pre-order tree traversal works as follows:
        1. we start traversing the root node.
        2. Next, we traverse the left sub-tree and call the preorder function with the left sub-tree recursively.
        3. Next, we traverse the right sub-tree and call the preorder function with the right sub-tree recursively.

        So, to trverse a tree in a pre-order mode, we visit the tree in the order of root node, left sub-tree and 
        the right sub-tree node.

    '''
    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)

    '''
    Post-order traversal and postfix notation
        Post-order tree traversal works as follows.
        First of all, we check if the current node is null or empty. If it is not 
        empty, we traverse the tree. Post-order tree travesal works as follows:
        1. We start traversing the left sub-tree and call the postorder function recursively.
        2. Next, we travese the right sub-tree and call the postorder function recursively.
        3. Finally, we visit the root node
        
        so, in a nutshell, regarding post-order tree traversal, we visit the nodes in the tree
        in the order of left sub-tree, right sub-tree and finally the root node.

    '''
    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)
    '''
    Breadth-first search
        Breadth-first traversak starts from the root node of the tree and then visits every node 
        of the next level of the next level of the tree. Then, we move to the next level of the tree, 
        and so on. this kind of tree ttraversal is breadth-first as it broadens the tree by traversing
        all the nodes in a level before going deep into the tree. 
    
        This mode of traversal is implemented using a queue data structure. Starting with the root node, 
        we push it into a queue. The node at the front of the queue is accessed(dequeued) and either 
        printed or stored for later use. the left node is added to the queue followed by the right node.
        Since the queue is not empty, we repeat this process.
    '''
    def breadth_first_traversal(self, root_node):
        list_of_nodes = []
        traversal_queue = deque([root_node])
        # We enqueue the root node and keep a list of the visited nodes in th list_of_nodes list.
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)
            if node.left_child:
                traversal_queue.append(node.left_child)
            if node.right_child:
                traversal_queue.append(node.right_child)

        return list_of_nodes

        
    
    
tree = Tree()
tree.inorder(n1)
tree.preorder(n1)
tree.postorder(n1)
print(tree.breadth_first_traversal(n1))



    