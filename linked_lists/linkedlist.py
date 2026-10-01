class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self,value):
        new_node =  Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            popped = self.tail
            self.tail = temp
            self.tail.next = None
            self.length -= 1
            return popped
        
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            temp.next = None # disconnecting the node
            self.length -= 1
            return temp
        
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
    
    def set_value(self,index,value):
        temp = self.get(index) # using another method inside a method
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next # not using get() again
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.length <= 1:
            return

        current = self.head
        prev = None
        self.tail = self.head  # old head becomes new tail

        while current is not None:
            nxt = current.next   # save next node
            current.next = prev  # reverse pointer
            prev = current       # move prev forward
            current = nxt        # move current forward

        self.head = prev  

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
my_linked_list.print_list()

my_linked_list.append(5)
my_linked_list.print_list()

my_linked_list.make_empty()
my_linked_list.append(4)
my_linked_list.print_list()

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print(f"popped {my_linked_list.pop()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop()}")

my_linked_list.print_list()
my_linked_list.prepend(4)
my_linked_list.prepend(5)
my_linked_list.print_list()
my_linked_list.append(6)
my_linked_list.prepend(3)
my_linked_list.print_list()

print(f"popped {my_linked_list.pop_first()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop_first()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop_first()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop_first()}")
my_linked_list.print_list()
print(f"popped {my_linked_list.pop_first()}")

my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(2)
print(my_linked_list.get(2).value)

my_linked_list.print_list()
my_linked_list.set_value(1,6)
my_linked_list.print_list()

my_linked_list.insert(1,5)
my_linked_list.print_list()

print(my_linked_list.remove(1),"\n")
my_linked_list.print_list()
my_linked_list.append(7)
my_linked_list.append(17)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()