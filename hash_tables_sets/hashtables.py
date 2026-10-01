class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i , ": " , val)
        print()

    def set_item(self,key,value):
        adress = self.__hash(key)
        if self.data_map[adress] is None:
            self.data_map[adress] = []
            self.data_map[adress].append([key,value])
        else:
            for i,x in enumerate(self.data_map[adress]):
                if key == x[0]:
                    self.data_map[adress][i] = [key,value]
                    return
            self.data_map[adress].append([key,value])

    def get_item(self,key):
        address = self.__hash(key)
        if self.data_map[address]:
            for x in self.data_map[address]:
                    if key == x[0]:
                        return x[1]
        return None
    
    def keys(self):
        keys = []
        for x in self.data_map:
            if x:
                for y in x:
                    keys.append(y[0])
        return keys



def common_element(list1,list2):
    my_hash = HashTable()
    for x in list1:
        my_hash.set_item(str(x),True)
    for x in list2:
        if my_hash.get_item(str(x)):
            return True
    return False

my_hash = HashTable() 
my_hash.print_table()
my_hash.set_item("key","value")
my_hash.print_table()
my_hash.set_item("ahmet", "semraa")
my_hash.print_table()
my_hash.set_item("ahmet","semra")
my_hash.print_table()
my_hash.set_item("abs","ahmet")
my_hash.print_table()
print(my_hash.get_item("ahmet"))
print(my_hash.keys())

list1 = [1,2,3]
list2 = [8,4,5]
print(common_element(list1,list2))