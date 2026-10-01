class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
            new_node.prev = current
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
        
    def reverse_between(self, start_index, end_index):
            if self.length <= 1 or start_index == end_index:
                return
    
            dummy = Node(0)
            dummy.next = self.head
            self.head.prev = dummy
    
            prev = dummy
            for _ in range(start_index):
                prev = prev.next
    
            current = prev.next
    
            for _ in range(end_index - start_index):
                node_to_move = current.next
    
                current.next = node_to_move.next
                if node_to_move.next:
                    node_to_move.next.prev = current
    
                node_to_move.next = prev.next
                prev.next.prev = node_to_move
                prev.next = node_to_move
                node_to_move.prev = prev
    
            self.head = dummy.next
            self.head.prev = None

        


my_DLL = DoublyLinkedList(1)
my_DLL.append(2)
my_DLL.append(3)
my_DLL.append(4)
my_DLL.append(5)
my_DLL.reverse_between(1,3)
my_DLL.print_list()
        


