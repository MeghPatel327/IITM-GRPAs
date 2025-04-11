def steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
