def square_root(number):
    if isinstance(number, int) and number > 1:
        number = number**(1/2)
    return number
