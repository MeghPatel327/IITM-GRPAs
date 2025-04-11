def rotate_list(lst: list, k: int) -> list:
    return lst[k*(-1):] + lst[:k*(-1)]