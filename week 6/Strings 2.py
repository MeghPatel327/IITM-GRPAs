def even_first_odd_reversed(s: str) -> str:
    s_out = s[::2] + s[1::2][::-1]
    return s_out