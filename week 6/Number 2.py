def is_ten_digit_even(n):
    if len(str(abs(n))) == 10 and n % 2 == 0:
        return True
    else:
        return False