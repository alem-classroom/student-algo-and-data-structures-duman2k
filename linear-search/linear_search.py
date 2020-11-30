def linear_search(lst, to_find):
    index = 0
    for item in lst:
        if item == to_find:
            return index
        index += 1
    return -1
    
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1