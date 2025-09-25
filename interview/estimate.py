
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    decimal = number - int(number)
    # this will add 1 if the decimal place is greater than 0.5 - you round up
    if decimal >= 0.5:
        result = int(number) + 1 
    # you would leave the else result alone since you would round down to the integer itself.
    else:
        result = int(number)  

    return result
