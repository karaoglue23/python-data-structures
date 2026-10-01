class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
            self.tail = new_node
        self.length += 1

    def merge(self,other_list):
        dummy_node = Node(0)
        current = dummy_node
        self_current = self.head
        other_list_current = other_list.head
        while self_current and other_list_current:
            if self_current.value <= other_list_current.value:
                current.next = self_current
                current = self_current
                self_current = self_current.next
                current.next = None
            else:
                current.next = other_list_current
                current = other_list_current
                other_list_current = other_list_current.next
                current.next = None
        if self_current:
            while self_current:
                current.next = self_current
                current = self_current
                self_current = self_current.next
                current.next = None
        if other_list_current:
            while other_list_current:
                current.next = other_list_current
                current = other_list_current
                other_list_current = other_list_current.next
                current.next = None
        self.tail = current
        self.head = dummy_node.next
        
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""