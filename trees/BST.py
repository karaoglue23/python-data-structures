class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self): # creates an empty list at first
        self.root = None

    def insert(self,value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        current = self.root
        while current:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return True
            elif value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return True
            else:
                return False
    
    def contains(self,value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

my_tree = BinarySearchTree()
print(my_tree.root)
my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(0)
my_tree.insert(3)
my_tree.insert(3)
my_tree.insert(6)
my_tree.insert(4)
my_tree.insert(5)
print(my_tree.contains(5))