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
    
    def __r_contains(self,current_node,value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        
        if current_node.value < value:
            return self.__r_contains(current_node.right,value)
        else:
            return self.__r_contains(current_node.left,value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)

    def __r_insert(self,current_node,value):
        if current_node is None:
            return Node(value)

        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left,value)
        elif current_node.value < value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root,value)


    def min_value(self,current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self,current_node,value):
        if current_node is None:
                return None

        if current_node.value > value:
            if current_node.left:
                current_node.left = self.__delete_node(current_node.left,value)
        elif current_node.value < value:
            if current_node.right:
                current_node.right = self.__delete_node(current_node.right,value)
        else:
            if current_node.left is None and current_node.right is None:
                current_node = None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is  None:
                current_node = current_node.left
            else:
                current_node.value = self.min_value(current_node.right)
                current_node.right = self.__delete_node(current_node.right,current_node.value)

        return current_node
                
    def delete_node(self,value):
        self.__delete_node(self.root,value)



my_tree = BinarySearchTree()
print(my_tree.root)
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(48)
my_tree.r_insert(18)
my_tree.r_insert(17)
my_tree.r_insert(19)
print(my_tree.contains(21))
my_tree.delete_node(21)
print(my_tree.contains(21))
print(my_tree.min_value(my_tree.root))

