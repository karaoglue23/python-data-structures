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

    def insertion_sort(self):
        if self.length <=1:
            return
        sorted_part_head = self.head
        sorted_part_tail = self.head
        unsorted_part_head = self.head.next
        sorted_part_head.next = None
        while unsorted_part_head:
            current = unsorted_part_head
            unsorted_part_head = unsorted_part_head.next
            current.next = None
            if current.value <= sorted_part_head.value:
                current.next = sorted_part_head
                sorted_part_head = current
            else:
                sorted_part_current = sorted_part_head
                while sorted_part_current:
                    if sorted_part_current.next and sorted_part_current.next.value > current.value:
                        temp = sorted_part_current.next
                        sorted_part_current.next = current
                        current.next = temp
                        break
                    if sorted_part_current.next is None:
                        sorted_part_current.next = current
                        sorted_part_tail = current
                        break
                    sorted_part_current = sorted_part_current.next
        self.head = sorted_part_head
        self.tail = sorted_part_tail


                        





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

