def has_a_in_second_half(s: str) -> bool:
    return True if 'a' in s[len(s)//2:].lower() else False