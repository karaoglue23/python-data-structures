class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def partition_list(self,x):
        if self.length <= 1:
            return
        prev1 = dummy1 = Node(0)
        prev2 = dummy2 = Node(0)
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current.prev = None
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = temp
        if dummy2.next:
            prev1.next = dummy2.next
            dummy2.next.prev = prev1
        if dummy1.next:
            self.head = dummy1.next
        else:
            self.head = dummy2.next
        if self.head: self.head.prev = None


my_DLL = DoublyLinkedList(1)
my_DLL.append(11)
my_DLL.append(5)
my_DLL.append(2)
my_DLL.append(3)
my_DLL.append(6)
my_DLL.partition_list(5)
my_DLL.print_list()