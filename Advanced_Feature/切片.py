def trim(s):
    length = len(s)
    if not length:
        return s
    else :
        i, j = 0, length
        for item in s[0: length]:
            if item != " ":
                break
            i += 1
        for item in s[-1: -length: -1]:
            if item != " ":
                break
            j -= 1
    return s[i: j]
