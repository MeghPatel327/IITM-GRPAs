def linear(P, Q, k, i=0):
    if i>len(P)-1:
        return True
    if len(P) != len(Q) or P[i] !=  k*Q[i]:
        return False
    else:
        return linear(P, Q, k, i+1)