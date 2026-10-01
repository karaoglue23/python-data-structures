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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result  
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def swap_pairs(self):
        if self.length <= 1:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        before = dummy
        
        while before.next and before.next.next:
            first = before.next
            second = before.next.next
            
            # swap
            first.next = second.next
            second.next = first
            before.next = second
            
            # move before forward
            before = first
        
        self.head = dummy.next 



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.swap_pairs()
my_linked_list.print_list()
