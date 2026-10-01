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
    def remove_duplicates(self):
        if self.length <= 1:
            return
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.value == current.value:
                    temp = runner.next
                    runner.next = temp.next
                    temp.next = None
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.remove_duplicates()
my_linked_list.print_list()