def find_duplicates(list1):
    dict1 = {}
    duplicates = []
    for x in list1:
        if dict1.get(x) is None:
            dict1[x] = True
        else:
            if x not in duplicates: 
                duplicates.append(x)
    return duplicates


print( find_duplicates([1, 2, 3, 4, 5]) )
print( find_duplicates([1, 1, 2, 2, 3]) )
print( find_duplicates([1, 1, 1, 1, 1]) )
print( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

