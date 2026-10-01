
def print_items(n): 
    for i in range(n):
        print(i)

print_items(10) # O(n) proporitonal
print("*"*10)
def print_items2(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items2(10) # n + n operations = 2n but its still O(n) # we drop constants
print("*"*10)
def print_items3(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items3(10) # n * n = n^2 operations therefore its O(n^2)
print("*"*10)
def print_items4(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items4(100) # n^2 + n we drop non dominants so it is O(n^2)
print("*"*10)

def add_items(n):
    return n+n

print(add_items(10)) # O(1) it's constant time it doesnt change when n increases
print("*"*10)

def halve_items(n):
    count = 0
    while n > 1:
        n /= 2
        count += 1
    print(count)

halve_items(256) # O(logn) how many times you need to halve something
print("*"*10)
def print_items5(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

print_items5(10,5) # a+b is O(a+b) cannot simplify if they are different terms same for O(a*b)
    

    

