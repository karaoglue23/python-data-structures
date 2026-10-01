class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
                  
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)

    #   +===================================================+
    #   |                                                   |
    #   | Description:                                      |
    #   | - Private method to invert a binary tree.         |
    #   | - It swaps every left child with its right child  |
    #   |   recursively.                                    |
    #   |                                                   |
    #   | Parameters:                                       |
    #   | - node: The current node being visited.           |
    #   |                                                   |
    #   | Return:                                           |
    #   | - The node after its subtree has been inverted.   |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - The function works recursively, swapping left   |
    #   |   and right children of all nodes in the tree.    |
    #   | - A temporary variable is used to facilitate the  |
    #   |   swap of the children.                           |
    #   +===================================================+
    def __invert_tree(self,current):
        if current is None:
            return None
        temp = current.left
        current.left = self.__invert_tree(current.right)
        current.right = self.__invert_tree(temp)
        return current

my_bst = BinarySearchTree()
my_bst.r_insert(5)
my_bst.r_insert(3)
my_bst.r_insert(7)
my_bst.r_insert(4)
my_bst.r_insert(2)
my_bst.r_insert(6)
my_bst.r_insert(8)
my_bst.invert()