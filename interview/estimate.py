
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    decimal = number - int(number)
    # must be greater than 0.5
    if decimal >= 0.5:
        result = int(number) + 1
    else:
        result = int(number)
    
    return result
