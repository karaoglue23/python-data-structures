class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __kth_smallest(self,current_node,num_visited,k):
        kth_smallest_value = None
        if current_node.left:
            kth_smallest_value =  self.__kth_smallest(current_node.left,num_visited,k)
        if kth_smallest_value is not None:
            return kth_smallest_value
        num_visited[0] += 1
        if num_visited[0] == k:
            return current_node.value
        if current_node.right:
            return self.__kth_smallest(current_node.right,num_visited,k)
        return None

    def kth_smallest(self,k):
        if self.root is None:
            return None
        num_visited = [0]
        return self.__kth_smallest(self.root,num_visited,k)


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """