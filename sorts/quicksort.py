def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(list1,pivot_index,end_index):
    if pivot_index == end_index:
        return pivot_index
    pivot = pivot_index
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if list1[i] < list1[pivot]:
            swap_index += 1
            swap(list1,i,swap_index)
    swap(list1,pivot,swap_index)
    pivot = swap_index
    return pivot

def quick_sort(list1,start_index,end_index):
    if start_index >= end_index:
        return
    pivot_final_index = pivot(list1,start_index,end_index)
    quick_sort(list1,start_index,pivot_final_index-1)
    quick_sort(list1,pivot_final_index+1,end_index)

my_list = [5,2,15,19,19,4,6,9,23,1]
quick_sort(my_list,0,9)
print(my_list)