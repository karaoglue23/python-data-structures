def insertion_sort(my_list):
    if len(my_list) > 1:
        for i in range(1,len(my_list)):
            for j in range(i,0,-1):
                if my_list[j] < my_list[j-1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j-1]
                    my_list[j-1] = temp
                else:
                    break
    return my_list

print(insertion_sort([2,4,1,-3,12,-9,5]))
