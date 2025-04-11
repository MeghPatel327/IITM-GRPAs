def in_exactly_one(l1: list, l2: list) -> set:
    l1, l2 =set(l1), set(l2)
    out = l1.union(l2) - l1.intersection(l2)
    return out