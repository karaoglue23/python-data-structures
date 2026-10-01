def find_pairs(arr1,arr2,target):
    pairs = []
    set1 = set(arr1)
    for num in arr2:
        if target - num in set1:
            pairs.append((target - num,num))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6,]
target = 5

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""