
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __repr__(self):
        return str(self.data)


'''
Binary Tree
    A binary tree is one in which each node has a maximum of two
    children. The nodes in the binary tree are organized in the 
    form of left sub-tree and right sub-tree. If the tree has a 
    root, R, and two sub-trees, that is, left sub-tree T1 , and 
    right sub-tree T2 , then their roots are called left successor 
    and right successor , respectively.
'''
'''
Binary search Tree
    A binary search tree (BST) is a special kind of binary tree. 
    It is one of the most important and commonly used data structures
    in computer science applications. A binary search tree is a tree
    that is structurally a binary tree, and stores data in its nodes
    very efficiently. It provides very fast search operations, and other
    operations, and other operations such as insertion and deletion 
    are also very easy and convenient.

    A binry tree is a binary search tree if the value at any node in the
    tree is greater than values in all the nodes of its left sub-tree, and 
    less or equal to the values of all the nodes of the right sub-tree.
    For example, if K1, K2 and K3 are key values in a tree of three nodes,
    where K1 is the root and k2 is left child and k3 is right child in the tree, 
    then it should satisfy following conditions:

    1. The key values of k2<=K1
    2. The key values K3>K1 
'''

class Tree:
    def __init__(self):
        self.root_node = None

    '''
    The operations that can be performed on a binary search tree are
    insert, delete, finding min, finding max, searching and so on.
    '''
    '''
    Finding the minimum and maximum nodes
        To find a node that has the smallest value in the tree, we start
        traversal from the root of the tree and visit the left node each 
        time until we reach the end of the tree. Similarly, we traverse 
        the right subtree recursively until we reach the end to find the 
        node with the biggest value in thr tree.
    '''
    # The Python implementation of the method that reyurns the minimum
    # node is as follows:
    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child 
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current
    '''
    The running complexity to find the minimum or maximum value is
    O(h), where h is the height of the tree.
    '''

    '''
    Inserting Node
        One of the most important operations to implement on a binary search tree 
        is to insert data items in the tree. As we have already discussed, 
        regarding the properties of the binary search tree, for each node 
        in the tree, the left child nodes should conatain the data less than
        their value. So, we have to ensure that the property of the binary
        search tree satisfies whenever we insert an item in the tree.
    '''
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
    '''
    Another important operattion on a BST is the deletion or removal
    of nodes. These are three scenarios that we need to cater for 
    during this process. The node that we want to remove might have
    the following:

    1. No children: If there is no leaf node, directly remove the node.
    2. One child: In this case, we swap the value of that node with its
       child, and then delete it.
    3. Two children: In this case, we first find the in-order successor
       predecessor, swap the value with it, and then delete that node.

    Our node class does not have a reference to a parent. As such, we need
    to use a helper method to search and return the node with its parent node.
    This method is similar to the search method:
    '''
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return(parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return(parent, current)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        # get children count
        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        '''
        After we know the number of children a node has that we want to dlete, 
        we need to handle various conditions in which a node can be deleted.
        The first part of the if statement handles the case where the node has 
        no children:
        '''
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        # In cases where the node to be deleted has only one child, the elif part of
        # the if statement does the following.
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        # case where there are 2 children
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    '''
    A binary search tree is a tree data structure in which all the nodes follow the property
    that all the nodes in the left sub tree of a node have lower key values, and have greater key 
    values in its right sub-tree. Thus, searching for an element with a given key value is quite easy.
    '''
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    