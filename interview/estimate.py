
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    decimal = number - int(number)

    if decimal >= 0.5:
        result = int(number) + 1 #plus 1 if the decimal place is greater than 0.5, you round up
    else:
        result = int(number) #leave it alone since you would round downto the integer itself. 

    return result
