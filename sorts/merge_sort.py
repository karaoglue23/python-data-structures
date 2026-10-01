def merge(sorted_list1,sorted_list2):
    i = 0 
    j = 0
    merged_list = []
    if len(sorted_list1) == 0:
        return sorted_list2
    if len(sorted_list2) == 0:
        return sorted_list1
    
    not_complete = False
    for _ in range(len(sorted_list1)+len(sorted_list2)):
        if i < len(sorted_list1) and j < len(sorted_list2):
            if sorted_list1[i] <= sorted_list2[j]:
                merged_list.append(sorted_list1[i])
                i += 1
            else:
                merged_list.append(sorted_list2[j])
                j += 1
        else:
            not_complete = True
            break

    if not_complete:
        if i >= len(sorted_list1):
            merged_list.extend(sorted_list2[j:])
        if j >=len(sorted_list2):
            merged_list.extend(sorted_list1[i:])
    return merged_list

def merge_sort(list1):
    if len(list1) == 1:
        return list1
    mid_index = int(len(list1)/2)
    left = merge_sort(list1[:mid_index])
    right = merge_sort(list1[mid_index:])
    return merge(left,right)

print(merge_sort([1,3,7,9,15,-1,5]))
        