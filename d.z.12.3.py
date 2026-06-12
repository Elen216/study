ef is_even(num):
    last_digit = str(num)[-1]
    if last_digit in ('0', '2', '4', '6', '8'):
        return True
    else:
        return False
