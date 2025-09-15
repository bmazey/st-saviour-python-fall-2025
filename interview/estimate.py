
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """
    integer_part = int(number)
    decimal_part = number - integer_part

    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part