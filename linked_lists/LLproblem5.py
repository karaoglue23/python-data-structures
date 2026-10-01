class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 
    
    def binary_to_decimal(self):
        decimal = 0
        if self.head is None:
            return
        current = self.head
        while current:
            decimal *= 2
            decimal += current.value
            current = current.next
        return decimal
    
my_linked_list = LinkedList(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)
print(my_linked_list.binary_to_decimal())