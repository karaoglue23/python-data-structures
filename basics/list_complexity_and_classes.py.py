mylist = [0,1,2,3]

mylist.append(4) # no reindexing
mylist.pop() # no reindexing
#they are O(1)

mylist.pop(0) # all others need to be reindexed
mylist.insert(0,0) # all others need to be reindexed again
#they are O(n) n is the number of items in the list

mylist.insert(2,2) # only the half need to be reindexed so 1/2n and we drop constants so it is O(n)
mylist.pop(2) # O(n)

class Cookie:
    def __init__(self,color): # constructor
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color
    
    
cookie1 = Cookie("green")
cookie2 = Cookie("blue")

print(f"cookie1 is {cookie1.get_color()}")
print(f"cookie2 is {cookie2.get_color()}")

cookie1.set_color("yellow")
print(f"cookie1 is now {cookie1.get_color()}")

while True:
    print(1)