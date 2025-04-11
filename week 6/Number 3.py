def arithmetic_operations(t: tuple) -> tuple:
    t = list(t)
    out = []
    out.append(t[0] + t[1])
    out.append(t[0] - t[1])
    out.append(t[0] * t[1])
    quotient = (t[0] - (t[0]% t[1])) // t[1]
    out.append(quotient)
    return tuple(out)