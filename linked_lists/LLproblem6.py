class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self,value):
        if self.length <=1:
            return
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < value:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = dummy2.next
        prev2.next = None
        dummy2.next = None
        self.head = dummy1.next
        dummy1.next = None

my_linked_list = LinkedList(1)
my_linked_list.append(6)
my_linked_list.append(11)
my_linked_list.append(3)
my_linked_list.append(15)
my_linked_list.print_list()
my_linked_list.partition_list(5)
my_linked_list.print_list()