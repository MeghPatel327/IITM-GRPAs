def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    string = list(string)
    new_str = ''
    for char in string[1::2]:
        new_str += char
    a = new_str.isalpha()
    new_str = ''
    for char in string[::2]:
        new_str += char
    b = new_str.isnumeric()
    return a and b