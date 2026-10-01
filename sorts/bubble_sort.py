def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([3,4,2,7,1,9]))