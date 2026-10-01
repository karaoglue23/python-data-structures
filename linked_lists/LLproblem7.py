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

    def reverse_between(self,idx1,idx2):
        if self.length <= 1:
            return
        if idx1 >= idx2:
            return
        if idx1 < 0 or idx2 >= self.length:
            return

        current = self.head
        for _ in range(idx1):
            prev1 = current
            current = current.next
        first_current = current
        after = current.next
        for _ in range(idx2 - idx1):
            temp = after.next
            after.next = current
            current = after
            after = temp
        if idx1 == 0:
            self.head = current
            first_current.next = after
        else:
            prev1.next = current
            first_current.next = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.reverse_between(0,2)
my_linked_list.print_list()            


