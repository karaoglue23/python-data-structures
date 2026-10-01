class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            for _ in range(2):
                fast = fast.next
            slow = slow.next
        return slow
    
my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
print(f"middle node's value: {my_linked_list.find_middle_node().value}")
my_linked_list.append(7)
print(f"middle node's value: {my_linked_list.find_middle_node().value}")