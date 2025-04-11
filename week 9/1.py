def reverse(L, temp = []):
    if len(L) == 0:
        return temp
    else:
        temp.append(L[-1])
        return reverse(L[:-1], temp)