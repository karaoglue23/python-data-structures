class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def is_palindrome(self):
        if self.length == 0:
            return True
        if self.length == 1:
            return True
        forward = self.head
        backward = self.tail
        for _ in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True
    

my_DLL = DoublyLinkedList(1)
my_DLL.append(2)
my_DLL.append(3)
my_DLL.append(4)
my_DLL.append(5)
my_DLL.append(4)
my_DLL.append(3)
my_DLL.append(2)
my_DLL.append(1)
print(my_DLL.is_palindrome())