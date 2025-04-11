def common_char_sorted_str(s1:str, s2:str) -> str:
    s1, s2 = set(list(s1)), set(list(s2))
    temp = list(s1 & s2)
    out = ''.join(sorted(temp))
    return out