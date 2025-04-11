def number_of_unique_common_digits(n1: int, n2: int) -> int:
    return len(set(str(n1)) & set(str(n2)))  
