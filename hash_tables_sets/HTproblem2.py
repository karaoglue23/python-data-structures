def first_non_repeating_char(word):
    dict1 = {}
    for char in word:
        if dict1.get(char) is None:
            dict1[char] = 1
        else:
            dict1[char] += 1
    for k,v in dict1.items():
        if v == 1:
            return k
    return None

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""