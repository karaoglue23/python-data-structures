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

    def BFS(self):
        if self.root is None:
            return []
        queue = [self.root]
        results = []
        while queue:
            results.append(queue[0].value)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        return results
    
    def dfs_pre_order(self):
        if self.root is None:
            return []
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        if self.root is None:
            return []
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results        

    def dfs_in_order(self):
        if self.root is None:
            return []
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results        
       

my_bst = BinarySearchTree()
my_bst.insert(10)
my_bst.insert(9)
my_bst.insert(11)
my_bst.insert(12)
my_bst.insert(8)
my_bst.insert(10.5)
my_bst.insert(9.5)
print(my_bst.BFS())
print(my_bst.dfs_pre_order())
print(my_bst.dfs_post_order())
print(my_bst.dfs_in_order())
