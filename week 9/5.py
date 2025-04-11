def ancestry(P, present, past):
    if present == past:
        return [past]
    if present not in P:
        return None  # If the present person is not in P, no path exists
    parent = P[present]
    path = ancestry(P, parent, past)
    return [present] + path if path else None