def collatz(n, count=0):
    if n<1:
        return None
    if n == 1:
        return count 
    else:
        return collatz((n/2) if n%2==0 else (3*n+1), count + 1)