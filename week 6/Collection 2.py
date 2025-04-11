def swap_alternate_elements(t):
    t = list(t)
    out = []
    for i in range(len(t)):
        if i % 2 != 0:
            out.insert(i, t[i-1])
        elif i % 2 == 0:
            out.insert(i, t[i+1])
    return tuple(out)