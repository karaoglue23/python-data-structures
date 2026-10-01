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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            for _ in range(2):
                fast = fast.next
            slow = slow.next
            if fast is slow:
                return True
        return False
    
    def get(self,index):
        if self.length == 0:
            return None

        if self.length <= index or index < 0:
            return None
        
        count = 0
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.get(2).next = my_linked_list.head
print(my_linked_list.has_loop())