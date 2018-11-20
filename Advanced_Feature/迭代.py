def findMinAndMax(L):
    import sys
    if not len(L):
        return None, None
    min_val, max_val = sys.maxsize, -sys.maxsize
    for i in L:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val, max_val
